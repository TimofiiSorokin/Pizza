from django.urls import path

from company.api.views import (CatalogPageAPIView, CatalogCreateAPIView, CatalogDetailAPIView)

urlpatterns = [
    # 4) A user should be able to observe a list of wishlists.
    path('catalog', CatalogPageAPIView.as_view(), name='catalog-page'),
    # 3) A user should be able to edit wishlist.
    # 2) A user should be able to create a wishlist and add items.
    path('catalog/create', CatalogCreateAPIView.as_view(), name='pizza-create'),
    # 5) A user should be able to see details of any own wishlist.
    path('catalog/detail/<int:pk>', CatalogDetailAPIView.as_view(), name='catalog-detail'),

]

# 1) A user should be able to login using google auth.
# 6) A user should be able to share any wishlist with other users.
# 7) A user should be able to reserve any item in the shared wishlist.