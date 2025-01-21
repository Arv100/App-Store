from django.contrib import admin
from .models import App, CustomUser
from django.contrib import admin
from .models import App
from django import forms


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'is_active', 'is_staff']
    search_fields = ['email', 'full_name']
    list_filter = ['is_active', 'is_staff']

class AppAdminForm(forms.ModelForm):
    class Meta:
        model = App
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['created_by'].initial = self.current_user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.pk:
            instance.created_by = self.current_user
        if commit:
            instance.save()
        return instance

class AppAdmin(admin.ModelAdmin):
    form = AppAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form

admin.site.register(App, AppAdmin)

