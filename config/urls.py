from django.contrib import admin
from django.urls import path
from guest import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/delete/<int:message_id>/", views.delete_message, name="delete_message"),
    path("dashboard/delete-all/", views.delete_all_messages, name="delete_all_messages"),
]
