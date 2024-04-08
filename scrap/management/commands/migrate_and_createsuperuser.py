from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Migrates the database and creates a superuser if one does not exist.'

    def handle(self, *args, **options):
        # Migrate database
        self.stdout.write("Migrating database...")
        call_command('migrate', interactive=False)

        # Check if superuser exists
        if not User.objects.filter(is_superuser=True).exists():
            # Create superuser
            self.stdout.write("Creating superuser...")
            User.objects.create_superuser(username='nill', email='moinulantu@gmail.com', password='nill@1234')
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
        else:
            self.stdout.write("Superuser already exists.")
