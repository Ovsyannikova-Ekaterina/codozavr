from django.db import models
from users.models import Parent, Teacher

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in hours")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    material_links = models.TextField()
    materials = models.FileField(upload_to='materials/')

    def __str__(self):
        return self.name

class Lesson(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    application = models.ForeignKey('CourseApplication', on_delete=models.CASCADE)

    def __str__(self):
        return f"Lesson on {self.date} from {self.start_time} to {self.end_time}"

class CourseApplication(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    parent_email = models.EmailField()
    parent_phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return f"Application by {self.parent.user.username} for {self.course.name} on {self.date}"


class FeedbackForm(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Feedback on {self.date} at {self.time}"
