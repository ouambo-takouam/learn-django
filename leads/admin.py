from django.contrib import admin

from .models import User, Organisation, Agent, Lead

admin.site.register(User)
admin.site.register(Organisation)
admin.site.register(Agent)
admin.site.register(Lead)
