# markets/views.py
from django.shortcuts import render, get_object_or_404
from .models import Market, MarketCategory
from django.contrib.auth.decorators import login_required

# login_required decorator
def market_list(request):
    markets = Market.objects.filter(is_active=True).order_by('-created_at')
    categories = MarketCategory.objects.all()
    is_authenticated = request.user.is_authenticated
    user = request.user
    return render(request, 'market_list.html', {
        'markets': markets,
        'categories': categories,
        'is_authenticated': is_authenticated,
        'user': user,
    })

def market_detail(request, pk):
    market = get_object_or_404(Market, pk=pk)
    return render(request, 'market_detail.html', {'market': market})

def multiversex(request):
    return render(request, 'multiversex.html')

def explorer_solana(request):
    return render(request, 'explorer_solana.html')