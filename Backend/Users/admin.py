from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Officer, District,Subcounty, Parish
from .forms import OfficerChangeForm, OfficerCreationForm




@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('name',)

@admin.register(Subcounty)
class SubCountyAdmin(ImportExportModelAdmin):
    list_display = ('name', 'district',)

@admin.register(Parish)
class ParishAdmin(ImportExportModelAdmin):
    list_display = ('name', 'sub_county',)

@admin.register(Officer)
class OfficerAdmin(ImportExportModelAdmin):
    add_form = OfficerCreationForm
    form = OfficerChangeForm
    list_display = ('username', 'login_id','password', 'parish')

# admin.site.register(Officer)
# admin.site.register(District, DistrictAdmin)
# admin.site.register(Parish, ParishAdmin)
# admin.site.register(Subcounty, SubCountyAdmin)

