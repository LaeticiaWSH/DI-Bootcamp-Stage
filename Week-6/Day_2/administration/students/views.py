from django.shortcuts import render
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
def student_list(request):
     if request.method == "GET":
         date_joined_param = request.GET.get('date_joined')  # Get the value of the 'date_joined' query parameter
         queryset = Student.objects.all()

         if date_joined_param:
             queryset = queryset.filter(date_joined=date_joined_param)
         
         serializer = StudentSerializer(queryset, many=True)
         return JsonResponse(data=serializer.data, safe=False)
     
     if request.method == "POST":
        student_data = JSONParser().parse(request)
        serializer = StudentSerializer(data = student_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 'successful'}) # successfully created
        return JsonResponse({'status': 'Retry'})
     
@csrf_exempt
def student_detail(request,pk):
   try:
        detail = Student.objects.get(pk=pk)
   except Student.DoesNotExist:
        return HttpResponse(status=404) # Not found

   if request.method == 'GET':
       serializer = StudentSerializer(detail)
       return JsonResponse(data=serializer.data)
   elif request.method == 'PUT':
        new_article = JSONParser(request)
        serializer = StudentSerializer(detail, data=new_article)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)
   elif request.method == 'DELETE':
      detail.delete()
      return HttpResponse(status=204) 
