# gameapp/views.py
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    points = request.session.get('points', 0)
    return render(request, 'gameapp/home.html', {'points': points})

def game1(request):
    """Simple Clicker Game: Click the moving button to earn points."""
    return render(request, 'gameapp/game1.html')

def game2(request):
    """Simple Reaction Game: Click the button as soon as it appears."""
    return render(request, 'gameapp/game2.html')

def add_points(request):
    if request.method == "POST":
        earned = int(request.POST.get('points', 0))
        current_points = request.session.get('points', 0)
        request.session['points'] = current_points + earned
        return JsonResponse({'new_points': request.session['points']})
    return JsonResponse({'error': 'Invalid request'})

def shop(request):
    points = request.session.get('points', 0)
    can_download = points >= 251
    return render(request, 'gameapp/shop.html', {'points': points, 'can_download': can_download})
