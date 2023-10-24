from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(
            id=1,
            name="test",
            message="test",
        )
    
    
    def test_model_content(self):
        self.assertEqual(self.post.id, 1)
        self.assertEqual(self.post.name, "test")
        self.assertEqual(self.post.message, "test")
    
    
    def test_url_exist_at_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_not_available_by_name(self):
        response = self.client.get(reverse("home") + "1")
        self.assertNotEqual(response.status_code, 200)
    
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "test")
        