from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, TopicViewSet, LessonViewSet, CourseApplicationViewSet, FeedbackFormViewSet, course_application_view, feedback_view

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'applications', CourseApplicationViewSet)
router.register(r'feedback', FeedbackFormViewSet)

urlpatterns = [
    path('course-application/', course_application_view, name='course_application'),
    path('feedback/', feedback_view, name='feedback'),  # Маршрут для формы обратной связи
]

urlpatterns += router.urls
