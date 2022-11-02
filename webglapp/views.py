from django.shortcuts import render

# Create your views here.

def unity(request):
    return render(request, template_name='webglapp/index.html')

def test(request):
    return render(request, template_name='webglapp/test.html')