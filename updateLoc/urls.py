from django.conf.urls import include, url
from updateLoc.views import Update_Loc



urlpatterns = [
    url(r'^$',  Update_Loc.as_view(), name='home'),

]