from django.shortcuts import render, redirect
#from .forms import PostForm
from .models import Content, Comment
    
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here

def home(request):
     contents = Content.objects.all()
     return render(request, 'home.html', {'contents': contents})   
     

#확대된 보드 보여줌
def board(request, id):
     content=Content.objects.get(pk=id)
     comments = Comment.objects.filter(content=content)
     
     return render(request, 'board.html',{'content': content, 'comments':comments})
     
     
# 기존 보드 및 추가보드에 쓰는거   
def add(request):
     if request.method == "POST":
          print("!!!!!!!!!!!!!!!!!!!!!!!!!!!",request.FILES,"@@")
          image = request.FILES['upload_image']
          print("!!!!!!!!!!!!!!!!!!!!!!!!!!!",image)
          title = request.POST.get('title')
          name = request.POST.get('name')
          content = request.POST.get('content')
          contents = Content(title = title, image = image,  content = content)
          contents.save()
          return redirect('share:home')
     else:
          return render(request, 'add.html')
     #if request.method == "POST":
     #     image = request.POST.get('image')
     #     title = request.POST.get('title')
     #     relay = request.POST.get('relay')
     #     name = request.POST.get('name')
     #     content = request.POST.get('content')
     #     contents = Content(title = title, image = image, relay = relay, content = content)
     #     return render(request, 'add.html', {'contents':contents})
     #return render(request, 'add.html')
     #return render(request,'add.html')
     #if request.method == "POST":
     #   form = PostForm(request.POST)
     #  if form.is_valid():
     #      form.save()
     #      return redirect('home')
     #return render(request, 'add.html', {'form': form})
          

# 수정 후 업데이트
def update(request, id):
     if request.method == "POST":
          contents = Content.objects.get(pk=id)
          # tags= Tag.objects.get(pk=id)
          
          title = request.POST.get('title')
          image = request.POST.get('image')
          
          # name = request.POST.get('name')
          content = request.POST.get('content')
          
          contents.title = title
          contents.image = image
          
          contents.content = content
          
          # Tag.name = name
          
          contents.save()
          # tags.save()
          return redirect ('share:home')
          
          
# 수정 
def edit(request, id):
     contents = Content.objects.get(pk=id)
     # tags = Tag.objects.get(pk=id)
     return render(request, 'edit.html', {'contents': contents})          
     

#삭제
def delete(request, id):
     if request.method == "GET":
          contents = Content.objects.get(pk=id)
          contents.delete()
          return redirect('share:home')
     return redirect('share:home')

def search(request):
     q=request.GET['q']
     ans = Content.objects.filter(title=q)
     return render (request, 'search.html',{'q':q,'ans':ans})

# #좋아요 숫자세기
# @login_required
# @require_POST
# def like(request):
#    if request.method == 'POST':
#         user = request.user # 로그인한 유저를 가져온다.
#         memo_id = request.POST.get('pk', None)
#         memo = Memos.objects.get(pk = memo_id)
#         if memo.likes.filter(id = user.id).exists():
#              memo.likes.remove(user)
#              message = 'You disliked this'
#         else:
#             memo.likes.add(user)
#             message = 'You liked this'

#    context = {'likes_count' : memo.total_likes, 'message' : message}
#    return HttpResponse(json.dumps(context), content_type='application/json')  

def comment(request,id):
     content = Content.objects.get(id=id)
     if request.method =="POST":
          comment_content = request.POST.get('comment')
          comment = Comment(comment=comment_content, content=content)
          comment.save()
          
          comments = Comment.objects.filter(content=content)
          
          return redirect('/'+str(content.id))
     return render(request, 'home.html')
     
     
# def editcomment(request, id):
#      comment = Comment.objects.get(id=id)
#      return render(request, 'editcomment.html', {'comment', comment})          
     
     
# def updatecomment(request, id):
#      if request.method == "POST":
#           comment = Comment.objects.get(pk=id)
          
          
#           comment = request.POST.get('comment')
         
#           Comment.comment = comment
         
                   
#           contents.save()
         
#           return redirect ('.html') 