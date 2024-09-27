from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import category, group, product, atribute

urlpatterns = [
    path('categories/', category.CategoryListApiView.as_view(), name='categories'),
    path('groups/', group.GroupListApiView.as_view(), name='groups'),
    path('category/<slug:slug>/', category.CategoryDetailApiView.as_view(), name='category'),
    path('all-products/', product.ProductListApiView.as_view(), name='all-products'),
    path('all-images/', product.ImageListApiView.as_view(), name='all-products'),
    path('attribute-keys/', atribute.AttributeKeyAPIView.as_view(), name='attribute-key-list'),
    path('product-attributes/', atribute.ProductAttributeAPIView.as_view(), name='product-attribute-list'),
    path('attribute-values/', atribute.AttributeValueAPIView.as_view(), name='attribute-value-list'),

]
