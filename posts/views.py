from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from posts.forms import CreatePostForm
from posts.models import *

# Create your views here.
def create_post(request):

    if request.method=='POST':
        createPostForm = CreatePostForm(request.POST,request.FILES);
        if createPostForm.is_valid():
            profile = createPostForm.save(commit=False);
            profile.user = request.user
            profile.author = request.user
            profile.save()
        return redirect('homepage')

    context = {
        'createPostForm':createPostForm,
    }

    return render(request, 'index.html', context=context)


def delete_post(request, pk):
    userPostForm = Post.objects.get(id=pk)
    if userPostForm.user == request.user:
        userPostForm.delete()
    else:
        return HttpResponse('You are not the author of the post')

    
    return redirect('homepage')


def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    user_exists = post.likes.filter(email=request.user.email).exists()
    
    if user_exists:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    
    context = {
        'obj':post,
    }
    
    return render(request, 'snippets/likes.html', context=context)






# def comment_post(request,post_id):
#     user = request.user
#     call = PostComments.objects.filter(post=AllPost.objects.get(id=post_id))
#     if not request.user.is_authenticated:
#         return redirect('login')
#     if request.method=='POST':
#         post = AllPost.objects.get(id=post_id)
#         content = request.POST.get('comment')
#         form = PostComments(user=user,post=post,content=content)
#         form.save()
#         return redirect(f'/posts/comment/{post_id}')
#     else:
#         return render(request,'comment.html', {'call':call} )