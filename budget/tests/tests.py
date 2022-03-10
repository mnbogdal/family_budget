from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


from rest_framework.test import APIClient

from ..models import Budget


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


class UsersViewSetAPICase(TestCase):
    fixtures = ['users.yaml', 'budget.yaml', 'categories.yaml',
                'incomes.yaml', 'expenses.yaml']

    def setUp(self):
        self.budget_list_url = reverse("budget:budget-list")

    def test_is_response_200(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get(self.budget_list_url)
        assert response.status_code == 200

    def test_is_response_401(self):
        client = APIClient()
        response = client.get(self.budget_list_url)
        assert response.status_code == 401
