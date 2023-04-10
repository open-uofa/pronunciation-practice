from django.urls import path
from .views import *
from rest_framework_nested import routers
from .viewsets import LoginViewSet, RefreshTokenViewSet

router = routers.SimpleRouter()
router.register(r'login', LoginViewSet, basename='auth_login')
router.register(r'refresh', RefreshTokenViewSet, basename='auth_refresh')

urlpatterns = [
    path('register/', AuthorCreate.as_view()),
    path('parents/', parent_list, name='parent_list'),
    path('parents/<uuid:pk>/', parent_detail, name='parent_detail'),
    path('students/', student_list, name='student_list'),
    path('students/<uuid:pk>/', student_detail, name='student_detail'),
    path('students/<uuid:student_id>/lessons/<uuid:lesson_id>', update_student_lesson, name="update_student_lesson"),
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/<uuid:pk>/', teacher_detail, name='teacher_detail'),
    path('content-creators/', content_creator_list, name='content_creator_list'),
    path('content-creators/<uuid:pk>/', content_creator_detail, name='content_creator_detail'),
    path('unfinished/<uuid:pk>/lessons/', unfinished_list, name='unfinished_list'),
    path('finished/<uuid:pk>/lessons/', finished_list, name='finished_list'),
    path('parentstudent/', parent_student, name = 'parent_student'),
     path('parentstudent/<uuid:parent_id>', parent_student_list, name = 'parent_student_list'),
     path('studentlesson/add/<uuid:lesson_id>/<uuid:student_id>', student_lesson, name = 'student_lesson'),
     path('studentchapter/add/<uuid:chapter_id>/<uuid:student_id>', assign_chapter, name = 'assign_chapter'),
     path('users/', user_list, name='user_list'),
     path('users/<uuid:pk>/', user_detail, name='user_detail'),
    *router.urls,
]