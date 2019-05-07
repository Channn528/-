from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='share'
urlpatterns = [
     path('',views.home, name='home'),
     path('<int:id>/', views.board, name='board'),
     path('add/', views.add, name='add'),
     path('delete/<int:id>/', views.delete, name="delete"),
     path('edit/<int:id>/', views.edit, name="edit"),
     path('search/', views.search, name="search"),
     path('<int:id>/comment/',views.comment, name="comment"),
     path('update/<int:id>',views.update,name="update"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)