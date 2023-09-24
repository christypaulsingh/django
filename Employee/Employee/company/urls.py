from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('viewsAllEmployee',views.viewsAllEmployee,name='viewsAllEmployee'),
    path('addEmployee',views.addEmployee,name='addEmployee'),
    path('updateEmployee',views.updateEmployee,name='updateEmployee'),
    path('updateEmployeeDetails/<int:id>',views.updateEmployeeDetails,name='updateEmployeeDetails'),
    path('DeleteEmployee',views.DeleteEmployee,name='DeleteEmployee'),
    path('DeleteEmployeeDetails/<int:id>',views.DeleteEmployeeDetails,name='DeleteEmployeeDetails'),



]