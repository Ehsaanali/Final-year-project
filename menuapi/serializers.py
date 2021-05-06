from rest_framework import serializers
from .models import Division
class DivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Division
        fields =('div_name','Total_Cases','Treatement_Completed','Treatement_Incompleted','No_of_Death')
