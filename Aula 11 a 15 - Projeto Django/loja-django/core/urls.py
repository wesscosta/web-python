
from django.contrib import admin
from django.urls import path
from app.views import ProductListView, ProductCreateView, ProductDetailView, ProductDeleteView,ProductUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view() , name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
