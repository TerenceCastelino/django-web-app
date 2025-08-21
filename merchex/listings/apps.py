"""
Module: listings/apps.py

EN: App configuration for the "listings" Django app. Bilingual comments (EN/FR).
FR : Configuration de l'application Django "listings". Commentaires bilingues (EN/FR).
"""

from __future__ import annotations

# EN: Import Django's AppConfig base class
# FR : Importation de la classe de base AppConfig de Django
from django.apps import AppConfig


class ListingsConfig(AppConfig):
    """
    EN: Configuration class for the "listings" app.
    FR : Classe de configuration pour l'application "listings".
    """

    # EN: Default primary key field type for models in this app
    # FR : Type de clé primaire par défaut pour les modèles de cette app
    default_auto_field = "django.db.models.BigAutoField"

    # EN: Name used by Django to refer to this app
    # FR : Nom utilisé par Django pour référencer cette app
    name = "listings"
