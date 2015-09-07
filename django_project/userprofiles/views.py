from django.shortcuts import render

from .forms import UserCreationEmailForm
from .forms import EmailAuthenticationForm
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class LoginView(TemplateView):

    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context = super(LoginView,self).get_context_data(**kwargs)
        is_auth = False
 #mirar       #if self.request




def signup(request):
    form = UserCreationEmailForm(request.POST or None)
    if form.is_valid():
        form.save()

        #loguear
        #crear userprofiles
        #redireccionar al home

    return render(request, 'signup.html', {'form': form})


def signin(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        #redireccionar el home

    return render(request, 'signin.html', {'form': form})