from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from PIL import Image


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    content = models.TextField()

    cover_image = models.ImageField(
        upload_to="post_covers/",
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="posts"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="published"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        # Generate a unique slug for new posts
        if not self.slug:
            base_slug = slugify(self.title)

            # Fallback for titles that produce an empty slug
            if not base_slug:
                base_slug = "post"

            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        # Save the post first
        super().save(*args, **kwargs)

        # Resize large cover images while preserving proportions
        if self.cover_image:
            img_path = self.cover_image.path

            try:
                with Image.open(img_path) as img:
                    if img.height > 800 or img.width > 800:
                        img.thumbnail((800, 800))
                        img.save(img_path)
            except (OSError, ValueError):
                # Skip resizing if the image cannot be processed
                pass

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            kwargs={"slug": self.slug}
        )

    def __str__(self):
        return self.title