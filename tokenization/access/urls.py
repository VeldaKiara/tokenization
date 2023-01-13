from django.urls import path
from django.views.generic import TemplateView
# from access import views
app_name='access'

urlpatterns=[
path('', TemplateView.as_view(template_name='home.html'), name='home'),
# path('hello/', views.HelloView.as_view(), name='hello'),

]

