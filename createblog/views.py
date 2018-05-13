from django.shortcuts import render
from models import NewPost
from django.http import HttpResponse
# Create your views here.



def index(request):

    posts=NewPost.objects.all()
    postlist=posts[::-1]
    return render(request,"index.html",{'postlist':postlist})

def createnewpost(request):
    if request.method =='POST':
        post_name=request.POST.get('posttitle')
        post_text=request.POST.get('posttext')
        p=NewPost(post_name=post_name,post_text=post_text)
        p.save()
    return render(request,'createpost.html')

def deletepost(request):    
    if request.method == 'POST':        
        post_id=request.POST.get('post_id')
        NewPost.objects.filter(pk=post_id).delete()
        posts=NewPost.objects.all()
        postlist=posts[::-1]
        return render(request,"index.html",{'postlist':postlist})



