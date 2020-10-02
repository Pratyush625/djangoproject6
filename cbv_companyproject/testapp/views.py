from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CompanyListView(ListView):
    model=Company
    #default template file name : company_list.html
    #default context object : company_list

class CompanyDetailView(DetailView):
    model=Company
    #default template file name : company_detail.html
    #default context name : company or object

class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','ceo')
    #default template form name : company_form.html

class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo')

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')
    #default template file name : company_confirm_delete.html
