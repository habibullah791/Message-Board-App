from django.urls import path
from .views import HomePageView


# add the URL pattern for the home page
urlpatterns = [
    path("", HomePageView.as_view(), name="home")
]