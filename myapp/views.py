from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Skillserializer,Applicantserializer
from .models import applicant,Skill



class applicant_data(APIView):   # handle http request
    def get(self,request,pk=None,format=None):  # handle get request
     obj=applicant.objects.all()   # fetch all data from database
     serializer=Applicantserializer(obj,many=True) #convert queryset to json using serializer
     return Response (serializer.data) # resturn data using respone to display
    

    def post(self,request,format=None):  # post request handle
        obj=request.data  #  get data from user request
        serializer=Applicantserializer(data=obj) # paas data into serializer to validate and save into queryset
        if serializer. is_valid(): # if valid code than save
            serializer.save()
            return Response ('new applicant add successfully')
        return Response ('enter valid data')
    
    def put(self,request,pk=None):  # handle put request 
        jsondata=request.data # get data from user 
        queryset=applicant.objects.get(id=pk) # get data using id from data base 
        serializer=Applicantserializer(data=jsondata,instance=queryset) # replace data from user and backend
        if serializer: # if serializer code valid after save
            serializer.save()
            return Response ('applicant updatet successully')
        return Response ('valid data please')
    
    def delete(self,request,pk=None):  # handle delete request
        data=applicant.objects.get(id=pk) # fetch data from data base using id
        if data : # if data exist so delete data and retun message
            data.delete()
            return Response ('delete applicant successfully')
        




class skill_data (APIView): # skilldata class inheri karega apiVews se apiview handle karta he http request 
    def get (self,request,pk=None,format=None):

        data=Skill.objects.all()
        serializer=Skillserializer(data,many=True)
        return Response (serializer.data)

    def post(self,request):
        data=request.data 
        serializer=Skillserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response ('data add successfully')
        return Response ('data invalid')
    
    def put(self,request,pk=None):
        jsondata=request.data 
        queryset=Skill.objects.get(id=pk)
        serializer=Skillserializer(data=jsondata,instance=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response ('data updated successfully')
        
        return Response ('data not a vlid')
    
    def delete(self,request,pk=None):
        data=Skill.objects.get(id=pk)
        data.delete()
        return Response ('data delete successfully')