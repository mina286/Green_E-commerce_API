from django.urls import path
from . import views

app_name ='products'

urlpatterns = [
    path('',views.products_list,name='products_list'),
    path('product_create/',views.product_create,name='product_create'),
    path('Generics_Category/',views.Generics_Category.as_view(),name='Generics_Category'),
    path('Mixins_Brand/',views.Mixins_Brand.as_view(),name='Mixins_Brand'),
    path('Generics_ProductImages/',views.Generics_ProductImages.as_view(),name='Generics_ProductImages'),
    path('Generics_ProductImages/<int:pk>/',views.Generics_ProductImages_PK.as_view(),name='Generics_ProductImages_PK'),
    path('Generics_Review/',views.Generics_Review.as_view(),name='Generics_Review'),
    path('Generics_Review/<int:pk>/',views.Generics_Review_PK.as_view(),name='Generics_Review_PK'),

    # slug product
    path('product_update/<slug:slug>/',views.product_update,name='product_update'),
    path('product_delete/<slug:slug>/',views.product_delete,name='product_delete'),
    path('<slug:slug>/',views.product_detail,name='product_detail'),
    # slug category
    path('Generics_Category/<slug:slug>/',views.Generics_Category_Slug.as_view(),name='Generics_Category_Slug'),
    # slug brand
    path('Mixins_Brand/<slug:slug>/',views.Mixins_Brand_Slug.as_view(),name='Mixins_Brand_Slug'),


]
