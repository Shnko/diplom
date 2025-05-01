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

            elobova = User.objects.create_user('elobova', 'elobova@example.com', 'elobova')
            elobova.is_admin = True
            elobova.is_staff = True
            elobova.is_active = True
            elobova.first_name = 'Екатерина'
            elobova.last_name = 'Лобова'
            elobova.save()