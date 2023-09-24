from django.shortcuts import render,redirect
from . models import employee,Department,Role

# Create your views here.
def home(request):
    return render(request,'home.html')

def viewsAllEmployee(request):
    mydata=employee.objects.all()
    if(mydata!=" "):
        return render(request,'views.html',{'datas':mydata})
    else:
        return render(request,'views.html')

def addEmployee(request):
    departD=Department.objects.all()
    rolesD=Role.objects.all()

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        age=request.POST['age']
        email=request.POST['email']
        #Foregin key
        department=request.POST.get('department')
        department1=Department.objects.get(id=department)
       #Foregin key
        roles =request.POST.get('roles')
        roles1=Role.objects.get(id=roles)
        
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        branch=request.POST['branch']
        hire_date=request.POST['hire_date']
        phone=request.POST['phone']

        obj=employee()
        obj.First_name=first_name
        obj.Last_name=last_name
        obj.Age=age
        obj.Email=email
        obj.Dept=department1
        obj.Salary=salary
        obj.Bonus=bonus
        obj.Roles=roles1
        obj.Branch=branch
        obj.Hire_Date=hire_date
        obj.Phone=phone
        obj.save()
        return redirect('home')
    return render(request,'add.html',{'departData':departD,'roleData':rolesD})

def updateEmployee(request):
    mydata=employee.objects.all()
    if(mydata!=" "):
        return render(request,'update.html',{'datas':mydata})
    else:
        return render(request,'update.html')
    
def updateEmployeeDetails(request,id):
    data_1=employee.objects.get(id=id)
    departD=Department.objects.all()
    rolesD=Role.objects.all()

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        age=request.POST['age']
        email=request.POST['email']
        #Foregin key
        department=request.POST.get('department')
        department1=Department.objects.get(id=department)
        #Foregin key
        roles =request.POST.get('roles')
        roles1=Role.objects.get(id=roles)
        
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        branch=request.POST['branch']
        hire_date=request.POST['hire_date']
        phone=request.POST['phone']

        data_1.First_name=first_name
        data_1.Last_name=last_name
        data_1.Age=age
        data_1.Email=email
        data_1.Dept=department1
        data_1.Salary=salary
        data_1.Bonus=bonus
        data_1.Roles=roles1
        data_1.Branch=branch
        data_1.Hire_Date=hire_date
        data_1.Phone=phone
        data_1.save()
        return redirect('updateEmployee')  

    return render(request,'update1.html',{'dataValue':data_1,'departData':departD,'roleData':rolesD})
def DeleteEmployee(request):
    DataValue=employee.objects.all()
    if(DataValue!=" "):
        return render(request,'delete.html',{'datas': DataValue})
    else:
        return render(request,'delete.html')
    
def DeleteEmployeeDetails(request,id):
    deleteValue=employee.objects.get(id=id)
    deleteValue.delete()
    return redirect('home')
    


    
    




