from django.conf.urls import url
from django.views.generic import RedirectView

from main_app import views
from django.urls.conf import path
from main_app.views import Pdf, Pdfs



urlpatterns = [
    url('^home$', views.home, name='home'),
    url('^newtemp$', views.home, name='newtemp'),
    url('^about$', views.about, name='about'),
    url('^contact$', views.contact, name='contact'),
    url('^build$',views.StudentCreateView.as_view(), name='build'),
    url('^list$',views.StudentListView.as_view(), name='student-list'),
    path('template/', views.TemplateListView.as_view()),  
    path('template/<int:pk>', views.TemplateDetailView.as_view()),
    url('^build/(?P<pk>[0-9]+)$', views.StudentDetailView.as_view(), name='student-detail'),
   # url('^template-list$',views.TemplateListView().as_view(), name='template-list'),
    url(r'^pdf/$',Pdf.as_view(),name='pdf'),
    url(r'^pdfs/$',Pdfs.as_view(),name='pdfs'),
    #url('build/(?P<pk>[0-9]+)$', views.TemplateDetailView().as_view(), name='newtemplate-detail'),
    url('',RedirectView.as_view(url='home')), 
    
]