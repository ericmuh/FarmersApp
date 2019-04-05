
import sys
import os
sys.path.append('/home/eric/projects/Django/Django_Projects/farmersapp')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Backend.settings")
from django.conf import settings
from Backend import settings
from Users.models import District, Subcounty, Parish

# import django.db
import csv
def uploadCSV():
    f = open("parish.csv")
    reader = csv.reader(f)
    for district_name,  parish_name, sub_county_name, in reader:
        district,  created = District.objects.get_or_create(name=district_name)
        subcounty, created = Subcounty.objects.get_or_create(name=sub_county_name, district=district)
        # district.subcounty_set.create(name=subcounty)
        # parish= Parish.objects.get_or_create(name=parish_name, sub_county=subcounty)
        subcounty.parish_set.create(name=parish_name)
        # parish = Parish(name=parish_name,  sub_county=subcounty
        # )

        # #-------ONE-------
        # district = District(name=district_name)
        # sub_county = Subcounty(name=sub_county_name,  district=district
        # )
        # # district.subcounty_set.create(name=sub_county_name)

        # parish = Parish(name=parish_name,  sub_county=sub_county
        # )
        # # sub_county.parish_set.create(name=parish_name)
        # district.save()
        # subcounty.save()
        # parish.save()
        print(f'added {district_name} , {sub_county_name}', {parish_name})
    return "Hooray"


uploadCSV()