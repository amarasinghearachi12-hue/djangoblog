
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login, models
from django.contrib import messages
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post, Category
from .forms import PostForm, UserRegisterForm


# =========================================================
# Register
# =========================================================

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("blog:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


# =========================================================
# Post List / Home
# =========================================================

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status="published"
        ).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


# =========================================================
# Post Detail
# =========================================================

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        if self.request.user.is_authenticated:
             post=Post.objects.filter( 
                  models.Q(status="published")
                | models.Q(author=self.request.user)
            )

        return Post


# =========================================================
# Create Post
# =========================================================

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(
            self.request,
            "Post created successfully!"
        )

        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


# =========================================================
# Update Post - Author Only
# =========================================================

class PostUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "login"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return self.object.get_absolute_url()


# =========================================================
# Delete Post - Author Only
# =========================================================

class PostDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    login_url = "login"
    success_url = reverse_lazy("blog:home")

    def test_func(self):
        return self.get_object().author == self.request.user


# =========================================================
# About
# =========================================================

def about(request):
    return render(
        request,
        "blog/about.html",
        {"team": "LankaVibe Team"},
    )


# =========================================================
# Contact
# =========================================================

def contact(request):
    return render(request, "blog/contact.html")


# =========================================================
# Category Posts
# =========================================================

class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/category_posts.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            name__iexact=self.kwargs["category_name"],
        )

        return Post.objects.filter(
            status="published",
            category=self.category,
        ).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context


# =========================================================
# My Posts Dashboard
# =========================================================

class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/my_posts.html"
    context_object_name = "posts"
    paginate_by = 6
    login_url = "login"

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        ).order_by("-created_at")


# =========================================================
# Custom 403 Forbidden Page
# =========================================================

def custom_403(request, exception):
    return render(
        request,
        "blog/403.html",
        status=403,
    )
def test_403(request):
    raise PermissionDenied

