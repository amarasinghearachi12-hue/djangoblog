from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostViewsTests(TestCase):
    def setUp(self):
        self.published_post = Post.objects.create(
            title="Primeiro artigo",
            slug="primeiro-artigo",
            excerpt="Um resumo curto.",
            content="Conteudo do artigo.",
            is_published=True,
        )
        Post.objects.create(
            title="Rascunho interno",
            slug="rascunho-interno",
            content="Ainda nao publicado.",
        )

    def test_list_shows_only_published_posts(self):
        response = self.client.get(reverse("blog:post_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published_post.title)
        self.assertNotContains(response, "Rascunho interno")

    def test_detail_shows_published_post(self):
        response = self.client.get(self.published_post.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Conteudo do artigo.")

    def test_detail_hides_draft(self):
        response = self.client.get("/blog/post/rascunho-interno/")

        self.assertEqual(response.status_code, 404)

    def test_home_shows_hello_world(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
