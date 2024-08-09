from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Skillserializer
from .models import Skill 

# Create your views here.

class skill_data(APIView): # class based vews
    def get (self,request,pk=None,format=None):

        data=Skill.objects.all()
        serializer=Skillserializer(data,many=True)
        return Response (serializer.data)

    def post(self,request,format=None):
        data=request.data 
        serializer=Skillserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response ('data add successfully')
        return Response ('data invalid')
    
    def put(self,request,pk=None,format=None):
        jsondata=request.data 
        queryset=Skill.objects.get(id=pk)
        serializer=Skillserializer(data=jsondata,instance=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response ('data updated successfully')
        
        return Response ('data not a vlid')
    
    def delete(self,request,pk=None,format=None):
        data=Skill.objects.get(id=pk)
        data.delete()
        return Response ('data delete successfully')