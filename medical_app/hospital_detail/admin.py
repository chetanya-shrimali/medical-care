from django.contrib import admin

from hospital_detail.models import Detail, Doctor, Tag, Review

admin.site.register(Detail)
admin.site.register(Doctor)
admin.site.register(Tag)
admin.site.register(Review)
