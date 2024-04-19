from django.shortcuts import get_object_or_404, render
from .models import Rink

def get_rink(request, rink_id):
    rink = get_object_or_404(Rink, pk=rink_id)
    context = {
        'rink': rink,
    }
    return render(request, 'rinks/details.html', context)