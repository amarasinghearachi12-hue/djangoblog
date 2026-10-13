
from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    RegisterView,
    MyPostsView,
    about,
    contact,
    CategoryPostListView,
)

app_name = "blog"

urlpatterns = [

    # =====================================================
    # Register
    # =====================================================

    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

    # =====================================================
    # Home
    # =====================================================

    path(
        "",
        PostListView.as_view(),
        name="home",
    ),

    # =====================================================
    # My Posts
    # =====================================================

    path(
        "my-posts/",
        MyPostsView.as_view(),
        name="my_posts",
    ),

    # =====================================================
    # Create Post
    # =====================================================

    path(
        "posts/new/",
        PostCreateView.as_view(),
        name="post_create",
    ),

    # =====================================================
    # Post Detail
    # =====================================================

    path(
        "posts/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),

    # =====================================================
    # Edit Post
    # =====================================================

    path(
        "posts/<slug:slug>/edit/",
        PostUpdateView.as_view(),
        name="post_update",
    ),

    # =====================================================
    # Delete Post
    # =====================================================

    path(
        "posts/<slug:slug>/delete/",
        PostDeleteView.as_view(),
        name="post_delete",
    ),

    # =====================================================
    # About
    # =====================================================

    path(
        "about/",
        about,
        name="about",
    ),

    # =====================================================
    # Contact
    # =====================================================

    path(
        "contact/",
        contact,
        name="contact",
    ),

    # =====================================================
    # Category
    # =====================================================

    path(
        "category/<str:category_name>/",
        CategoryPostListView.as_view(),
        name="category_posts",
    ),
]
