from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a default admin user'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "Admin@123")
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created successfully."))
        else:
            self.stdout.write(self.style.WARNING("Superuser 'admin' already exists."))
