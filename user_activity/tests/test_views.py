import mock
from django.test import TestCase, Client
from django.urls import reverse

from user_activity.views import UserActivity


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class TestUserActivity(TestCase):
    def setUp(self):
        self.client = Client()

    @mock.patch.object(UserActivity.activity_queryset, 'filter')
    def test_get_user_activity(self, mock_filter):
        mock_filter.return_value.exists.return_value = True
        get_response = self.client.get(path=reverse('get_json'))
        self.assertEqual(get_response.status_code, 200)

