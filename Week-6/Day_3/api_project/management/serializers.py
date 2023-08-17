from rest_framework import serializers
from .models import Department,Employee,Task,Project

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = Department
       fields = ('name', 'description', 'employee')

       model = Employee
       fields = ('name', 'email', 'phone_number','department')

       model = Task
       fields = ('name', 'description', 'due_date','completed','project')

       model = Project
       fields = ('name', 'description' , 'start_date','end_date')