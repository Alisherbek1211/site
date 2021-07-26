from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("add-cartitem/<int:product_id>/",add_cartitem,name="add-cartitem"),
    path("subtract-cartitem/<int:product_id>/",substract_cartitem,name="subtract-cartitem"),
    path("remove-cartitem/<int:product_id>/",remove_cartitem,name="remove-cartitem"),
    path("cart/",cart,name="cart"),
]