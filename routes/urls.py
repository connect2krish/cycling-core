from django.urls import path

from routes.views import (
    route_detail_view,
    # route_delete_view,
    route_create_view,
    route_list_view,
)

urlpatterns = [
    path('<int:id>', route_detail_view),
    path('create', route_create_view),
    # path('delete/<int:id>', product_delete_view),
    path('', route_list_view),
]
