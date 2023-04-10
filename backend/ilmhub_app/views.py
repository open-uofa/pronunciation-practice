import os, zipfile, pathlib, shutil
from django.shortcuts import render, get_object_or_404
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import transaction
from rest_framework import viewsets, status, generics, mixins, response
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Student, Parent, Teacher, ContentCreator, Lesson, Chapter, Tab, StudentLesson, ParentStudent
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from IlmHub.settings import MEDIA_ROOT
from django.db.models.functions import Length
from django.db.models import Q

class AuthorCreate(generics.CreateAPIView):

    # queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        This function is a view for the API endpoint that creates a new user.

        :param request: The HTTP request object (POST).
        :type request: HttpRequest

        :return: A HTTP 201 Created response with the new user's data, or a HTTP 400 Bad Request response if the data is invalid.
        :rtype: HttpResponse
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def user_list(request):
    """
    This function is a view for the API endpoint that lists all users.

    :param request: The HTTP request object (GET).
    :type request: HttpRequest

    :return: A list JSON objects representing all users.
    :rtype: HttpResponse
    """

    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
@api_view(["GET"])
def user_detail(request, pk):
    """
    This function is a view for the API endpoint that retrieves an individual user by their ID.

    :param request: The HTTP request object (GET).
    :type request: HttpRequest
    :param pk: The ID of the user to retrieve.
    :type pk: string

    :return: A JSON object representing the user, or a HTTP 404 Not Found response if the user does not exist.
    :rtype: HttpResponse
    """

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(["GET", "POST"])
def parent_list(request):
    """ List all parents, or create a new parent.

    This function is a view for the API endpoint that lists all parents, or creates a new parent.

    :param request: The HTTP request object (either GET or POST).
    :type request: HttpRequest
    :return: A list JSON objects representing all parents, or a HTTP 201 Created response with the new parent's data.
    :rtype: HttpResponse
    """
    
    if request.method == "GET":
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = UserCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # ParentStudent.objects.create(parent=serializer.data, student=Student.objects.filter(student__)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET", "PUT", "DELETE"])
def parent_detail(request, pk):
    """ Retrieve, update or delete an individual parent.
    
    This function is a view for the API endpoint that retrieves, updates or deletes an individual parent.
    
    :param request: The HTTP request object (either GET, PUT or DELETE).
    :type request: HttpRequest
    :param pk: The primary key of the parent to retrieve, update or delete.
    :type pk: string
    :return: A JSON object representing the parent, a HTTP 204 No Content response, or a HTTP 404 Not Found response.
    :rtype: HttpResponse
    """

    try:
        parent = Parent.objects.get(pk=pk)
    except Parent.DoesNotExist:
        return Response({"error": "Parent not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ParentSerializer(parent)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def student_list(request):
    """
    This function is a view for the API endpoint that lists all students, or creates a new student.

    :param request: The HTTP request object (either GET or POST).
    :type request: HttpRequest
    :return: A list JSON objects representing all students, or a HTTP 201 Created response with the new student's data.
    :rtype: HttpResponse
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, pk):
    """
    This function is a view for the API endpoint that retrieves, updates or deletes an individual student.

    :param request: The HTTP request object (either GET, PUT or DELETE).
    :type request: HttpRequest
    :param pk: The primary key of the student to retrieve, update or delete.
    :type pk: string
    :return: A JSON object representing the student, a HTTP 204 No Content response, or a HTTP 404 Not Found response.
    :rtype: HttpResponse
    """

    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def teacher_list(request):
    """
    This function is a view for the API endpoint that lists all teachers, or creates a new teacher.

    :param request: The HTTP request object (either GET or POST).
    :type request: HttpRequest
    :return: A list JSON objects representing all teachers, or a HTTP 201 Created response with the new teacher's data.
    :rtype: HttpResponse
    """

    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def teacher_detail(request, pk):
    """
    This function is a view for the API endpoint that retrieves, updates or deletes an individual teacher.

    :param request: The HTTP request object (either GET, PUT or DELETE).
    :type request: HttpRequest
    :param pk: The primary key of the teacher to retrieve, update or delete.
    :type pk: string
    :return: A JSON object representing the teacher, a HTTP 204 No Content response, or a HTTP 404 Not Found response.
    :rtype: HttpResponse
    """
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def content_creator_list(request):
    """
    This function is a view for the API endpoint that lists all content creators, or creates a new content creator.

    :param request: The HTTP request object (either GET or POST).
    :type request: HttpRequest
    :return: A list JSON objects representing all content creators, or a HTTP 201 Created response with the new content creator's data.
    :rtype: HttpResponse
    """

    if request.method == 'GET':
        content_creators = ContentCreator.objects.all()
        serializer = ContentCreatorSerializer(content_creators, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def content_creator_detail(request, pk):
    """
    This function is a view for the API endpoint that retrieves, updates or deletes an individual content creator.

    :param request: The HTTP request object (either GET, PUT or DELETE).
    :type request: HttpRequest
    :param pk: The primary key of the content creator to retrieve, update or delete.
    :type pk: string
    :return: A JSON object representing the content creator, a HTTP 204 No Content response, or a HTTP 404 Not Found response.
    :rtype: HttpResponse
    """

    try:
        content_creator = ContentCreator.objects.get(pk=pk)
    except ContentCreator.DoesNotExist:
        return Response({"error": "Content Creator not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ContentCreatorSerializer(content_creator)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ContentCreatorSerializer(content_creator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        content_creator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["PUT"])
def update_student_lesson(request, student_id, lesson_id):
    """
    This function is a view for the API endpoint that updates the status of a student's lesson.

    :param request: The HTTP request object (PUT).
    :type request: HttpRequest
    :param student_id: The primary key of the student.
    :type student_id: string
    :param lesson_id: The primary key of the lesson.
    :type lesson_id: string
    :return: A HTTP 204 No Content response.
    :rtype: HttpResponse
    """

    student = Student.objects.get(pk=student_id)
    lesson = Lesson.objects.get(pk=lesson_id)
    student_lesson = StudentLesson.objects.get(student=student, lesson=lesson)
    
    data = request.data
    if data["status"] == StudentLesson.StatusChoices.COMPLETED:
        student_lesson.status = StudentLesson.StatusChoices.COMPLETED
    if data["status"] == StudentLesson.StatusChoices.ASSIGNED:
        student_lesson.status = StudentLesson.StatusChoices.ASSIGNED
    
    student_lesson.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ContentView(viewsets.ViewSet):
    """
    This class is a view for the API endpoint that lists all content, or creates a new content.

    :param viewsets.ViewSet: The base class for all viewsets.
    :type viewsets.ViewSet: ViewSet

    :return: A list JSON objects representing all content, or a HTTP 201 Created response with the new content's data.
    :rtype: HttpResponse
    """

    def student_exists(self, pk):
        return Student.objects.filter(pk=pk).count() > 0
    
    def custom_message_response(self, message, status_code):
        data = {"detail": message}
        return Response(data, status=status_code)
    
    def parent_exists(self, pk):
        return Parent.objects.filter(pk=pk).count() > 0

    # GET
    # //service/lessontabs/student/{username}
    @swagger_auto_schema(
        tags=["Lesson Tabs"],
        operation_description="Fetches the lessons associated with a student with username {username}, along with the chapters, and lesson tabs.",
        operation_summary="Fetches the lessons associated with a student, along with the chapters, and lesson tabs.",
        operation_id="get_student_lesson_tabs",
        method='GET',
        responses={
            "200": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "tabs": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Tab UUID"),
                                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Tab Name"),
                                "chapters": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            "id": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Chapter UUID"),
                                            "name": openapi.Schema(type=openapi.TYPE_STRING, description="Chapter Name"),
                                            "tab": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Tab UUID"),
                                            "lessons": openapi.Schema(
                                                type=openapi.TYPE_ARRAY,
                                                items=openapi.Schema(
                                                    type=openapi.TYPE_OBJECT,
                                                    properties={
                                                        "id": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Lesson UUID"),
                                                        "text": openapi.Schema(type=openapi.TYPE_STRING, description="Path to the file containing the textual component of the lesson. \
                                                                            File could be in text or image format."),
                                                        "audio": openapi.Schema(type=openapi.TYPE_STRING, description="Path to the file containing the audible component of the lesson."),
                                                        "has_image": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Is true if the file containing the textual component of the lesson \
                                                                                    is an image. false otherwise."),
                                                        "chapter": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Chapter UUID"),
                                                    }
                                                )
                                            )
                                        }
                                    )
                                )
                            }
                        )
                    )
                }
            ),
            "404": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(type=openapi.TYPE_STRING, description="Student does not exist.")
                }
            )
        }
    )
    @action(detail=True, methods=['get'])
    def get_student_lesson_tabs(self, request, *args, **kwargs):
        """
        This function is a view for the API endpoint that lists all lessons associated with a student, along with the chapters, and lesson tabs.

        :param request: The HTTP request object (GET).
        :type request: HttpRequest
        :return: A list JSON objects representing all lessons associated with a student, along with the chapters, and lesson tabs.
        :rtype: HttpResponse
        """
    
        student_id = kwargs["pk"]
        if not self.student_exists(student_id):
            return self.custom_message_response("Student does not exist.", status.HTTP_404_NOT_FOUND)

        student = Student.objects.get(id=student_id)
        data = {"tabs":[]}

        student_lessons = StudentLesson.objects.filter(student=student)

        lessons = Lesson.objects.filter(id__in=student_lessons.values('lesson')).order_by(Length('text'),'text')
        chapters = Chapter.objects.filter(id__in=lessons.values('chapter'))
        tabs = Tab.objects.filter(id__in=chapters.values('tab'))
        
        for tab in tabs:
            # append each lesson tab to the 'tabs' key in the data dictionary
            serialized_tab = TabSerializer(tab).data
            data["tabs"].append(serialized_tab)
            
            # get each chapter in the lesson tab
            serialized_tab["chapters"] = []
            tab_chapters = chapters.filter(tab=tab)
            for chapter in tab_chapters:
                # serialize each chapter and append it to the 'chapters' key in the serialized tab
                serialized_chapter = ChapterSerializer(chapter).data
                serialized_tab["chapters"].append(serialized_chapter)

                # get each lesson in the chapter
                serialized_chapter["lessons"] = []
                chapter_lessons = lessons.filter(chapter=chapter)
                for lesson in chapter_lessons:
                    # serialize each lesson and append it to the 'lessons' key in the serialized chapter
                    serialized_lesson = LessonSerializer(lesson).data
                    student_lesson = student_lessons.get(lesson=lesson)
                    serialized_lesson["status"] = student_lesson.status
                    serialized_lesson["num_repetitions"] = student_lesson.num_repetitions
                    serialized_chapter["lessons"].append(serialized_lesson)


        return Response(data, status=status.HTTP_200_OK)
    
    
    @action(detail=True, methods=['get'])
    def get_parent_children(self, request, *args, **kwargs):
        """
        This function is a view for the API endpoint that lists all children associated with a parent.
        :param request: The HTTP request object (GET).
        :type request: HttpRequest
        :return: A list JSON objects representing all children associated with a parent.
        :rtype: HttpResponse
        """

        parent_id = kwargs["pk"]
        if not self.parent_exists(parent_id):
            return self.custom_message_response("Parent does not exist.", status.HTTP_404_NOT_FOUND)
        
        parent = Parent.objects.get(id=parent_id)
        data = {"students":[]}
        parent_student = ParentStudent.objects.filter(parent=parent)
        students = Student.objects.filter(id__in=parent_student.values('student'))
        
        for student in students:
            # serialize each student and append it to the 'students' key in the data dictionary
            serialized_student = StudentSerializer(student).data
            data["students"].append(serialized_student)
            serialized_student["tabs"] = []

            # get all lessons, chapters, and lesson tabs associated with the student
            student_lessons = StudentLesson.objects.filter(student=student)
            lessons = Lesson.objects.filter(id__in=student_lessons.values('lesson')).order_by(Length('text'),'text')
            chapters = Chapter.objects.filter(id__in=lessons.values('chapter'))
            tabs = Tab.objects.filter(id__in=chapters.values('tab'))


            for tab in tabs:
                # append each lesson tab to the 'tabs' key in the serialized student
                serialized_tab = TabSerializer(tab).data
                serialized_student["tabs"].append(serialized_tab)

                # get each chapter in the lesson tab
                serialized_tab["chapters"] = []
                tab_chapters = chapters.filter(tab=tab)
                for chapter in tab_chapters:
                # serialize each chapter and append it to the 'chapters' key in the serialized tab
                    serialized_chapter = ChapterSerializer(chapter).data
                    serialized_tab["chapters"].append(serialized_chapter)

                    # get each lesson in the chapter
                    serialized_chapter["lessons"] = []
                    chapter_lessons = lessons.filter(chapter=chapter)
                    for lesson in chapter_lessons:
                        # serialize each lesson and append it to the 'lessons' key in the serialized chapter
                        serialized_lesson = LessonSerializer(lesson).data
                        student_lesson = student_lessons.get(lesson=lesson)
                        serialized_lesson["status"] = student_lesson.status
                        serialized_lesson["num_repetitions"] = student_lesson.num_repetitions
                        serialized_chapter["lessons"].append(serialized_lesson)



        return Response(data, status=status.HTTP_200_OK)
    
    # GET
    # //service/lessontabs
    @swagger_auto_schema(
        tags=["Lesson Tabs"],
        operation_description="Fetches all the lessons, chapters, and lesson tabs in the database.",
        operation_summary="Fetches the lessons associated with a student, along with the chapters, and lesson tabs.",
        operation_id="get_student_lesson_tabs",
        method='GET',
        responses={
            "200": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "tabs": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Tab UUID"),
                                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Tab Name"),
                                "chapters": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            "id": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Chapter UUID"),
                                            "name": openapi.Schema(type=openapi.TYPE_STRING, description="Chapter Name"),
                                            "tab": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Tab UUID"),
                                            "lessons": openapi.Schema(
                                                type=openapi.TYPE_ARRAY,
                                                items=openapi.Schema(
                                                    type=openapi.TYPE_OBJECT,
                                                    properties={
                                                        "id": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Lesson UUID"),
                                                        "text": openapi.Schema(type=openapi.TYPE_STRING, description="Path to the file containing the textual component of the lesson. \
                                                                            File could be in text or image format."),
                                                        "audio": openapi.Schema(type=openapi.TYPE_STRING, description="Path to the file containing the audible component of the lesson."),
                                                        "has_image": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Is true if the file containing the textual component of the lesson \
                                                                                    is an image. false otherwise."),
                                                        "chapter": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="Chapter UUID"),
                                                    }
                                                )
                                            )
                                        }
                                    )
                                )
                            }
                        )
                    )
                }
            )
        }
    )
    @action(detail=True, methods=['get'])
    def get_all_lesson_tabs(self, request, pk=None):
        """
        This function is a view for the API endpoint that lists all lessons, chapters, and lesson tabs in the database.

        :param request: The HTTP request object (GET).
        :type request: HttpRequest
        :param pk: The primary key of the student to filter by.
        :type pk: int
        :return: A list JSON objects representing all lessons, chapters, and lesson tabs in the database, with a "status" field
        indicating if a lesson is assigned to the given student or not.
        :rtype: HttpResponse
        """

        # If a student ID is provided, filter lessons by that student's ID
        if pk is not None:
            student = get_object_or_404(Student, pk=pk)
            # assigned_lessons = StudentLesson.objects.filter(student=student).values_list('lesson', flat=True)
            assigned = []
            completed = []
            confirmed = []
            marked_for_redo = []
            for i in StudentLesson.objects.filter(student=student):
                if i.status == "Assigned":
                    assigned.append(i.lesson.id)
                elif i.status == "Completed":
                    completed.append(i.lesson.id)
                elif i.status == "Confirmed":
                    confirmed.append(i.lesson.id)
                elif i.status == "Marked For Redo":
                    marked_for_redo.append(i.lesson.id)
                
        
            data = {"tabs": []}
            
            # Loop through each tab, chapter, and lesson, and add a "status" field
            # indicating if the lesson is assigned to the given student or not
            for tab in Tab.objects.all():
                serialized_tab = TabSerializer(tab).data
                data["tabs"].append(serialized_tab)
                serialized_tab["chapters"] = []
                tab_chapters = Chapter.objects.filter(tab=tab)
                for chapter in tab_chapters:
                    serialized_chapter = ChapterSerializer(chapter).data
                    serialized_tab["chapters"].append(serialized_chapter)
                    serialized_chapter["lessons"] = []

                    lessons = Lesson.objects.filter(chapter=chapter).order_by(Length('text'),'text')
                    for lesson in lessons:
                        serialized_lesson = LessonSerializer(lesson).data
                        if lesson.id in assigned:
                            serialized_lesson["status"] = "assigned"
                        elif lesson.id in completed:
                            serialized_lesson["status"] = "completed"
                        elif lesson.id in confirmed:
                            serialized_lesson["status"] = "confirmed"
                        elif lesson.id in marked_for_redo:
                            serialized_lesson["status"] = "marked_for_redo"
                        else:
                            serialized_lesson["status"] = "unassigned"

                        serialized_chapter["lessons"].append(serialized_lesson)

            return Response(data, status=status.HTTP_200_OK)

        # If no student ID is provided, return all lessons
        else:
            data = {"tabs": []}
            for tab in Tab.objects.all():
                serialized_tab = TabSerializer(tab).data
                data["tabs"].append(serialized_tab)
                serialized_tab["chapters"] = []
                tab_chapters = Chapter.objects.filter(tab=tab)
                for chapter in tab_chapters:
                    serialized_chapter = ChapterSerializer(chapter).data
                    serialized_tab["chapters"].append(serialized_chapter)
                    serialized_chapter["lessons"] = LessonSerializer(Lesson.objects.filter(chapter=chapter).order_by(Length('text'),'text'), many=True).data

            return Response(data, status=status.HTTP_200_OK)
    

    @action(detail=True, methods=['post'])
    def create_lesson_tab(self, request, *args, **kwargs):
        """
        This function is a view for the API endpoint that creates a new lesson tab.

        :param request: The HTTP request object (POST).
        :type request: HttpRequest
        :return: A JSON object representing the newly created lesson tab.
        :rtype: HttpResponse
        """

        zip_file = request.FILES['file']
        tab_name = pathlib.Path(zip_file.name).stem
        tab_directory = pathlib.Path(MEDIA_ROOT) / tab_name

        # True if a new tab folder was created
        new_tab = False
        # Represents directories that were newly created, and directories that previously existed
        added_directories = []
        existing_directories = []
        # Represents lesson files that were newly created
        added_files = []

        # Temporary directory to which lessons will be moved in case something goes wrong
        temp_dir = "temp/"

        try:
            with transaction.atomic():
                # Create a new tab if it doesn't already exist
                if not os.path.exists(tab_directory):
                    os.makedirs(tab_directory)
                    new_tab = True
                    tab = Tab.objects.create(name=tab_name)
                else:
                    tab = Tab.objects.get(name=tab_name)
                
                data = TabSerializer(tab).data
                data["chapters"] = []
                # Extract the zip file containing the chapters
                with zipfile.ZipFile(zip_file, mode="r") as archive:
                    files_in_archive = archive.namelist()
                    directory = ""
                    i = 0
                    while i < len(files_in_archive):
                        if files_in_archive[i][-1] == "/":
                            # If directory
                            chapter_directory = tab_directory / files_in_archive[i]
                            chapter_name = chapter_directory.stem
                            if not os.path.exists(chapter_directory):  
                                os.makedirs(chapter_directory)
                                added_directories.append(chapter_directory)
                                chapter = Chapter.objects.create(name=chapter_name, tab=tab)
                            else:
                                existing_directories.append(chapter_directory)
                                os.makedirs(chapter_directory / temp_dir)
                                chapter = Chapter.objects.get(name=chapter_name, tab=tab)
                            chapter_serializer = ChapterSerializer(chapter).data
                            chapter_serializer["lessons"] = []
                            data["chapters"].append(chapter_serializer)
                            i += 1
                        else:
                            # If lesson files
                            lesson_files = files_in_archive[i:i+2]
                            if lesson_files[0][-1] == "/" or lesson_files[1][-1] == "/":
                                raise Exception
                            if not (lesson_files[0].endswith(".mp3") and not lesson_files[1].endswith(".mp3")) or \
                                        (not lesson_files[0].endswith("mp3") and lesson_files[1].endswith(".mp3")):
                                raise Exception
                            # I pass in tab_directory here because the chapter directory is included in the file names for some reason
                            self.create_new_lessons(archive, lesson_files, chapter, tab_directory, chapter_serializer, chapter_directory / temp_dir)
                            for lesson_file in lesson_files:
                                added_files.append(lesson_file)
                            i += 2
                for directory in existing_directories:
                    shutil.rmtree(directory / temp_dir)
                return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            if new_tab:
                shutil.rmtree(tab_directory)
            else:
                for lesson_file in added_files:
                    os.remove(tab_directory / lesson_file)
                for directory in added_directories:
                    os.rmdir(tab_directory / directory)
                for directory in existing_directories:
                    files = os.listdir(directory / temp_dir)
                    for file in files:
                        shutil.move(directory / temp_dir / file, directory)
                    os.rmdir(directory / temp_dir)
                    
            return self.custom_message_response("Please make sure the .zip file is in the format specified.", status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def create_chapter(self, request, *arg, **kwargs):
        """
        This function is a view for the API endpoint that creates a new chapter.

        :param request: The HTTP request object (POST).
        :type request: HttpRequest
        :return: A JSON object representing the newly created chapter.
        :rtype: HttpResponse
        """

        tab_id = kwargs["id"]
        tab = Tab.objects.get(id=tab_id)

        zip_file = request.FILES['file']
        chapter_name = pathlib.Path(zip_file.name).stem
        chapter_directory = pathlib.Path(MEDIA_ROOT) / tab.name / chapter_name

        # True if a new chapter folder was created
        new_chapter = False
        # Represents lesson files that were newly created
        added_files = []
        
        temp_dir = "temp/"


        try:
            with transaction.atomic():
                # Create a new chapter if it doesn't already exist
                if not os.path.exists(chapter_directory):
                    os.makedirs(chapter_directory)
                    new_chapter = True
                    chapter = Chapter.objects.create(name=chapter_name, tab=tab)
                else:
                    chapter = Chapter.objects.get(name=chapter_name, tab=tab)
                    os.makedirs(chapter_directory / temp_dir)
                
                data = ChapterSerializer(chapter).data
                # Extract the zip file containing the lessons
                with zipfile.ZipFile(zip_file, mode='r') as archive:
                    files_in_archive = archive.namelist()
                    if len(files_in_archive) % 2 == 1:
                        raise Exception
                    data["lessons"] = []
                    i = 0
                    while i < len(files_in_archive):
                        lesson_files = files_in_archive[i:i+2]
                        if lesson_files[0][-1] == "/" or lesson_files[1][-1] == "/":
                            raise Exception
                        if not (lesson_files[0].endswith(".mp3") and not lesson_files[1].endswith(".mp3")) or \
                                    (not lesson_files[0].endswith(".mp3") and lesson_files[1].endswith(".mp3")):
                            raise Exception
                        self.create_new_lessons(archive, lesson_files, chapter, chapter_directory, data, chapter_directory / temp_dir)
                        for lesson_file in lesson_files:
                            added_files.append(lesson_file)
                        i += 2
                    if not new_chapter:
                        shutil.rmtree(chapter_directory / temp_dir)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            if new_chapter:
                shutil.rmtree(chapter_directory)
            else:
                for lesson_file in added_files:
                    os.remove(chapter_directory / lesson_file)
                files = os.listdir(chapter_directory / temp_dir)
                for file in files:
                    shutil.move(chapter_directory / temp_dir / file, chapter_directory)
                os.rmdir(chapter_directory / temp_dir)
                    
            return self.custom_message_response("Please make sure the .zip file is in the format specified.", status.HTTP_400_BAD_REQUEST)



    
    def create_new_lessons(self, archive, filenames, chapter, directory, chapter_serializer, temp_dir):
        """
        This function creates new lessons from the files in the zip file.

        :param archive: The zip file containing the lesson files.
        :type archive: ZipFile
        :param filenames: The names of the files in the zip file.
        :type filenames: list
        :param chapter: The chapter that the lessons belong to.
        :type chapter: Chapter
        :param directory: The directory that the lessons will be saved to.
        :type directory: Path
        :param chapter_serializer: The chapter serializer that will be returned to the user.
        :type chapter_serializer: ChapterSerializer
        :param temp_dir: The directory that the lessons will be temporarily saved to.
        :type temp_dir: Path
        """
            
        ## Filenames contains the chapter name as part of the name of each file. See zipfile.namelist() documentation.
        if filenames[0].endswith(".mp3"):
            audio_file_name, text_file_name = filenames
        else:
            text_file_name, audio_file_name = filenames
        
        if text_file_name.endswith(".txt"):
            has_image = False
        else:
            has_image = True
        
        lesson_exists = False
        text_file_path = pathlib.Path(directory) / text_file_name
        audio_file_path = pathlib.Path(directory) / audio_file_name
        if os.path.exists(text_file_path):
            shutil.move(text_file_path, temp_dir)
            lesson_exists = True
        if os.path.exists(audio_file_path):
            shutil.move(audio_file_path, temp_dir)
            lesson_exists = True

        text_file = default_storage.save(text_file_path, ContentFile(archive.read(text_file_name)))
        audio_file = default_storage.save(audio_file_path, ContentFile(archive.read(audio_file_name)))
        
        if not lesson_exists:
            lesson = Lesson.objects.create(text=text_file, audio=audio_file, has_image=has_image, chapter=chapter)
        else:
            lesson = Lesson.objects.get(text=text_file, audio=audio_file, has_image=has_image, chapter=chapter)
        
        chapter_serializer["lessons"].append(LessonSerializer(lesson).data)


                

@api_view(['GET'])
def unfinished_list(request, *args, **kwargs):
    """
    Returns a list of lessons that have not been completed by the student.

    :param request: The request object (GET).
    :type request: Request
    :return: A list of lessons that have not been completed by the student.
    :rtype: Response
    """

    query = StudentLesson.objects.filter(
        Q(student__pk=kwargs['pk']) & 
        (Q(status="Assigned") | Q(status="Marked For Redo"))
    )
    serializers = StudentLessonSerializer(query, many=True).data
    return Response(serializers, status=status.HTTP_200_OK)

@api_view(['GET'])
def finished_list(request, *args, **kwargs):
    """
    Returns a list of lessons that have been completed by the student.

    :param request: The request object (GET).
    :type request: Request
    :return: A list of lessons that have been completed by the student.
    :rtype: Response
    """

    query = StudentLesson.objects.filter(
        Q(student__pk=kwargs['pk']) & 
        (Q(status="Completed") | Q(status="Confirmed"))
    )
    serializers = StudentLessonSerializer(query, many=True).data
    return Response(serializers, status=status.HTTP_200_OK)

@api_view(['POST'])
def parent_student(request, *args, **kwargs):
    """
    Creates a new parent-student relationship.

    :param request: The request object (POST).
    :type request: Request
    :return: The newly created parent-student relationship.
    :rtype: Response

    """
    serializer = ParentStudentSerializer(data=request.data)
    if serializer.is_valid() and request.method == 'POST':
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def parent_student_list(request, *args, **kwargs):
    """
    Returns a list of parent-student relationships.

    :param request: The request object (GET).
    :type request: Request
    :return: A list of parent-student relationships.
    :rtype: Response
    """

    queryset = ParentStudent.objects.filter(parent__id=kwargs["parent_id"])
    serializer = ParentStudentSerializer(queryset, many=True).data
    return Response(serializer,  status=status.HTTP_200_OK)

@api_view(['GET','POST', 'DELETE', 'PUT'])
def student_lesson(request, *args, **kwargs):
    """
    Returns a list of student-lesson relationships.

    :param request: The request object (GET, POST, DELETE, or PUT).
    :type request: Request
    :return: A list of student-lesson relationships.
    :rtype: Response
    """

    serializer = StudentLessonSerializer(data=request.data)
    if request.method == 'GET':
        queryset = StudentLesson.objects.filter(lesson=Lesson.objects.get(id=kwargs["lesson_id"]), student=User.objects.filter(id=kwargs["student_id"]).first())
        serializer = StudentLessonSerializer(queryset, many=True).data
        return Response(serializer,  status=status.HTTP_200_OK)
    if serializer.is_valid() and request.method == 'POST':
        serializer.save(lesson=Lesson.objects.get(id=kwargs["lesson_id"]), student=User.objects.filter(id=kwargs["student_id"]).first())
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if serializer.is_valid() and request.method == 'PUT':
        StudentLesson.objects.filter(lesson=Lesson.objects.get(id=kwargs["lesson_id"]), student=User.objects.filter(id=kwargs["student_id"]).first()).update(status=request.data["status"])
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    elif request.method == 'DELETE':
        StudentLesson.objects.filter(lesson=Lesson.objects.get(id=kwargs["lesson_id"]), student=User.objects.filter(id=kwargs["student_id"]).first()).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def assign_chapter(request, chapter_id, student_id):
    """
    Assigns a chapter to a student.

    :param request: The request object (GET or POST).
    :type request: Request
    :return: A list of student-lesson relationships.
    :rtype: Response
    """

    if request.method == 'GET':
        queryset = StudentLesson.objects.filter(lesson__chapter__id=chapter_id, student=User.objects.filter(id=student_id).first())
        serializer = StudentLessonSerializer(queryset, many=True).data
        return Response(serializer,  status=status.HTTP_200_OK)
    if request.method == 'POST':
        lessons = Lesson.objects.filter(chapter__id=chapter_id)
        student = User.objects.filter(id=student_id).first()
        student_lessons = []
        
        for lesson in lessons:
            student_lesson = {
                "lesson": lesson,
                "student": student,
                "status": "Assigned",
                "num_repetitions": request.data.get("num_repetitions", 1) 
            }
            if StudentLesson.objects.filter(lesson=lesson, student=student).exists():
                StudentLesson.objects.filter(lesson=lesson, student=student).update(status=request.data.get("status"), num_repetitions=request.data.get("num_repetitions"))

            else:
                StudentLesson.objects.create(**student_lesson)
            
        serializer = StudentLessonSerializer(data=student_lessons, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    