from django.shortcuts import render, redirect
from .models import FoodSpot
from .forms import FoodSpotForm
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q


def home(request):
    food_type = request.GET.get('type')
    search_query = request.GET.get('search', '')
    now = timezone.now()

    # Get spots where available_until is in the future OR null
    spots = FoodSpot.objects.filter(
        Q(available_until__gt=now) | Q(available_until__isnull=True)
    )

    if food_type:
        spots = spots.filter(food_type=food_type)

    if search_query:
        spots = spots.filter(description__icontains=search_query)

    context = {
        'spots': spots,
        'selected_type': food_type,
        'search_query': search_query,
    }
    return render(request, 'tracker/home.html', context)



def post_spot(request):
    if request.method == 'POST':
        form = FoodSpotForm(request.POST, request.FILES)
        if form.is_valid():
            spot = form.save()
            messages.success(request, '✅ Food spot posted successfully!')
            return redirect('home')
    else:
        form = FoodSpotForm()
    return render(request, 'tracker/post_spot.html', {'form': form})
