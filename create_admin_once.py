from django.contrib.auth import get_user_model

User = get_user_model()
username = "adminmanasa"
password = "adminpassword123"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    print(f"✅ Creating superuser: {username}")
    User.objects.create_superuser(username=username, password=password, email=email)
else:
    print(f"⚠️ Superuser '{username}' already exists.")
