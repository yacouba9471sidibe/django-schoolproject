from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import AddPostForm
from .models import Women

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

def index(request):
    posts = Women.objects.filter(is_published=True).order_by('-id')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'schoolapp/index.html', data)

def about(request):
    return render(request, 'schoolapp/about.html')

def show_post(request, post_slug):
    post = Women.objects.get(slug=post_slug)
    return render(request, 'schoolapp/post.html', {'post': post, 'menu': menu})

def contact(request):
    result = None
    if request.method == 'POST':
        result = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),
        }
    context = {
        'title': 'Обратная связь',
        'menu': menu,
        'result': result,
    }
    return render(request, 'schoolapp/contact.html', context)

def login(request):
    return HttpResponse("Страница входа (à venir)")

def upload(request):
    if request.method == 'POST':
        if 'myfile' in request.FILES:
            f = request.FILES['myfile']
            with open(f"uploads/{f.name}", "wb+") as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            return HttpResponse("Файл успешно загружен")
    return render(request, 'schoolapp/upload.html', {'menu': menu})

def map_view(request):
    return render(request, 'schoolapp/map.html', {'menu': menu})

def gemini_view(request):
    result = None
    if request.method == 'POST':
        user_question = request.POST.get('question')
        if user_question:
            result = f"Question : {user_question}\n\nRéponse : (démo)"
    return render(request, 'schoolapp/gemini.html', {'result': result, 'menu': menu})

class AddPage(PermissionRequiredMixin, CreateView):
    permission_required = 'schoolapp.add_women'
    form_class = AddPostForm
    template_name = 'schoolapp/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Добавление статьи'}