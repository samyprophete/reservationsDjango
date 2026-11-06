from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView 
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserSignUpForm 
from django.shortcuts import redirect, render                              # <-- ajoute render
from django.contrib.auth.decorators import login_required 
from .forms import UserUpdateForm                                  # <-- AJOUTER
from django.contrib.auth.models import User    


class UserUpdateView(UserPassesTestMixin, UpdateView):             # <-- AJOUTER (toute la classe)
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("accounts:user-profile")
    template_name = "user/update.html"

    def test_func(self):
        pkInURL = self.kwargs['pk']
        return self.request.user.is_authenticated and self.request.user.id == pkInURL or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Vous n'avez pas l'autorisation d'accéder à cette page!")
        return redirect('accounts:user-profile')

@login_required
def profile(request):
    languages = {
        "fr": "Français",
        "en": "English",
        "nl": "Nederlands",
    }
    return render(request, 'user/profile.html', {
        "user_language": languages[request.user.usermeta.langue],
    })
    
class UserSignUpView(UserPassesTestMixin, CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def test_func(self):
        return self.request.user.is_anonymous or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Vous êtes déjà inscrit!")
        return redirect('home')