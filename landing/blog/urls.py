from django.urls import path

from landing.blog import views


app_name = 'blog'


urlpatterns = [
    path('<int:pk>', views.PostDetail.as_view(), name='detail'),
]