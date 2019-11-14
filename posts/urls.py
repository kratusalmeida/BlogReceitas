
from posts.views import  listarReceitas,criarReceita,atualizarReceita,deletarReceita
from django.urls import path


urlpatterns = [
    path('list/',listarReceitas, name="postsList"),
    path('new/', criarReceita, name="postsNew"),
    path('update/<int:id>/', atualizarReceita, name="postsUpdate"),
    path('delete/<int:id>/', deletarReceita, name="postsDelete"),

    ]
