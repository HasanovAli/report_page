from django.shortcuts import render


def readme(request):
    return render(request, 'index.html')
