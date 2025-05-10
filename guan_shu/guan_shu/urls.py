# guanshu/urls.py
from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from markets import views as markets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', markets_views.market_list, name='home'),
    path('markets/<int:pk>/', markets_views.market_detail, name='market_detail'),
    path('accounts/register/', accounts_views.register_view, name='register'),
    path('accounts/login/', accounts_views.login_view, name='login'),
    path('accounts/logout/', accounts_views.logout_view, name='logout'),
]