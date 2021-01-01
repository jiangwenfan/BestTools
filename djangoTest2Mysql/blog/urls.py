from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^index$',views.index),
    url(r'^book(\d+)$',views.delete),
    url(r'^create$',views.create),

]