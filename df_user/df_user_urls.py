from django.urls import path,re_path
from df_user import views

urlpatterns = [
    path('loginin',views.loginin),
    path('register',views.register)
]