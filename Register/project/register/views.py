from django.shortcuts import render,redirect
from . models import Datas

# Create your views here.
def home(request):#123:8000-url
    #previous data
    mydatas=Datas.objects.all()
    if (mydatas !=" "):
        return render(request,'home.html',{'datas':mydatas}) #---previous datas display in web page
    else:
        return render(request,'home.html')


def addData(request):#123:8000/addData-url   after submit click process
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        contact=request.POST['contact']
        place=request.POST['place']
        
        #Database class object created and push to db
        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Email=email
        obj.Contact=contact
        obj.Place=place
        obj.save()
        return redirect('home')

    return render(request,'home.html')#submit before render 

def updateData(request,id): #123:8000/updateData
    #1.request id == database id
    mydata=Datas.objects.get(id=id) #particular person data storage

    #2.After update submit condition again push data to db:
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        contact=request.POST['contact']
        place=request.POST['place']

        #particular person data storage update
        mydata.Name=name
        mydata.Age=age
        mydata.Email=email
        mydata.Contact=contact
        mydata.Place=place
        mydata.save()
        return redirect('home')   
     
    #1.update.html form push pannum
    return render(request,'update.html',{'data':mydata})

def delete(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')   



