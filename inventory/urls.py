from django.conf.urls import url
from . import views

app_name = "inventory"

urlpatterns = [
    url(r'^product_list', views.ProductView.list, name='product_list'),
    url(r'^product_create', views.ProductView.create, name='product_create'),
    # url(r'^product_save', views.ProductView.save, name='product_save'),
    ]