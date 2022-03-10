from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


from rest_framework.test import APIClient

"""
To make a test API call over an authenticated API endpoint, follow
this pattern:


```
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()
user = ...
client.force_authenticate(user=self.user)
response = client.get(reverse('{REVERSED_URL}'))
```

"""


class UserViewSetAPICase(TestCase):
    fixtures = ['users.yaml']

    def test_is_response_200(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get(reverse("users:users-list"))
        assert response.status_code == 200

    def test_is_response_401(self):
        client = APIClient()
        response = client.get(reverse("users:users-list"))
        assert response.status_code == 401

    def test_get_user_list(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get(reverse("users:users-list"))
        self.assertEqual(response.data['count'], 4)

