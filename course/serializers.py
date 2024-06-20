from rest_framework import serializers
from .models import Course, Topic, Lesson, CourseApplication, FeedbackForm

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseApplication
        fields = '__all__'

class FeedbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = '__all__'
