from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar


handler403 = "blog.views.custom_403"


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Blog
    path("", include("blog.urls")),

    # Login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html"
        ),
        name="login",
    ),

    # Logout
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="blog:home"
        ),
        name="logout",
    ),

    # Debug Toolbar
    path("__debug__/", include(debug_toolbar.urls)),

    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="blog/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="blog/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="blog/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="blog/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )