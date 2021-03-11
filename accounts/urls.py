from django.urls import path
from accounts.views import login_view, logout_view, register_view, user_account, other_account, home


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', register_view, name='register'),
    path('profile/', user_account, name='profile'),
    path('user/<int:account_id>/', other_account, name='users'),
]

