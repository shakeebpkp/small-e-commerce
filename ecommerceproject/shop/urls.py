
from . import views
from django.urls import path
app_name='shop'
urlpatterns = [
    path('',views.allprodCat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodCat,name='product_by_category'),
path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]