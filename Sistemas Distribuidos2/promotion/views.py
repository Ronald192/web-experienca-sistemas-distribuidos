from .models import Promotion
from django.shortcuts import render


# Create your views here.

def promotion_list(request):
    promotions = Promotion.objects.all()
    return render(request, 'promotion/list.html', {'promotions': promotions})
