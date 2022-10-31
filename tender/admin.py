from django.contrib import admin
from tender.models.company_model import Company
from tender.models.project_model import Project
from tender.models.registrant_model import Registrant
from tender.models.image_model import Image

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Registrant)
admin.site.register(Image)