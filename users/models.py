from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Валидатор, разрешающий использование кириллических символов и пробелов
username_validator = RegexValidator(
    regex=r'^[\w.@+-\u0400-\u04FF\s]+$',  # Добавлены символы Unicode для кириллицы и пробелы
    message='Введите корректное имя пользователя. Это значение может содержать только буквы, цифры, пробелы и символы @/./+/-/_.'
)

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Parent'),
        (2, 'Student'),
        (3, 'Teacher'),
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "Пользователь с таким именем уже существует.",
        },
    )
    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Изменен related_name
        blank=True,
        help_text=(
            'Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из их групп.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Изменен related_name
        blank=True,
        help_text='Конкретные разрешения для этого пользователя.',
        related_query_name='user',
    )

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15)
    relation_to_child = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} (Parent)"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} (Student)"

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} (Teacher)"
