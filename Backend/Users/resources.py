from import_export import resources
from .models import District

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District