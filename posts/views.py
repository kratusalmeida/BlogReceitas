from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from posts.models import Post


def listarReceitas(request):
    postagens = Post.objects.all()
    return render(request, 'posts.html', {'posts':postagens})


def criarReceita(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('postsList')
    return render(request, 'posts_form.html',{'form':form})

def atualizarReceita(request, id):
    posts = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=posts)
    if form.is_valid():
        form.save()
        return redirect('postsList')
    return render(request,'posts_form.html',{'form':form})

def deletarReceita(request, id):
    postagens = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=postagens)
    if request.method == 'POST':
        postagens.delete()
        return redirect('postsList')
    return render(request, 'posts_delete_confirm.html', {'posts':postagens})

def home(request):

    return render(request, 'home.html')