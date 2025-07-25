from blog.data import posts
from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        # 'text': 'Olá Blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def post(request, id):
    print('post', id)

    context = {
        # 'text': 'Olá Blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá Exemplo',
        'title': 'Essa é uma página de exemplo',
    }

    return render(
        request,
        'blog/exemplo.html',
        context,
    )
