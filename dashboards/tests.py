from django.test import TestCase
from django.urls import reverse
from blogs.models import Category, Blog
from django.contrib.auth.models import User

class CategoryViewsTests(TestCase):

    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_add_category(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_category'), {'category_name': 'Tech'})
        self.assertEqual(response.status_code, 302)  # Should redirect to categories page
        self.assertEqual(Category.objects.count(), 1)  # Ensure category is created

    def test_edit_category(self):
        category = Category.objects.create(category_name='Tech')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_category', args=[category.pk]), {'category_name': 'Updated Tech'})
        self.assertEqual(response.status_code, 302)  # Should redirect to categories page
        category.refresh_from_db()
        self.assertEqual(category.category_name, 'Updated Tech')

    def test_delete_category(self):
        category = Category.objects.create(category_name='Tech')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_category', args=[category.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect to categories page
        self.assertEqual(Category.objects.count(), 0)  # Ensure category is deleted


class BlogViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(category_name='Tech')
        self.client.login(username='testuser', password='testpassword')

    def test_edit_post(self):
        blog = Blog.objects.create(
            title='Old Blog Post',
            slug='old-blog-post',
            category=self.category,
            author=self.user,
            featured_image='image.jpg',
            short_description='Short description',
            blog_body='Blog content',
            status='Published',
            is_featured=True
        )
        response = self.client.post(reverse('edit_post', args=[blog.pk]), {
            'title': 'Updated Blog Post',
            'category': self.category.id,
            'featured_image': 'image.jpg',
            'short_description': 'Updated short description',
            'blog_body': 'Updated blog content',
            'status': 'Published',
            'is_featured': True
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to posts page
        blog.refresh_from_db()
        self.assertEqual(blog.title, 'Updated Blog Post')  # Check title updated
        self.assertTrue(blog.slug.startswith('updated-blog-post'))  # Check slug is updated

    def test_delete_post(self):
        blog = Blog.objects.create(
            title='Blog to be deleted',
            slug='blog-to-be-deleted',
            category=self.category,
            author=self.user,
            featured_image='image.jpg',
            short_description='Short description',
            blog_body='Blog content',
            status='Published',
            is_featured=True
        )
        response = self.client.post(reverse('delete_post', args=[blog.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect to posts page
        self.assertEqual(Blog.objects.count(), 0)  # Ensure blog post is deleted


class UserViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_add_user(self):
        response = self.client.post(reverse('add_user'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to users page
        self.assertEqual(User.objects.count(), 2)  # Ensure new user is created

    def test_edit_user(self):
        user = User.objects.create_user(username='user1', password='testpassword')
        response = self.client.post(reverse('edit_user', args=[user.pk]), {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to users page
        user.refresh_from_db()
        self.assertEqual(user.username, 'updateduser')  # Ensure username is updated

    def test_delete_user(self):
        user = User.objects.create_user(username='user2', password='testpassword')
        response = self.client.post(reverse('delete_user', args=[user.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect to users page
        self.assertEqual(User.objects.count(), 1)  # Ensure user is deleted

