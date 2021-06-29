from django.urls import path
from .views import *

urlpatterns = [
    path('course/',CourseView.as_view()),
    path('courses/',CoursesView.as_view()),
    # path('<slug:subject_slug>/',CoursesView.as_view()),
]
