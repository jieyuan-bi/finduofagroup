import mechanicalsoup
import re
import logging
from django.db.models import Q
from .models import *

# Get an instance of a logger
logger = logging.getLogger(__name__)

# get all catalogue
# @param None
# @return list of faculty, list of faculty slug


def get_catalogues():
    browser = mechanicalsoup.StatefulBrowser()

    browser.open("https://apps.ualberta.ca/catalogue")

    draft = str(browser.page.find_all('li'))

    list = []

    list = re.findall('<a href="/catalogue/faculty/.*?</a></li>', draft)

    for i in range(len(list)):
        list[i] = re.sub('</a></li>', '', list[i])
        list[i] = re.sub('<a.*?>', '', list[i])
    faculty = []
    faculty_abbrev = []
    for i in range(len(list)):
        abbrev, name = list[i].split(' - ')
        faculty.append(name)
        faculty_abbrev.append(abbrev)
    logger.info("[Courses] faculty: %s, abbrev: %s" %
                (faculty[0], faculty_abbrev[0]))
    return faculty, faculty_abbrev

# add all catalogues into database


def init_catalogues_database():
    faculty, faculty_abbrev = get_catalogues()
    for i in range(len(faculty)):
        name = faculty[i]
        slug = faculty_abbrev[i]
        # first make sure if the course is in the database, if it's not, create it
        try:
            CatalogueModel.objects.get(name=name)
            logger.info("[Courses] Catalogue already exist!")
        except Exception:
            CatalogueModel.objects.create(name=name, slug=slug)
            logger.info("[Courses] Created catalogue %s!" % name)
    return faculty, faculty_abbrev

# get the subjects of one catalogue
# @param catalogue abbrev
# @return [list of subject, list of subject slug, catalogue]


def get_subjects(catalogue):
    browser = mechanicalsoup.StatefulBrowser()

    browser.open("https://apps.ualberta.ca/catalogue/faculty/"+catalogue)

    draft = str(browser.page.find_all('li'))

    list = []

    list = re.findall('<a href="/catalogue/course/.*?</a></li>', draft)

    for i in range(len(list)):
        list[i] = re.sub('</a></li>', '', list[i])
        list[i] = re.sub('<a.*?>', '', list[i])
        list[i] = re.sub('&amp;', '&', list[i])
    subject = []
    subject_abbrev = []
    for i in range(len(list)):
        # the format is different because some subjects has extra '-'
        abbrev, name = list[i].split(' - ')[0], list[i].split(' - ')[-1]
        subject.append(name)
        subject_abbrev.append(abbrev)
    c_id = get_catalogue(catalogue)
    return [subject, subject_abbrev, c_id]

# get the catalogue with catalogue abbrev
# @param name of catalogue
# @return object of catalogue


def get_catalogue(catalogue):
    catalogue = CatalogueModel.objects.get(slug=catalogue)
    logger.info("[Courses] Catalogue_ID: %d" % catalogue.id)
    return catalogue

# add all subjects into database
# @param name of catalogue abbrev
# @return [name list, slug list]


def init_subjects_database(catalogue):
    # get subject info [name list, slug list, cate_id]
    subjects_info = get_subjects(catalogue)
    # iterate subject name and save names, slugs, and correspond catalogue id
    for i in range(len(subjects_info[0])):
        name = subjects_info[0][i]
        slug = subjects_info[1][i]
        catalogue = subjects_info[2]
        # first make sure if the course is in the database, if it's not, create it
        try:
            SubjectModel.objects.get(name=name, slug=slug, catalogue=catalogue)
            logger.info("[Courses] Subject %s already exist!" % slug)
        except Exception:
            SubjectModel.objects.create(
                name=name, slug=slug, catalogue=catalogue)
            logger.info("[Courses] Created subject %s!" % name)
    return subjects_info[:2]

# get the courses of one subject
# @param subject abbrev
# @return {name:[list of name],title:[list of title],desc:[list of disc],subject:subject object}


