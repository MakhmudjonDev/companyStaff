from django.urls import path
from .views import *
urlpatterns = [
    # path('update/', Person_update),
    path('', home_view),

    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('dashboard/',dashboard_view, name='dashboard'),
]
