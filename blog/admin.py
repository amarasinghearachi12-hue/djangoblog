from django.contrib import admin

from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "category",
        "tags",
    )

    search_fields = (
        "title",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "tags",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "post_count",
    )

    search_fields = (
        "name",
    )

    def post_count(self, obj):
        return obj.posts.count()

    post_count.short_description = "Posts"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )