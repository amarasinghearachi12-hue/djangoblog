from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {'title': 'This is the Djangoblog Homepage.'})


def about(request):
    return render(request, 'blog/about.html', {'content': 'This is the Djangoblog team.'})