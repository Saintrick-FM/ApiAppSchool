from django.contrib import admin
from .models import Cycle, Ecole, Site

admin.site.register(Ecole)
admin.site.register(Cycle)
admin.site.register(Site)