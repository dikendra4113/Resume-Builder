from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from main_app.models import  Student, Template
  
from django.http.response import HttpResponse
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from utils import  Render
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from django.contrib.auth import get_user_model
from django.views import generic
from main_app import models
from _datetime import timezone

#class HelloPDFView(PDFTemplateView):
 #   template_name = 'main_app/student_detail.html'
class Pdf(View):

    def get(self, request):
        sales = Student.objects.all()
        #today = timezone.now()
        params = {
            #'today': today,
            'sales': sales,
            'request': request
        }
        
        return Render.render('student_detail1.html',params)
 
class Pdfs(View):

    def get(self, request):
        sales = Student.objects.all()
        #today = timezone.now()
        params = {
            #'today': today,
            'sales': sales,
            'request': request
        }
        
        return Render.render('contact.html',params)
 
def home(request):
    return render(request, 'home.html')



def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

#def contact(request):
   # return render(request, 'contact.html')


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    fields = (
        'name', 'dob', 'email_id', 'mobile_no', 'address', 'objective', 'brief_overview', 'tenth_marks', 'twe_marks',
        'gradu_agg', 'tech_certi', 'extra_curri', 'project')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super(StudentCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    model = Student
    template_name = 'main_app/student_list.html'

    def get_queryset(self):
        si = self.request.GET.get('user')
        if si == None:
            si = ''
        # username = (User.objects.filter(id=int(si))).username
        # print(username)
        return Student.objects.filter(username_id__exact=int(si))


@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    
class TemplateListView(ListView):
    model = Template
    template_name = 'main_app/template_list.html'
class TemplateDetailView(DetailView):
    model = Student
