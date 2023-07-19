from django.shortcuts import render
from .models import Cliente

# Create your views here.
def index(request):
    cliente = Cliente.objects.all()
    return render(request, "CORE/index.html",{"cliente": cliente })

