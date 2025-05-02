from django.contrib.auth.models import User
from django.core.management import BaseCommand

from core.models import Child

class Command(BaseCommand):
    help = "Creates random data."

    def handle(self, *args, **options):
        for i in range(100):
            child = Child()
            child.save()
