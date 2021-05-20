from django.contrib import admin

# Register your models here.
from faculty.models import Faculty, Faculty_by_admin, Video, Contact

admin.site.register(Faculty)

admin.site.register(Faculty_by_admin)
admin.site.register(Video)
admin.site.register(Contact)