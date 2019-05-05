from django.shortcuts import render
from .models import Tag, Content
# Create your views here.

def home(request):
     return render(request, 'home.html')
     
#def share_list(request):
     #share_list=Content.objects.prefetch_related('tag_set').select_related('author_profile').all()
      
     #return render(request, 'share/share_list.html',{'share_list':share_list,})   
     