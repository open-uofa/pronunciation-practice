from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.db import transaction
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from .models import *
from .serializers import *

class HelpfulTestMethods:
    # This class is meant to be another superclass to classes that test models
    # It provides helpful functions used in many of those classes
    def get_required_fields(self, model, excluded_fields=[]):
        # Get the required fields of a model that are not automatically assigned.
        # Some fields should be excluded as their test is different than a group
        # of other fields
        return [field.name for field in model._meta.get_fields() \
                    if not field.null and field.name != 'id' and field.name not in excluded_fields]

    def compare_attributes(self, model_instance, attributes):
        # Compare the attributes manually assigned while creating a model instance in setUp to 
        # the attributes of a model fetched from the database.
        for attribute in attributes:
            self.assertEqual(getattr(model_instance, attribute), attributes[attribute])

class UserModelTest(TestCase, HelpfulTestMethods):
    def setUp(self):
        self.user_attributes = {
            "username":"test_user", 
            "password":"test_pass", 
            "first_name":"test", 
            "last_name":"user", 
            "role":User.RoleChoices.STUDENT
        }
        self.test_user = User.objects.create(**self.user_attributes)
        return super().setUp()
    
    def test_user_exists(self):
        fetched_user = User.objects.get(username=self.user_attributes["username"])
        self.assertEqual(self.test_user, fetched_user)
        self.compare_attributes(fetched_user, self.user_attributes)
    
    def test_add_existing_username(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(username=self.user_attributes["username"], first_name="test", last_name="user", role=User.RoleChoices.STUDENT)

    def test_default_values(self):
        self.assertEqual(self.test_user.is_staff, False)
        self.assertEqual(self.test_user.is_admin, False)
        self.assertEqual(self.test_user.is_active, True) 
    
    def test_required_fields_not_included(self):
        default_user_fields = ['is_active', 'admin', 'staff']
        required_fields = self.get_required_fields(User, default_user_fields)
        with self.assertRaises(ValidationError) as cm:
            User.objects.create().clean_fields()
        for field_name in required_fields:
            assert(field_name in dict(cm.exception))

    def test_different_roles(self):
        # Student, Parent, Teacher, and Content Creator are proxy classes of User, where a User
        # belongs to the proxy class if the User's role matches the corresponding proxy class
        # Here, I test that functionality
        
        attributes = self.user_attributes
        

        # The different roles with the different models associated with them
        roles_to_models = {
            User.RoleChoices.STUDENT: Student,
            User.RoleChoices.PARENT: Parent,
            User.RoleChoices.TEACHER: Teacher,
            User.RoleChoices.CONTENT_CREATOR: ContentCreator
        }

        for test_role, model in roles_to_models.items():
            attributes["username"] = f"new_{test_role}"
            attributes["role"] = test_role
            # Create a new user with role test_role
            new_user = User.objects.create(**attributes)
            # Make sure this user exists in the model corresponding to the role
            self.assertEqual(model.objects.filter(id=new_user.id).count(), 1)
            # Make sure this user does not exist in the models not corresponding to the role
            for role, model in roles_to_models.items():
                if role != test_role:
                    self.assertEqual(model.objects.filter(id=new_user.id).count(), 0)

class TabModelTest(TestCase, HelpfulTestMethods):
    def setUp(self):
        self.tab_attributes = {
            "name": "Test Tab"
        }
        self.test_tab = Tab.objects.create(**self.tab_attributes)
        return super().setUp()

    def test_tab_exists(self):
        fetched_tab = Tab.objects.get(id=self.test_tab.id)
        self.assertEqual(fetched_tab, self.test_tab)
        self.compare_attributes(fetched_tab, self.tab_attributes)
    
    def test_required_fields_not_included(self):
        required_fields = self.get_required_fields(Tab)
        with self.assertRaises(ValidationError) as cm:
            Tab.objects.create().clean_fields()
        for field_name in required_fields:
            assert(field_name in dict(cm.exception))

class ChapterModelTest(TestCase, HelpfulTestMethods):
    def setUp(self):
        tab = Tab.objects.create(name="Test Tab")
        self.chapter_attributes = {
            "name": "Test Chapter",
            "tab": tab
        }
        self.test_chapter = Chapter.objects.create(**self.chapter_attributes)
        return super().setUp()

    def test_chapter_exists(self):
        fetched_chapter = Chapter.objects.get(id=self.test_chapter.id)
        self.assertEqual(fetched_chapter, self.test_chapter)
        self.compare_attributes(fetched_chapter, self.chapter_attributes)
    
    def test_required_fields_not_included(self):
        required_fields = self.get_required_fields(Chapter, ['tab'])

        with self.assertRaises(ValidationError) as cm:
            # No chapter name
            Chapter.objects.create(tab=self.chapter_attributes["tab"]).clean_fields()
        for field_name in required_fields:
            assert(field_name in dict(cm.exception))

        with self.assertRaises(IntegrityError) as cm:
            # Chapter not associated with a tab
            Chapter.objects.create(name="Test No Tab")

class LessonModelTest(TestCase, HelpfulTestMethods):
    def setUp(self):
        tab = Tab.objects.create(name="Test Tab")
        self.test_chapter = Chapter.objects.create(name="Test Chapter", tab=tab)
        self.lesson_attributes = {
            "text": "Example Text",
            "audio": "Example Audio",
            "has_image": True,
            "chapter": self.test_chapter
        }
        self.test_lesson = Lesson.objects.create(**self.lesson_attributes)
        return super().setUp()

    def test_lesson_exists(self):
        fetched_lesson = Lesson.objects.get(id=self.test_lesson.id)
        self.assertEqual(fetched_lesson, self.test_lesson)
        self.compare_attributes(fetched_lesson, self.lesson_attributes)
    
    def test_required_fields_not_included(self):
        # 'has_image' is included because although it is required, it has a default value
        # so an error will not be raised if it is missing
        required_fields = self.get_required_fields(Lesson, ['chapter', 'has_image'])

        with self.assertRaises(ValidationError) as cm:
            # No chapter name
            Lesson.objects.create(chapter=self.lesson_attributes["chapter"]).clean_fields()
        for field_name in required_fields:
            assert(field_name in dict(cm.exception))

        with self.assertRaises(IntegrityError) as cm:
            # Lesson not associated with a chapter
            Lesson.objects.create()

class ParentStudentModelTest(TestCase, HelpfulTestMethods):
    def setUp(self):
        self.user_attributes = {
            "first_name": "test",
            "last_name": "test",
            "password": "testpass"
        }
        student_username = "test_student"
        parent_username = "test_parent"
        self.student = Student.objects.create(username=student_username, **self.user_attributes)
        self.parent = Parent.objects.create(username=parent_username, **self.user_attributes)

        self.parent_student_attributes = {
            "student": self.student,
            "parent": self.parent
        }
        self.parent_student = ParentStudent.objects.create(**self.parent_student_attributes)

        return super().setUp()
    
    def test_parent_student_exists(self):
        fetched_parent_student = ParentStudent.objects.get(student=self.student, parent=self.parent)
        self.compare_attributes(fetched_parent_student, self.parent_student_attributes)
        self.compare_attributes(fetched_parent_student.student, self.user_attributes)
        self.assertEqual(self.student.username, fetched_parent_student.student.username)
        self.compare_attributes(fetched_parent_student.parent, self.user_attributes)
        self.assertEqual(self.parent.username, fetched_parent_student.parent.username)
    
    def test_required_fields_not_included(self):
        with transaction.atomic():
            # ParentStudent not associated with either a student or a parent
            try:
                ParentStudent.objects.create()
            except IntegrityError:
                pass
        with transaction.atomic():
            # ParentStudent not associated with a parent
            try:
                ParentStudent.objects.create(student=self.student)
            except IntegrityError:
                pass
        with transaction.atomic():
            # ParentStudent not associated with a student
            try:
                ParentStudent.objects.create(parent=self.parent)
            except IntegrityError:
                pass

class StudentLessonModelTest(TestCase, HelpfulTestMethods):
    def setUp(self):
        self.student_attributes = {
            "username": "test_student",
            "first_name": "test",
            "last_name": "test",
            "password": "testpass"
        }
        self.student = Student.objects.create(**self.student_attributes)
        
        test_tab = Tab.objects.create(name="Test Tab")
        test_chapter = Chapter.objects.create(name="Test Chapter", tab=test_tab)
        self.lesson_attributes = {
            "text": "Test",
            "audio": "Test",
            "has_image": True,
            "chapter": test_chapter
        }
        self.lesson = Lesson.objects.create(**self.lesson_attributes)

        self.student_lesson_attributes = {
            "student": self.student,
            "lesson": self.lesson
        }
        self.student_lesson = StudentLesson.objects.create(**self.student_lesson_attributes)

        return super().setUp()
    
    def test_student_lesson_exists(self):
        fetched_student_lesson = StudentLesson.objects.get(student=self.student, lesson=self.lesson)
        self.compare_attributes(fetched_student_lesson, self.student_lesson_attributes)
        self.compare_attributes(fetched_student_lesson.student, self.student_attributes)
        self.compare_attributes(fetched_student_lesson.lesson, self.lesson_attributes)
    
    def test_required_fields_not_included(self):
        with transaction.atomic():
            # StudentLesson not associated with either a student or a lesson
            try:
                StudentLesson.objects.create()
            except IntegrityError:
                pass
        with transaction.atomic():
            # StudentLesson not associated with a lesson          
            try:
                StudentLesson.objects.create(student=self.student)
            except IntegrityError:
                pass
        with transaction.atomic():
            # StudentLesson not associated with student
            try:
                StudentLesson.objects.create(lesson=self.lesson)
            except IntegrityError:
                pass
        

class ContentViewTest(APITestCase):
    def setUp(self):
        
        self.student_username = "test_user"
        student = Student.objects.create(username=self.student_username, password="test_pass", first_name="test", last_name="test")
        self.id = student.id    
        # Creating 4 tabs, each containing 4 chapters, each containing 4 lessons
        self.n = 4
        for i in range(self.n):
            tab = Tab.objects.create(name=f"Tab {i}")
            for j in range(self.n):
                chapter = Chapter.objects.create(name=f"Chapter {j} of Tab {i}", tab=tab)
                for k in range(self.n):
                    lesson = Lesson.objects.create(text=f"Lesson {k} of Chapter {j} of Tab {k}", audio=f"Audio of lesson {i}:{j}:{k}", chapter=chapter)
                    # Assigning 2 lessons of 2 chapters of 2 tabs to the student
                    if i < self.n//2 and j < self.n//2 and k < self.n//2:
                        StudentLesson.objects.create(student=student, lesson=lesson)

        return super().setUp()
    
    def testGetAllLessonTabs(self):
        response = self.client.get(reverse("lesson_tabs"), format="json")
        response_lesson_tabs = response.data
        assert("tabs" in response_lesson_tabs)
        for tab in response_lesson_tabs["tabs"]:
            assert("id" in tab)
            assert("name" in tab)
            assert("chapters" in tab)
            self.assertEqual(len(tab["chapters"]), self.n)
            for chapter in tab["chapters"]:
                assert("id" in chapter)
                assert("name" in chapter)
                assert("tab" in chapter)
                self.assertEqual(str(chapter["tab"]), tab["id"])
                assert("lessons" in chapter)
                self.assertEqual(len(chapter["lessons"]), self.n)
                for lesson in chapter["lessons"]:
                    assert("id" in lesson)
                    assert("text" in lesson)
                    assert("audio" in lesson)
                    assert("has_image" in lesson)
                    assert("chapter" in lesson)
                    self.assertEqual(str(lesson["chapter"]), chapter["id"])
    
    def testGetStudentLessonTabs(self):
        response = self.client.get(reverse("student_lesson_tabs", args=[self.id]), format="json")
        response_lesson_tabs = response.data
        assert("tabs" in response_lesson_tabs)
        for tab in response_lesson_tabs["tabs"]:
            assert("id" in tab)
            assert("name" in tab)
            assert("chapters" in tab)
            self.assertEqual(len(tab["chapters"]), self.n//2)
            for chapter in tab["chapters"]:
                assert("id" in chapter)
                assert("name" in chapter)
                assert("tab" in chapter)
                self.assertEqual(str(chapter["tab"]), tab["id"])
                assert("lessons" in chapter)
                self.assertEqual(len(chapter["lessons"]), self.n//2)
                for lesson in chapter["lessons"]:
                    assert("id" in lesson)
                    assert("text" in lesson)
                    assert("audio" in lesson)
                    assert("has_image" in lesson)
                    assert("chapter" in lesson)
                    self.assertEqual(str(lesson["chapter"]), chapter["id"])

    def testUnfinishedList(self):
        response = self.client.get(reverse("unfinished_list", args=[self.id]), format="json")
        unfinished_lessons = response.data
        self.assertEqual(len(unfinished_lessons), self.n*2)
        for lesson in unfinished_lessons:
            assert("id" in lesson)
            assert("student" in lesson)

    def testFinishedList(self):
        response = self.client.get(reverse("finished_list", args=[self.id]), format="json")
        finished_lessons = response.data
        self.assertEqual(len(finished_lessons), 0)        
   
    def testParentStudentList(self):
        parent = Parent.objects.create(username="parent", password="parent", first_name="parent", last_name="parent")
        ParentStudent.objects.create(parent=parent, student=Student.objects.get(username=self.student_username))
        response = self.client.get(reverse("parent_student_list", args=[parent.id]), format="json")
        students = response.data
        self.assertEqual(len(students), 1)
        student = students[0]
        assert("id" in student)
    
    def testAssignChapter(self):
        parent = Parent.objects.create(username="parent", password="parent", first_name="parent", last_name="parent")
        ParentStudent.objects.create(parent=parent, student=Student.objects.get(username=self.student_username))
        chapter = Chapter.objects.get(name="Chapter 0 of Tab 0")
        response = self.client.post(reverse("assign_chapter", args=[parent.id, self.id]), {"chapter": chapter.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StudentLesson.objects.filter(student=Student.objects.get(username=self.student_username), lesson__chapter=chapter).count(), self.n//2)
    


class ParentListTests(APITestCase):

    def setUp(self):
        self.url = reverse("parent_list")
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Parent"
        }
        
    def test_list_parents(self):
        # Create a parent
        Parent.objects.create(**self.valid_data)

        # Make a GET request
        response = self.client.get(self.url)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data returned
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        self.assertEqual(response.data, serializer.data)


    def test_create_invalid_parent(self):
        # Make a POST request with invalid data
        invalid_data = {
            'username': '',
            'password': 'password123',
            'first_name': '',
            'last_name': 'Doe',
            'role': 'Parent'
        }
        response = self.client.post(self.url, invalid_data, format="json")

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ParentDetailTests(APITestCase):

    def setUp(self):
        self.parent = Parent.objects.create(**{
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'password123'
        })
        self.url = reverse("parent_detail", args=[self.parent.pk])
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Parent"
        }
class StudentListTests(APITestCase):
    def setUp(self):
        self.url = reverse("student_list")
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Student"
        }

    def test_list_students(self):
        # Create a student
        Student.objects.create(**self.valid_data)

        # Make a GET request
        response = self.client.get(self.url)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data returned
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_invalid_student(self):
        # Make a POST request with invalid data
        invalid_data = {} # Add some invalid data
        response = self.client.post(self.url, invalid_data, format="json")

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class StudentDetailTests(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(**{
            # Add the required fields and their values
        })
        self.url = reverse("student_detail", args=[self.student.pk])
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Studnet",
        }
    def test_get_valid_student(self):
        # Make a GET request
        response = self.client.get(self.url)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data returned
        serializer = StudentSerializer(self.student)
        self.assertEqual(response.data, serializer.data)

class TeacherListTests(APITestCase):
    def setUp(self):
        self.url = reverse("teacher_list")
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Teacher",
        }

    def test_list_teachers(self):
        # Create a teacher
        Teacher.objects.create(**self.valid_data)

        # Make a GET request
        response = self.client.get(self.url)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data returned
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_invalid_teacher(self):
        # Make a POST request with invalid data
        invalid_data = {} # Add some invalid data
        response = self.client.post(self.url, invalid_data, format="json")

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TeacherDetailTests(APITestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(**{
            # Add the required fields and their values
        })
        self.url = reverse("teacher_detail", args=[self.teacher.pk])
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Teacher",
        }

    def test_get_valid_teacher(self):
        # Make a GET request
        response = self.client.get(self.url)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data returned
        serializer = TeacherSerializer(self.teacher)
        self.assertEqual(response.data, serializer.data)


class ContentCreatorListTests(APITestCase):
    def setUp(self):
        self.url = reverse("content_creator_list")
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Content Creator",
        }

    def test_list_contentcreators(self):
        # Create a contentcreator
        ContentCreator.objects.create(**self.valid_data)

        # Make a GET request
        response = self.client.get(self.url)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data returned
        contentcreators = ContentCreator.objects.all()
        serializer = ContentCreatorSerializer(contentcreators, many=True)
        self.assertEqual(response.data, serializer.data)

class ContentCreatorDetailTests(APITestCase):
    def setUp(self):
        self.contentcreator = ContentCreator.objects.create(**{
            # Add the required fields and their values
        })
        self.url = reverse("content_creator_detail", args=[self.contentcreator.pk])
        self.valid_data = {
            "username":"john",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "role": "Content Creator",
        }

    def test_get_valid_contentcreator(self):
        # Make a GET request
        response = self.client.get(self.url)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the data returned
        serializer = ContentCreatorSerializer(self.contentcreator)
        self.assertEqual(response.data, serializer.data)    




    