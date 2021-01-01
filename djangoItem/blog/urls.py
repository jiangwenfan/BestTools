from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^index2$',views.index2),
    url(r'^books$',views.showBooks),
    url(r'^books/(\d+)$',views.details),

]