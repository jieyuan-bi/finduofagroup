from django.shortcuts import render
from django.template import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
from .models import *
import logging
from rest_framework.permissions import IsAuthenticated

# Get an instance of a logger
logger = logging.getLogger(__name__)

# returns all the catalogues and subjects
class CourseView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        '''
        fetch data and create database
        '''
        # catalogue, catalogue_abbrev = init_catalogues_database()
        # subject = {} #{catalogue_abbrev1: subject_list, catalogue2:subject_list, c3:...}
        # subject_abbrev = {} #{catalogue_abbrev1: subject_abbrev_list, catalogue2:subject_abbrev_list, c3:...}
        # for i in range(len(catalogue)):
        #     logger.info("[Courses View] faculty abbrev: %s" % catalogue_abbrev[i])
        #     subject[catalogue_abbrev[i]] = init_subjects_database(catalogue_abbrev[i])[0]
        #     subject_abbrev[catalogue_abbrev[i]] = init_subjects_database(catalogue_abbrev[i])[1]
            
        catalogues = CatalogueModel.objects.all()
        subjects = SubjectModel.objects.all()
        response = {}
        #catalogue returns [[cat1,cat-abb1], [cat2,cat-abb2], []...}
        response['catalogue'] = []
        for i in catalogues:
            response['catalogue'].append([i.name, i.slug])
        #subject returns {cata_slug:[[sub1,sub-abb1],[sub2,sib-abb2],...], cata_slug2:[],...}
        response['subject'] = {}
        for i in subjects:
            if i.catalogue.slug in response['subject'].keys():
                response['subject'][i.catalogue.slug].append([i.name, i.slug])
            else:
                response['subject'][i.catalogue.slug] = [[i.name, i.slug],]
        return Response(response)

# returns all the courses correspond to subject
class CoursesView(APIView):    
    def get(self, request, *args, **kwargs):
        '''
        fetch data and create database
        '''
        # subjects = SubjectModel.objects.all()
        # for subject in subjects:
        #     init_courses_database(subject.slug)

        response={}
        subject_slug = request.GET.get('subject_slug')

        # check if the user is search for class or using menu
        if subject_slug=="search":
            query = request.GET.get('query')
            # logger.info("[Courses] Classes subjectslug!"+ query)
            response['classes']=[]
            results = search_courses(query)
            for result in results:
                response['classes'].append([result.name,result.title,result.description])
        # using menu
        else:
            subject = SubjectModel.objects.filter(slug=subject_slug)
            # classes format [[name, title, description], [name, title, description], ...]
            response['classes']=[]
            if subject:            
                for i in ClassModel.objects.filter(subject=subject[0]):
                    response['classes'].append([i.name, i.title, i.description])
                # response['classes']=ClassModel.objects.filter(subject=subject[0])
        return Response(response)