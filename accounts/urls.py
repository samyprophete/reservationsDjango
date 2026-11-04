from django.urls import path
from .import views 
from .views import UserSignUpView

app_name = 'accounts'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('profile/', views.profile, name='user-profile'),   
]
