from django.shortcuts import render

from .forms import UserCreationEmailForm
# Create your views here.
def signup (request):
    form = UserCreationEmailForm()

    return render(request, 'signup.html', {'form': form})