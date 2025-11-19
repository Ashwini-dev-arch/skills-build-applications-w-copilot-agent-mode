from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            {'email': 'ironman@marvel.com', 'username': 'IronMan', 'team': marvel},
            {'email': 'captain@marvel.com', 'username': 'CaptainAmerica', 'team': marvel},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': dc},
            {'email': 'wonderwoman@dc.com', 'username': 'WonderWoman', 'team': dc},
        ]
        for u in users:
            user = User.objects.create_user(email=u['email'], username=u['username'], password='test1234')
            # Optionally associate team if using a ForeignKey

        # Create activities
        Activity.objects.create(name='Running', user_email='ironman@marvel.com')
        Activity.objects.create(name='Swimming', user_email='batman@dc.com')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
