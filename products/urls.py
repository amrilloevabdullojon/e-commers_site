from django.urls import path

from products.views import ProductListView, ProductDetailView, WishListListView, create_wishlist, add_to_cart, \
    CartListView

app_name = 'products'
urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('wishlist/', WishListListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', create_wishlist, name='create_wishlist'),
    path('', ProductListView.as_view(), name='list')
]