from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
import sys
from dotenv import load_dotenv
load_dotenv()

class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials from environment variables'

    def handle(self, *args, **options):
        username = os.environ.get('SUPERUSER_USERNAME')
        email = os.environ.get('SUPERUSER_EMAIL')
        password = os.environ.get('SUPERUSER_PASSWORD')

        # Validar que todas las variables de entorno estén presentes
        if not all([username, email, password]):
            self.stderr.write(self.style.ERROR(
                'Error: SUPERUSER_USERNAME, SUPERUSER_EMAIL, and SUPERUSER_PASSWORD environment variables are required.'
            ))
            sys.exit(1)

        # Verificar si el superusuario ya existe
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))
        else:
            try:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error creating superuser "{username}": {e}'))
                sys.exit(1)