def get_courses(subject):
    

    browser = mechanicalsoup.StatefulBrowser()


    browser.open("https://apps.ualberta.ca/catalogue/course/" +
                 '_'.join(subject.split()))

    draft = str(browser.page.find_all("div", class_="card-body"))

    list = re.findall('<div class="card-body">.*?</p>', draft, re.DOTALL)
    # print(list[0],list[2])

    class_list = {}
    class_list['name'] = []
    class_list['title'] = []
    class_list['description'] = []
    class_list['subject'] = get_subject(subject)

    if not list:
        list = re.findall('<div class="card-body">.*?</div>',draft, re.DOTALL)
        for i in range(len(list)):
            name_title = re.sub('<span class="float-right">.*','',list[i], 0, re.DOTALL)
            name_title = re.sub('<div class="card-body">.*?flex-grow-1">','',name_title, 0, re.DOTALL)
            desc = re.sub('.*?warning">', '', list[i], 0, re.DOTALL)
            desc = re.sub('</div>.*', '', desc, 0, re.DOTALL)
            # get and save correspond name, title, and desc
            class_list['name'].append(' '.join(name_title.split('-')[0].split()))
            class_list['title'].append(' '.join(name_title.split('-')[1].split()))
            class_list['description'].append(desc)
    else:
        for i in range(len(list)):
            name_title = re.sub(
                '<span class="float-right">.*?</p>', '', list[i], 0, re.DOTALL)
            name_title = re.sub(
                '<div class="card-body">.*?flex-grow-1">', '', name_title, 0, re.DOTALL)
            desc = re.sub('.*?<p>', '', list[i], 0, re.DOTALL)
            desc = re.sub('</p>', '', desc, 0, re.DOTALL)
            # get and save correspond name, title, and desc
            class_list['name'].append(' '.join(name_title.split('-')[0].split()))
            class_list['title'].append(' '.join(name_title.split('-')[1].split()))
            class_list['description'].append(desc)

    return class_list

# get the subject with subject abbrev
# @param name of subject
# @return object of subject


def get_subject(subject):
    subject = SubjectModel.objects.filter(slug=subject).first()
    logger.info("[Courses] Subject_ID: %d" % subject.id)
    return subject

# add all courses into database
# @param name of subject abbrev
# @return {name:[list of name],title:[list of title],desc:[list of disc],subject:subject object}


def init_courses_database(subject_slug):
    # get course info {name:[list of name],title:[list of title],desc:[list of disc],subject:subject object}
    courses_info = get_courses(subject_slug)
    # iterate course name and save names, title, desc, and correspond subject
    for i in range(len(courses_info['name'])):
        name = courses_info['name'][i]
        title = courses_info['title'][i]
        description = courses_info['description'][i]
        subject = courses_info['subject']
        # first make sure if the course is in the database, if it's not, create it
        try:
            ClassModel.objects.get(
                name=name, title=title, description=description, subject=subject)
            logger.info("[Courses] Course %s already exist!" % name)
        except Exception:
            ClassModel.objects.create(
                name=name, title=title, description=description, subject=subject)
            logger.info("[Courses] Created course %s!" % name)
    return courses_info


# search and return all courses according to query
# @param query from user input
# @return an empty list or a list of ClassModel object

def search_courses(query):
    result = []
    # search according to class number or class name
    id = re.findall("\d+",query)
    name = re.findall("[a-zA-Z]+",query)
    # logger.info("!!!!!!!!!!!!![Courses] id:%s , name:%s" %(id,name))
    if id and name:
        id = id[0]
        name = name[0]
        filter_result = ClassModel.objects.filter((Q(name__icontains=id) & Q(name__icontains=name)) |Q(title__icontains=name))
        for j in filter_result:
            # logger.info("[Courses] Search course :" + j.name)
            result.append(j)
    elif id:
        id = id[0]
        filter_result = ClassModel.objects.filter(Q(name__icontains=id))
        for j in filter_result:
            # logger.info("[Courses] Search course :" + j.name)
            result.append(j)
    elif name:
        name = name[0]
        filter_result = ClassModel.objects.filter(Q(name__icontains=name) |Q(title__icontains=name))
        for j in filter_result:
            # logger.info("[Courses] Search course :" + j.name)
            result.append(j)
    else:
        pass
    # logger.info("[Courses] Search result :" + result[0].name)
    return result
