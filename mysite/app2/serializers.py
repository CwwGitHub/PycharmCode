from rest_framework import serializers
from app2.models import Defect

class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Defect
        fields=('bug_no','bug_name','bug_desc','bug_state')
