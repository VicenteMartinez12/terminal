from django.shortcuts import render

# Create your views here.
def menu_principal(request):
    return render(request, 'centra/menu.html')