from django.conf.urls import url
from nickle.views.home import HomeView

urlpatterns = [
    url(r'^', HomeView.as_view()),
]
