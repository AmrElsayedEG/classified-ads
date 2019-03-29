from django.urls import path, include

from ads import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/products',views.ProductsView)
app_name = "ads"
urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.productsview),
    path('test/',views.CategorySearch),
    path('product/<int:id>/',views.oneproduct),
    path('search/',views.search),
    path('my-ads/',views.user_products),
    path('acc/',views.redirectaccounthome),
    path('contact/',views.contact),
    path('add/',views.add_product),
    path('',include(router.urls)),
    path('favorites/',views.favorites),
]