from django.urls import path,re_path
from django.contrib import admin
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()

# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/games/$', views.games_list),

]