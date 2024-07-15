# from django.contrib import admin
from django.urls import path
from .views import CategoryViewSet, ProductViewSet

urlpatterns = [
    path(
        "categories",
        CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "categories/<pk>",
        CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "Product",
        ProductViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "Product/<pk>",
        ProductViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
]
