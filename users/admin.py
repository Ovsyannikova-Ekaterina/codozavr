from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Parent, Student, Teacher

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_staff', 'is_active']
    list_filter = ['user_type', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Role info', {'fields': ('user_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class ParentAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'relation_to_child']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'parent']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'phone']

admin.site.register(Parent, ParentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
