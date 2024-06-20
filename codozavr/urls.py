from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import profile_view
from course.views import feedback_view, home_view, course_application_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/courses/', include('course.urls')),
    path('api/feedback/', feedback_view, name='feedback'),  # Маршрут для формы обратной связи
    path('', home_view, name='index'),  # Главная страница
    path('login/', TemplateView.as_view(template_name="login.html"), name='login'),
    path('register/', TemplateView.as_view(template_name="register.html"), name='register'),
    path('courses/', TemplateView.as_view(template_name="courses.html"), name='courses'),
    path('profile/', profile_view, name='profile'),
    path('course-application/', course_application_view, name='course_application'),  # Маршрут для формы записи на курс
]
