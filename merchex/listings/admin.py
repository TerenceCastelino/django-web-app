"""
Module: listings/admin.py

EN: Admin configuration for the "listings" app. Bilingual comments (EN/FR).
FR : Configuration de l'interface d'administration pour l'application "listings". Commentaires bilingues (EN/FR).
"""

from __future__ import annotations

# EN: Import Django's admin interface
# FR : Importation de l'interface d'administration Django
from django.contrib import admin

# EN: Import local models to register them in the admin site
# FR : Importation des modèles locaux pour les enregistrer dans le site d'administration
from listings.models import Band, Listing


# ========================================
#  Register models / Enregistrement modèles
# ========================================

# EN: Register Band model so it appears in the Django admin
# FR : Enregistrer le modèle Band pour qu'il apparaisse dans l'admin Django
admin.site.register(Band)

# EN: Register Listing model so it appears in the Django admin
# FR : Enregistrer le modèle Listing pour qu'il apparaisse dans l'admin Django
admin.site.register(Listing)
