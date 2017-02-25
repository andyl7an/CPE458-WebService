from django.conf.urls import include, url
from newLoc.views import Add_Loc



urlpatterns = [
    url(r'^$',  Add_Loc.as_view(), name='home'),
]
