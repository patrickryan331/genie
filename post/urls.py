from django.urls import path
import post.views as view

urlpatterns = [
    path('', view.HomePageView.as_view(), name='home'),
    path('about/', view.AboutPageView.as_view(), name='about'),
]