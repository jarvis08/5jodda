from django.urls import path
from. import api_views


app_name = 'api_accounts'

urlpatterns = [
    path('', api_views.user_list, name='user_list'),
    path('<int:user_pk>/', api_views.user_detail, name='user_detail'),
<<<<<<< HEAD
    path('checker/', api_views.checker, name='checker'),
=======
    path('<int:user_pk>/delete/', api_views.user_delete, name='user_delete'),
>>>>>>> 8a680164a32f9b43bdbcf8d5f5163b1d8aea481f
]