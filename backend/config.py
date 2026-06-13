import os


class Config:
    """
    Central application configuration.

    The project does not use a database yet, but the database-related
    environment variables are already defined here so adding a DB later
    will be a small infrastructure change instead of a redesign.
    """

    APP_NAME = os.getenv("APP_NAME", "kubeops-backend")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    APP_ENV = os.getenv("APP_ENV", "local")

    # Kubernetes automatically exposes the Pod name through the HOSTNAME env variable.
    POD_NAME = os.getenv("HOSTNAME", "local-machine")

    # Demo secret. In Kubernetes, this will come from a Secret object.
    DEMO_API_KEY = os.getenv("DEMO_API_KEY", "")

    # Future database configuration.
    DB_HOST = os.getenv("DB_HOST", "")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "")
    DB_USER = os.getenv("DB_USER", "")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

    @classmethod
    def is_database_configured(cls):
        """
        Returns True only when the minimal database configuration exists.

        We are not connecting to a database yet, but this helps us design
        the service in a way that is ready for a future database integration.
        """
        return all([
            cls.DB_HOST,
            cls.DB_NAME,
            cls.DB_USER,
            cls.DB_PASSWORD
        ])