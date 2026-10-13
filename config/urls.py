from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar


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
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )