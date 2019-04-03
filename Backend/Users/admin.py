from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Officer, District,Subcounty, Parish
# Register your models here.
# class DistrictAdmin(admin.ModelAdmin):
#     model=District
#     list_display = ('name',)

# class SubCountyAdmin(admin.ModelAdmin):
#     model=Subcounty
#     list_display = ('name', 'district')
# class ParishAdmin(admin.ModelAdmin):
#     model=Parish
    




@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('name',)

@admin.register(Subcounty)
class SubCountyAdmin(ImportExportModelAdmin):
    list_display = ('name', 'district',)

@admin.register(Parish)
class ParishAdmin(ImportExportModelAdmin):
    list_display = ('name', 'sub_county',)



# admin.site.register(Officer)
# admin.site.register(District, DistrictAdmin)
# admin.site.register(Parish, ParishAdmin)
# admin.site.register(Subcounty, SubCountyAdmin)