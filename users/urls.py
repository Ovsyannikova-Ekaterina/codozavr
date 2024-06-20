from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ParentViewSet, StudentViewSet, TeacherViewSet, login_view, register_view, logout_view, profile_view

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = router.urls + [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
