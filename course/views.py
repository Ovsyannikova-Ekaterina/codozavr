import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.utils import timezone
from .models import Course, Topic, Lesson, CourseApplication, FeedbackForm
from .serializers import CourseSerializer, TopicSerializer, LessonSerializer, CourseApplicationSerializer, FeedbackFormSerializer
from users.models import Parent

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CourseApplicationViewSet(viewsets.ModelViewSet):
    queryset = CourseApplication.objects.all()
    serializer_class = CourseApplicationSerializer

class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedbackFormSerializer

@login_required
@csrf_exempt
def course_application_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        parent_email = data.get('parent_email')
        parent_phone = data.get('parent_phone')
        course_id = data.get('course_id')
        parent_id = data.get('parent_id')
        try:
            parent = Parent.objects.get(id=parent_id)
        except Parent.DoesNotExist:
            return HttpResponseBadRequest("Parent does not exist")

        CourseApplication.objects.create(
            parent_email=parent_email,
            parent_phone=parent_phone,
            course_id=course_id,
            parent=parent,
            status='Pending',
            date=timezone.now().date(),
            time=timezone.now().time()
        )
        return JsonResponse({'status': 'ok'})

    course_id = request.GET.get('course_id')
    course = get_object_or_404(Course, id=course_id)
    try:
        parent = Parent.objects.get(user=request.user)
    except Parent.DoesNotExist:
        parent = None

    return render(request, 'course_application.html', {'course': course, 'parent': parent, 'courses': Course.objects.all()})

@csrf_exempt
def feedback_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            description = data.get('description')
            if not description:
                return JsonResponse({'status': 'error', 'message': 'Description is required'}, status=400)
            feedback = FeedbackForm.objects.create(description=description)
            return JsonResponse({'status': 'ok', 'message': 'Feedback submitted successfully'})
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def home_view(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})
