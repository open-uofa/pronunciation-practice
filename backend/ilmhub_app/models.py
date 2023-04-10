from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid
from IlmHub.settings import MEDIA_URL

fs = FileSystemStorage(location=MEDIA_URL)


class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth instead of usernames.

    :param BaseUserManager: The default django user manager.
    """

    def validate_data(self, username, password, first_name, last_name):
        # Makes sure none of the parameters are empty
        if not username:
            raise ValueError("Users must have a username!")
        if not password:
            raise ValueError("Users must have a password!")
        if not first_name:
            raise ValueError("Users must have a first name!")
        if not last_name:
            raise ValueError("Users must have a last name!")

    # https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
    def create_user(self, username, password, first_name, last_name, role):
        """
        Creates and saves a User with the given username, password, first and last names,
        and a role.

        :param username: The username of the user.
        :param password: The password of the user.
        :param first_name: The first name of the user.
        :param last_name: The last name of the user.
        :param role: The role of the user.

        :return: The newly-created default user.
        """

        self.validate_data(username, first_name, last_name, role)
        roles = tuple(choice[0] for choice in User.RoleChoices.choices)

        user = self.model(
            username=username, first_name=first_name, last_name=last_name, role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password, first_name, last_name):
        """
        Creates and saves a staff user with the given username, password, first and last names,
        and the default role of "Content Creator".

        :param username: The username of the user.
        :param password: The password of the user.
        :param first_name: The first name of the user.
        :param last_name: The last name of the user.

        :return: The newly-created staff user.
        """
        self.validate_data(username, password, first_name, last_name)
        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=User.RoleChoices.CONTENT_CREATOR,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, first_name, last_name):
        """
        Creates and saves a superuser with the given username, password, first and last names,
        and the default role of "Content Creator".

        :param username: The username of the user.
        :param password: The password of the user.
        :param first_name: The first name of the user.
        :param last_name: The last name of the user.

        :return: The newly-created superuser (content-creator).
        """
        self.validate_data(username, password, first_name, last_name)
        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=User.RoleChoices.CONTENT_CREATOR,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    A custom user model to replace the default django user model.

    :param AbstractBaseUser: The default django user model.
    """

    # https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/

    objects = UserManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=32)
    password = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    class RoleChoices(models.TextChoices):
        """
        The choices for the role of a user.

        :param models.TextChoices: The default django text choices.
        """
        STUDENT = "Student"
        PARENT = "Parent"
        TEACHER = "Teacher"
        CONTENT_CREATOR = "Content Creator"

    first_name = models.TextField(verbose_name="First Name", null=False, blank=False)
    last_name = models.TextField(verbose_name="Last Name", null=False, blank=False)
    role = models.TextField(choices=RoleChoices.choices, null=True, blank=True)

    ### Other required fields, such as address, date of birth, etc.

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]  # Required fields for superuser

    def get_full_name(self):
        # The user is identified by their username
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


class GetParents(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=User.RoleChoices.PARENT)


class Parent(User):
    """
    A proxy model for the User model, to allow for filtering of users by role.

    :param User: The User model.
    """
    class Meta:
        proxy = True
        verbose_name_plural = "Parents"

    objects = GetParents()

    def save(self, *args, **kwargs):
        self.role = User.RoleChoices.PARENT
        return super().save(*args, **kwargs)


class GetStudents(models.Manager):
    """
    A manager for the Student model, to allow for filtering of users by the 'student' role.

    :param models.Manager: The default django manager.
    """

    def get_queryset(self):
        return super().get_queryset().filter(role=User.RoleChoices.STUDENT)


class Student(User):
    """
    A proxy model for the User model, to allow for filtering of users by role.

    :param User: The User model.
    """

    class Meta:
        proxy = True
        verbose_name_plural = "Students"

    objects = GetStudents()

    def save(self, *args, **kwargs):
        self.role = User.RoleChoices.STUDENT
        return super().save(*args, **kwargs)


class GetTeachers(models.Manager):
    """
    A manager for the Teacher model, to allow for filtering of users by the 'teacher' role.

    :param models.Manager: The default django manager.
    """
        
    def get_queryset(self):
        return super().get_queryset().filter(role=User.RoleChoices.TEACHER)


class Teacher(User):
    """
    A proxy model for the User model, to allow for filtering of users by role.

    :param User: The User model.
    """

    class Meta:
        proxy = True
        verbose_name_plural = "Teachers"

    objects = GetTeachers()

    def save(self, *args, **kwargs):
        self.role = User.RoleChoices.TEACHER
        return super().save(*args, **kwargs)


class GetContentCreators(models.Manager):
    """
    A manager for the content creator model, to allow for filtering of users by the 'content creator' role.

    :param models.Manager: The default django manager.
    """

    def get_queryset(self):
        return super().get_queryset().filter(role=User.RoleChoices.CONTENT_CREATOR)


class ContentCreator(User):
    """
    A proxy model for the User model, to allow for filtering of users by role.

    :param User: The User model.
    """

    class Meta:
        proxy = True
        verbose_name_plural = "Content Creators"

    objects = GetContentCreators()

    def save(self, *args, **kwargs):
        self.role = User.RoleChoices.CONTENT_CREATOR
        return super().save(*args, **kwargs)


class Tab(models.Model):
    """
    A model for the lesson tabs in the app, which contain the chapters and lessons.

    :param models.Model: The default django model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    """
    A model for the chapters in the app, which contain the lessons.

    :param models.Model: The default django model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, blank=False)
    tab = models.ForeignKey(Tab, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    A model for the lessons in the app, which contain the lesson text/image, audio, and chapter that it belongs to.

    :param models.Model: The default django model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.FileField(null=False, blank=False, storage=fs)
    audio = models.FileField(
        null=False, blank=False, storage=fs
    )  # relative path to the audio file associated with the lesson
    has_image = models.BooleanField(
        default=False
    )  # if true, the "text" field represents the
    # relative path to the image file associated
    # with the lesson
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)


class ParentStudent(models.Model):
    """
    A model for the parent-student relationship in the app, which contains the student and parent that it belongs to.

    :param models.Model: The default django model.
    """

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("parent", "student"), name="Unique Parent-Student Combination"
            ),
        ]
        verbose_name = "Parent-Student"
        verbose_name_plural = "Parent-Students"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(
        Parent, on_delete=models.CASCADE, related_name="Users_Parent"
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="Users_Student"
    )


class StudentLesson(models.Model):
    """
    A model for the student-lesson relationship in the app, which allows for a student to be assigned a particular lesson.

    :param models.Model: The default django model.
    """
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("student", "lesson"), name="Unique Student-Lesson Combination"
            ),
        ]
        verbose_name = "Student-Lesson"
        verbose_name_plural = "Student-Lessons"

    class StatusChoices(models.TextChoices):
        ASSIGNED = "Assigned"
        COMPLETED = "Completed"
        CONFIRMED = "Confirmed"
        MARKED_FOR_REDO = "Marked For Redo"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    num_repetitions = models.IntegerField(default=1)
    status = models.TextField(
        choices=StatusChoices.choices, default=StatusChoices.ASSIGNED
    )
