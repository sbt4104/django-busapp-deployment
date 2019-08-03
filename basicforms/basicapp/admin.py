from django.contrib import admin

from basicapp.models import User
from basicapp.models import Bar
from basicapp.models import ML_data
from basicapp.models import Notifi
# Register your models here.

admin.site.register(User)

admin.site.register(Bar)

admin.site.register(ML_data)

admin.site.register(Notifi)
