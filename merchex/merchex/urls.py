"""
EN: Clean, commented Django URL configuration. All comments are bilingual (EN/FR).
FR : Fichier de configuration des URLs Django, propre et commenté en anglais et en français.
"""

from __future__ import annotations

# EN: Django imports for URL routing and admin site
# FR : Importations Django pour le routage des URLs et le site d'administration
from django.contrib import admin
from django.urls import path

# EN: Local views import (all views from listings app)
# FR : Importation des vues locales (toutes les vues de l'app listings)
from listings import views


# ======================================
#  URL patterns / Définition des routes
# ======================================

urlpatterns = [
    # EN: Django admin interface
    # FR : Interface d'administration Django
    path("admin/", admin.site.urls),

    # --------------------------
    # Bands URLs / URLs des groupes
    # --------------------------

    # EN: List all bands
    # FR : Lister tous les groupes
    path("bands/", views.band_list, name="bands"),

    # EN: Create a new band
    # FR : Créer un nouveau groupe
    path("bands/add/", views.band_create, name="band-create"),

    # EN: Band detail by id
    # FR : Détails d'un groupe par id
    path("bands/<int:id>/", views.band_detail, name="band-detail"),

    # EN: Update an existing band by id
    # FR : Mettre à jour un groupe existant par id
    path("bands/<int:id>/change/", views.band_update, name="band-update"),

    # -----------------------------
    # Listings URLs / URLs des annonces
    # -----------------------------

    # EN: List all listings
    # FR : Lister toutes les annonces
    path("listings/", views.listings, name="listings"),

    # EN: Create a new listing
    # FR : Créer une nouvelle annonce
    path("listings/add/", views.listing_create, name="listing_create"),

    # EN: Detail page for a single listing (lookup by id, required argument)
    # FR : Page de détail pour une annonce (recherche par id, argument requis)
    path("listings/<int:id>/", views.listing_detail, name="listing_detail"),

    # -----------------------------
    # Static pages / Pages statiques
    # -----------------------------

    # EN: About us page
    # FR : Page "À propos"
    path("about-us/", views.about, name="about"),

    # EN: Contact form page
    # FR : Page de contact
    path("contact-us/", views.contact, name="contact"),


    path("listings/<int:id>/change/", views.listing_update, name="listing_update"),
    path("bands/<int:id>/delete/", views.band_delete, name="band-delete"),
    path("listings/<int:id>/delete/", views.listing_delete, name="listing_delete"),
]

