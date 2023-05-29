from django.contrib import admin

from apps.admin_panel_app.models import Contacts, FAQ, Team, Topic, News, Person

admin.site.register(Topic)
admin.site.register(FAQ)
admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Contacts)
admin.site.register(News)
