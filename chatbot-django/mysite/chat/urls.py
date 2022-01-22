# chat/urls.py


# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
# -----------------------

# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

#---------------------
# from django.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
# ]
from django.urls import path
from . import views

from .views import index, room


urlpatterns = [

    path('', index, name='index'),
    path('<str:room_name>/', views.room, name="room"),
    path('<room_name>/', views.room, name="room"),

]