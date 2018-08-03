from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from nickle.views.home import HomeView

urlpatterns = [
    url(r'^$', login_required(HomeView.as_view())),
]
