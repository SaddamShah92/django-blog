from django.test import TestCase
from .models import Category, Comment, Blog
from django.contrib.auth.models import User
from django.urls import reverse

class CategoryModelTests(TestCase):

    def test_category_creation(self):
        category = Category.objects.create(category_name="Technology")
        self.assertEqual(category.category_name, "Technology")
        self.assertTrue(category.created_at)  # created_at should be set automatically

    def test_category_str_method(self):
        category = Category.objects.create(category_name="Lifestyle")
        self.assertEqual(str(category), "Lifestyle")

class BlogModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(category_name="Tech")
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_blog_creation(self):
        blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            category=self.category,
            author=self.user,
            featured_image="image.jpg",
            short_description="Short description",
            blog_body="Full blog content",
            status="Published",
            is_featured=True
        )
        self.assertEqual(blog.title, "Test Blog")
        self.assertEqual(blog.status, "Published")
        self.assertTrue(blog.created_at)  # created_at should be set automatically

    def test_blog_str_method(self):
        blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            category=self.category,
            author=self.user,
            featured_image="image.jpg",
            short_description="Short description",
            blog_body="Full blog content",
            status="Published",
            is_featured=True
        )
        self.assertEqual(str(blog), "Test Blog")

class CommentModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(category_name="Test Category")
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            category=self.category,
            author=self.user,
            short_description="Test description",
            blog_body="Test body",
            status="Published",
            is_featured=True
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(
            user=self.user,
            blog=self.blog,
            comment="This is a test comment"
        )
        self.assertEqual(comment.comment, "This is a test comment")
        self.assertTrue(comment.created_at)  # created_at should be set automatically

    def test_comment_str_method(self):
        comment = Comment.objects.create(
            user=self.user,
            blog=self.blog,
            comment="This is a test comment"
        )
        self.assertEqual(str(comment), "This is a test comment")

class PostsByCategoryViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.category = Category.objects.create(category_name="Test Category")
        self.blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            category=self.category,
            author=self.user,
            short_description="Test description",
            blog_body="Test body",
            status="Published",
            is_featured=True
        )

    def test_posts_by_category_view(self):
        response = self.client.get(reverse('posts_by_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")
        self.assertContains(response, self.category.category_name)

    def test_pagination(self):
        # Create multiple blogs to test pagination
        for _ in range(15):
            Blog.objects.create(
                title="Test Blog",
                slug="test-blog",
                category=self.category,
                author=self.user,
                featured_image="image.jpg",
                short_description="Short description",
                blog_body="Full blog content",
                status="Published",
                is_featured=True
            )

        response = self.client.get(reverse('posts_by_category', args=[self.category.id]) + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")

class BlogViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(category_name="Test Category")
        self.blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            category=self.category,
            author=self.user,
            featured_image="image.jpg",
            short_description="Short description",
            blog_body="Full blog content",
            status="Published",
            is_featured=True
        )

    def test_blog_view(self):
        response = self.client.get(reverse('blogs', args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.blog.title)
        self.assertContains(response, self.blog.blog_body)

    def test_post_comment(self):
        self.client.login(username="testuser", password="password")  # Ensure the user is logged in
        response = self.client.post(reverse('blogs', args=[self.blog.slug]), {'comment': "This is a test comment"})
        self.assertEqual(response.status_code, 302)  # Should redirect back to the same page
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().comment, "This is a test comment")

class SearchViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.category = Category.objects.create(category_name="Test Category")
        self.blog = Blog.objects.create(
            title="Test Blog",
            slug="test-blog",
            category=self.category,
            author=self.user,
            short_description="Test description",
            blog_body="Test body",
            status="Published",
            is_featured=True
        )

    def test_search_view(self):
        response = self.client.get(reverse('search') + '?keyword=Searchable')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.blog.title)

    def test_empty_search(self):
        response = self.client.get(reverse('search') + '?keyword=')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No blogs found.")
