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

    def test_get_and_filter_budgets(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get(self.budget_list_url)
        self.assertEqual(response.data['count'], 3)
        response = client.get(reverse("budget:budget-detail", args=[2]))
        self.assertEqual(response.data['name'], 'b2')
        response = client.get('%s?owner=%s' % (reverse('budget:budget-list'), 2))
        self.assertEqual(response.data['count'], 2)

    def test_get_expenses(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get('%s?budget=%s' % (reverse('budget:expense-list'), 1))
        self.assertEqual(response.data['count'], 1)
        response = client.get('%s?budget=%s' % (reverse('budget:expense-list'), 3))
        self.assertEqual(response.data['count'], 0)

    def test_get_incomes(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get('%s?budget=%s' % (reverse('budget:income-list'), 1))
        self.assertEqual(response.data['count'], 2)
        response = client.get('%s?budget=%s' % (reverse('budget:income-list'), 3))
        self.assertEqual(response.data['count'], 1)


    def test_assigned_budgets_to_user(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get('%s?assigned_budgets=%s' % (reverse('budget:budget-list'), 1))
        self.assertEqual(response.data['count'], 0)
        response = client.get('%s?assigned_budgets=%s' % (reverse('budget:budget-list'), 2))
        self.assertEqual(response.data['count'], 1)


    def test_pagination(self):
        client = APIClient()
        admin = User.objects.get(username='admin')
        client.force_authenticate(user=admin)
        response = client.get(self.budget_list_url)
        self.assertEqual(response.data['next'], None)
