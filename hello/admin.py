from django.contrib import admin
from .models import User
from  .models import Nationalities
from  .models import Profile

# Register your models here.


#admin.site.register(User)
admin.site.register(Nationalities)
admin.site.register(Profile)