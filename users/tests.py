from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccountPageTests(TestCase):
    def test_auth_forms_render(self):
        for page in ('login', 'register'):
            with self.subTest(page=page):
                self.assertEqual(self.client.get(reverse(page)).status_code, 200)

    def test_logout_uses_post(self):
        user = get_user_model().objects.create_user(username='demo')
        self.client.force_login(user)

        home = self.client.get(reverse('blog-home'))
        self.assertContains(home, 'method="post"')
        self.assertContains(home, 'action="/logout/"')
        self.assertEqual(self.client.get(reverse('logout')).status_code, 405)
        self.assertIn('_auth_user_id', self.client.session)

        self.assertContains(self.client.post(reverse('logout')), 'You have been logged out')
        self.assertNotIn('_auth_user_id', self.client.session)
