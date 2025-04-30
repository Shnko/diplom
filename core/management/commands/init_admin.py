from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Creates default superuser."

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            admin.is_superuser = True
            admin.is_admin = True
            admin.is_active = True
            admin.save()
