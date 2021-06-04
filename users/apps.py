from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration for users app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):  # noreorder
        """Import custom signals."""
        import users.signals  # noqa: F401
