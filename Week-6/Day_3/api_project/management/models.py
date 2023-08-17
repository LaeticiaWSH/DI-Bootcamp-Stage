from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 100,blank=False)
    description = models.TextField(blank=False)
    employee = models.ManyToManyField('Employee',related_name = 'employee_department',blank=True)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length = 100,blank=False)
    email = models.EmailField(max_length = 120)
    phone_number = models.CharField(max_length = 14)
    department = models.ForeignKey(Department,on_delete = models.CASCADE, related_name='+')
    emp_projects = models.ManyToManyField('Project',related_name = 'employee_project',blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length = 100,blank=False)
    description = models.TextField(blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    task = models.ManyToManyField('Task',related_name= 'task_project',blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length = 100,blank=False)
    description = models.TextField(blank=False)
    due_date = models.DateField()
    completed = models.BooleanField()
    project = models.ForeignKey(Project,on_delete = models.CASCADE,related_name='+')

    def __str__(self):
        return self.name