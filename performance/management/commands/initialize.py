from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.cache import cache

from faker import Faker

from category.models import Event, AgeGroup
from performance.models import Performance
from participant.models import Participant


class CubeFaker:

    def __init__(self):
        cache.clear()
        self.faker = Faker()
        self.events = []
        self.participants = []
        self.ageGroups = []
        self.performances = []

    def create_events(self, count=10):
        events = []
        for i in range(count):
            events.append(
                Event(
                    name=self.faker.text(max_nb_chars=35),
                )
            )
        self.events = Event.objects.bulk_create(events)

    def create_age_groups(self, count=5):
        ageGroups = []
        samples = [
            {"name": "6-7", "minAge": 6, "maxAge": 7},
            {"name": "8-12", "minAge": 8, "maxAge": 12},
            {"name": "13-16", "minAge": 13, "maxAge": 16},
            {"name": "17-19", "minAge": 17, "maxAge": 19},
        ]
        for i in samples:
            ageGroups.append(
                AgeGroup(
                    name=i['name'],
                    maxAge=i['maxAge'],
                    minAge=i['minAge']
                )
            )
        self.ageGroups = AgeGroup.objects.bulk_create(ageGroups)
        for a in self.ageGroups:
            for e in self.events:
                a.event.add(e)

    def create_participants(self, count=200):
        participants = []
        for i in range(count):
            participants.append(
                Participant(
                    name=self.faker.name(),
                    contact=self.faker.phone_number(),
                    email=self.faker.email(),
                    dob=self.faker.date(),
                    isEmailVerified=True,
                    gender="F" if self.faker.random_int(min=0, max=10) % 3 == 0 else "M",
                    city=self.faker.city(),
                    state=self.faker.state(),
                    country=self.faker.country(),
                    referredBy=self.faker.name(),
                    isOnline=self.faker.random_int(min=0, max=10) % 3 == 0,
                    ageGroup=list(self.ageGroups)[self.faker.random_int(min=0, max=len(self.ageGroups)-1)]
                )
            )
        self.participants = Participant.objects.bulk_create(participants)
        for p in self.participants:
            for e in self.events:
                p.event.add(e)

    def create_performances(self, count=350):
        i = 0
        while i < count:
            event = list(self.events)[self.faker.random_int(min=0, max=len(self.events) - 1)]
            participant = list(self.participants)[self.faker.random_int(min=0, max=len(self.participants) - 1)]
            try:
                Performance.objects.create(
                    duration=timedelta(
                        minutes=self.faker.random_int(min=0, max=59),
                        seconds=self.faker.random_int(min=0, max=59),
                    ),
                    event=event,
                    participant=participant
                )
                i += 1
            except Exception:
                pass

    def initialize(self):
        print("\nCreating Admin User")
        admin_username = input("Username: ")
        admin_email = input("Email: ")
        from getpass import getpass

        admin_password = getpass("Password: ")

        User = get_user_model()

        user = User.objects.create(
            username=admin_username,
            email=admin_email,
            is_superuser=True,
            is_staff=True,
        )
        user.set_password(admin_password)
        user.save()
        print("Admin account created. \n")

        self.create_events()
        self.create_age_groups()
        self.create_participants()
        self.create_performances()

        print("Done! Completed initializing a mock cube event")


class Command(BaseCommand):

    def handle(self, *args, **options):
        import os
        import django

        os.environ["DJANGO_SETTINGS_MODULE"] = "framework.settings"
        django.setup()
        django.core.management.execute_from_command_line(["manage.py", "migrate"])
        django.core.management.execute_from_command_line(["manage.py", "flush", "--no-input"])

        cube = CubeFaker()
        cube.initialize()
