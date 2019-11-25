from django.urls import path
from. import api_views


app_name = 'api_accounts'

urlpatterns = [
    path('<int:movie_pk>/', api_views.user_detail, name='user_detail'),
    path('signup/', api_views.signup, name='signup'),
]