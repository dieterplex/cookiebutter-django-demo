from django.urls import path

from mva_demo.users.views import (
    user_detail_view,
    user_notification_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("~notification/", view=user_notification_view, name="notification"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
