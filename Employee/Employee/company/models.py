from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,default=" ")

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,default=" ")

    def __str__(self):
        return self.name


class employee(models.Model):
    First_name=models.CharField(max_length=100,default=" ")
    Last_name=models.CharField(max_length=100,default=" ")
    Age=models.IntegerField(max_length=100,default="")
    Email=models.CharField(max_length=100,default=" ")
    Dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    Salary=models.IntegerField(max_length=100,default="")
    Bonus=models.IntegerField(max_length=100,default="")
    Roles=models.ForeignKey(Role,on_delete=models.CASCADE)
    Branch=models.CharField(max_length=100,default=" ")
    Hire_Date=models.DateField()
    Phone=models.IntegerField(max_length=100,default="")

    def __str__(self):
        return "%s %s" %(self.First_name,self.Last_name)




