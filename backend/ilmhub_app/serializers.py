from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    """
    A Custom login serializer to allow for users with different roles to login correctly on the frontend.

    :param TokenObtainPairSerializer: The default django rest framework simplejwt login serializer.
    """
 
    def validate(self, attrs):
        # validate that the provided credentials are of a valid type
        data =  super().validate(attrs)
         
        data['username'] = self.user.username
        data['password'] = self.user.password
        data['id'] = self.user.id
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['role'] = self.user.role
 
        return data

class AuthorRegisterSerializer(serializers.ModelSerializer):
    """
    A Custom register serializer to allow for users with different roles to register correctly on the frontend.

    :param serializers.ModelSerializer: The default django rest framework model serializer.
    """
    
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name','last_name', 'role')
         
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name', 'role']
        
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id','username','first_name','last_name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','username','first_name','last_name']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','username','first_name','last_name']

class ContentCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCreator
        fields = ['id','username','first_name','last_name']
class UserCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name', 'role']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'id',
            'name',
            'tab'
        ]

class LessonSerializer(serializers.ModelSerializer):
    #chapter=ChapterSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = [
            'id',
            'text',
            'audio',
            'has_image',
            'chapter'
        ]

class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = [
            'id',
            'name'
        ]

class StudentLessonSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    lesson = LessonSerializer(read_only=True)
    class Meta:
        model = StudentLesson
        fields = '__all__'


class ParentStudentSerializer(serializers.ModelSerializer):
    parent = ParentSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = ParentStudent
        fields = '__all__'
    