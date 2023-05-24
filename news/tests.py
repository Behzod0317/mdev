from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.

class Newstest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'myself',
            email = 'test@email.com',
            password = 'parol123',
        )
        self.post = Post.objects.create(
            title = 'new test post',
            content = 'content text',
            author = self.user,

        )

    def test_string_representation(self):
        post = Post(title = 'Post mavzusi')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','new test post')
        self.assertEqual(f'{self.post.author}','myself')
        self.assertEqual(f'{self.post.content}','content text')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'content text')
        self.assertTemplateUsed(response, 'home.html')


    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,301)
        self.assertContains(response, 'new test post')
        self.assertTemplateUsed(response,'post_detail.html')
