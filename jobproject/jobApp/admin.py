from django.contrib import admin
from jobApp.models import hydjobs,bangjobs,chennaijobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


class bangjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(bangjobs,bangjobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
