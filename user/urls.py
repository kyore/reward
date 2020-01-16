from django.urls import path

from .views import LoginView, UserCreateView, DivisionCreateView, SupervisorCreateView, HrCreateView, logout_view

app_name = 'user'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('create/supervisor/', SupervisorCreateView.as_view(), name='create-supervisor'),
    path('create/hr/', HrCreateView.as_view(), name='create-hr'),
    path('division/create/', DivisionCreateView.as_view(), name='division-create'),
]
