To run locally, do the usual:

#. Create a Python 3.6 virtualenv Django 1.11 version installed

#. Create project projectname (Function Based View Project)
   
    django-admin startproject crudfbvproject

#. Go to the project dir 
   
    cd crudfbvproject

#. Create application inside main project directory 

    py manage.py startapp testapp

#. Configure the templatefile and staticfile inside settings.py 

#.Create template folder and static folder, inside static folder create css folder and image folder, insert the required images, Here sqlite used as default database

#. Create Employee model class with attributes

#. To convert model class to sql code use makemigrations 

    py manage.py makemigrations

#. To create table inside database 

    py manage.py migrate

#. Create superuser to connect with database 

    py manage.py createsuperuser

#. Register the model class inside admin.py file
   
    admin.site.register(model,modeladmin)

#. Create django model form

#. Define view function inside views.py 
    
    from django.shortcuts import render
    from testapp.models import Employee
    from testapp.forms import EmployeeForm
    from django.shortcuts import redirect


    def retrieve_view(request):
       emp_list=Employee.objects.all()
       my_dict={'emp_list':emp_list}
       return render(request,'testapp/index.html',context=my_dict)

    def create_view(request):
      form=EmployeeForm()
      if request.method=='POST':
          form=EmployeeForm(request.POST)
        if form.is_valid():
             form.save()
            return redirect('/')
    return render(request,'testapp/create.html',{'form':form})

     def delete_view(request,id):
       emp_list=Employee.objects.get(id=id)
       emp_list.delete()
       return redirect('/')

    def update_view(request,id):
      emp_list=Employee.objects.get(id=id)
     if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp_list)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'emp_list':emp_list})

    
#. One populate.py script has been created for generating multiple records at a time using Faker Module

#. Define view function inside urls.py
    
    from django.conf.urls import url
    from django.contrib import admin
     from testapp import views
     urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^$', views.retrieve_view),
      url(r'^create/', views.create_view),
      url(r'^delete/(?P<id>\d+)/$', views.delete_view),
      url(r'^update/(?P<id>\d+)/$', views.update_view),
    ]

#. To run server 

    py manage.py runserver
