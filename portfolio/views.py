from django.shortcuts import render

def portfolio(request):
    return render(request, 'portfolio.html', {

    })


def resume(request):
    return render(request, 'resume.html', {

    })