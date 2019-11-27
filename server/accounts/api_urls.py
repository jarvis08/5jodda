from django.urls import path
from. import api_views


app_name = 'api_accounts'

urlpatterns = [
    path('', api_views.user_list, name='user_list'),
    path('<int:user_pk>/', api_views.user_detail, name='user_detail'),
    path('<int:user_pk>/delete/', api_views.user_delete, name='user_delete'),
]