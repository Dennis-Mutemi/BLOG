from django.urls import path,re_path
from .import views
app_name='article'
urlpatterns = [    
    path('',views.indexx,name="home"),
     path('create',views.create,name="create_post"),
     path('<slug:me>',views.article_details,name='details'),

]
