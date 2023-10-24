from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        """
        Set up test data for the Post model.
        """
        cls.post = Post.objects.create(
            id=1,
            name="test",
            message="test",
        )

    def test_model_content(self) -> None:
        """
        Test the Post model's attributes.
        """
        self.assertEqual(self.post.id, 1)
        self.assertEqual(self.post.name, "test")
        self.assertEqual(self.post.message, "test")

    def test_url_exist_at_location(self) -> None:
        """
        Test if the URL '/' exists and returns a 200 status code.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_not_available_by_name(self) -> None:
        """
        Test if a URL with the name 'home' + '1' does not exist (not a 200 status code).
        """
        response = self.client.get(reverse("home") + "1")
        self.assertNotEqual(response.status_code, 200)

    def test_home_page(self) -> None:
        """
        Test the home page URL, template used, and content.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "test")
