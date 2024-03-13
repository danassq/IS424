from django.urls import path
from . import views
app_name="APP1"
urlpatterns = [path("",views.list,name="list"),
               path ("add",views.add,name="add")]
