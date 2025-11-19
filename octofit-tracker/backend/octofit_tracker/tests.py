from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Team.objects.create(name='Marvel')
        Team.objects.create(name='DC')
        User.objects.create_user(username='IronMan', email='ironman@marvel.com', password='test1234', team='Marvel')
        User.objects.create_user(username='Batman', email='batman@dc.com', password='test1234', team='DC')
        Activity.objects.create(name='Running', user_email='ironman@marvel.com')
        Leaderboard.objects.create(team='Marvel', points=100)
        Workout.objects.create(name='Pushups', difficulty='Easy')

    def test_api_root(self):
        response = self.client.get(reverse('api_root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
