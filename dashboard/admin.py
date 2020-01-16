from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User, Supervisor, Hr
from main_app.models import Rating, HRRating

admin.site.register(User, UserAdmin)
admin.site.register(Supervisor)
admin.site.register(Hr)

admin.site.register(Rating)
admin.site.register(HRRating)
