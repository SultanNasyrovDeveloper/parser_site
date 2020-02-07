from django.urls import path

from landing.index import views


app_name = 'index'


urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('download/<int:example_id>', views.download_document, name='download'),
]