from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError  # <-- Import these!

class SubhubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subhub'

    def ready(self):
        User = get_user_model()
        try:
            if not User.objects.filter(username='adminmanasa').exists():
                User.objects.create_superuser('adminmanasa', 'manasaneeli57@gmail.com', '22am1a3157')
        except (OperationalError, ProgrammingError):
            # Database might not be ready, so ignore errors here
            pass
