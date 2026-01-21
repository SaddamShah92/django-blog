from django.test import TestCase
from .models import About

class AboutModelTests(TestCase):

    def test_about_model_creation(self):
        about = About.objects.create(
            about_heading="About Us",
            about_description="This is the about description for the site."
        )
        self.assertEqual(about.about_heading, "About Us")
        self.assertEqual(about.about_description, "This is the about description for the site.")
        self.assertTrue(about.created_at)  # created_at should be set automatically

    def test_about_str_method(self):
        about = About.objects.create(
            about_heading="About Us",
            about_description="Description here."
        )
        self.assertEqual(str(about), "About Us")  # Ensures the __str__ method works correctly


class SocialLinkModelTests(TestCase):

    def test_sociallink_model_creation(self):
        social_link = SocialLink.objects.create(
            platform="Facebook",
            link="https://facebook.com/test"
        )
        self.assertEqual(social_link.platform, "Facebook")
        self.assertEqual(social_link.link, "https://facebook.com/test")
        self.assertTrue(social_link.created_at)  # created_at should be set automatically

    def test_sociallink_str_method(self):
        social_link = SocialLink.objects.create(
            platform="Twitter",
            link="https://twitter.com/test"
        )
        self.assertEqual(str(social_link), "Twitter")  # Ensures the __str__ method works correctly