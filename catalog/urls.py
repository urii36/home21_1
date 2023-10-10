from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import ProductListView, contacts, ProductDetailView

app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', contacts, name='contacts'),
    path('product/<str:name>/', ProductDetailView.as_view(), name='product_detail'),
]
