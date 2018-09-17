from django.urls import path,re_path
from bold import views

urlpatterns = [
    path('index/', views.indexView),
    re_path(r'^content/(?P<id>[0-9]+)$',views.getContent),
    re_path(r'^editadd/(?P<id>[0-9]+)$',views.addBoke),
    path('submitContent/',views.submitBoke)
]