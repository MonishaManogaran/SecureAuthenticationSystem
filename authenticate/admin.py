from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    list_display=('email', 'firstname', 'lastname', 'phonenumber', 'is_staff')
    list_filter=('is_staff', 'is_superuser', 'is_active')
    search_fields=('email',)
    ordering=('email',)

    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Personal Information',{'fields':('firstname','lastname','phonenumber')}),
        ('Permissions',{'fields':('is_active','is_superuser','is_staff','groups','user_permission')})

    )

    add_fieldsets=(
        (None,{
            'class':'wide',
            'fields':('email','firstname','lastname','password1','password2','phonenumber','is_staff','is_active')
        }),
    )



admin.site.register(CustomUser, CustomUserAdmin)

    