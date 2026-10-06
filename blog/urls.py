from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    about,
    contact,
    CategoryPostListView,
)

app_name = "blog"

urlpatterns = [
    path(
        "",
        PostListView.as_view(),
        name="home",
    ),

    path(
        "posts/new/",
        PostCreateView.as_view(),
        name="post_create",
    ),

    path(
        "posts/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),

    path(
        "posts/<slug:slug>/edit/",
        PostUpdateView.as_view(),
        name="post_update",
    ),

    path(
        "posts/<slug:slug>/delete/",
        PostDeleteView.as_view(),
        name="post_delete",
    ),

    path(
        "about/",
        about,
        name="about",
    ),

    path(
        "contact/",
        contact,
        name="contact",
    ),
    path(
    "category/<str:category_name>/",
     CategoryPostListView.as_view(),
    name="category_posts",
),
]