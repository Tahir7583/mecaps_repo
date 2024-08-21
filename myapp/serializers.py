from rest_framework import serializers
from . models import Skill,applicant


class Skillserializer(serializers.ModelSerializer):
    class Meta:
        model= Skill
        fields='__all__'

class Applicantserializer(serializers.ModelSerializer):
    class Meta :
        model=applicant
        fields='__all__'

# class User_Ragister_serializer(serializers.ModelSerializer):
#     class Meta:
#         model=userRagister
#         fields='__all__'



                
