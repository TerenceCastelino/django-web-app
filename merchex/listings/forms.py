"""
Module: listings/forms.py

EN: Clean, commented Django forms for the "listings" app. All key comments are bilingual (EN/FR).
FR : Formulaires Django propres et commentés pour l'application "listings". Tous les commentaires clés sont bilingues (EN/FR).
"""

from __future__ import annotations

# EN: Import Django's form base classes
# FR : Importation des classes de base des formulaires Django
from django import forms

# EN: Import local models to build ModelForms
# FR : Importation des modèles locaux pour construire les ModelForms
from listings.models import Band, Listing


# ==================================
#  Contact form / Formulaire contact
# ==================================
class ContactUsForm(forms.Form):
    """
    EN: Basic contact form (not linked to a model).
    FR : Formulaire de contact basique (non lié à un modèle).
    """

    # EN: Optional name field
    # FR : Champ nom optionnel
    name = forms.CharField(required=False)

    # EN: Required email field
    # FR : Champ email requis
    email = forms.EmailField()

    # EN: Message text, max 1000 chars
    # FR : Texte du message, max 1000 caractères
    message = forms.CharField(max_length=1000)


# ===============================
#  Band form / Formulaire de groupe
# ===============================
class BandForm(forms.ModelForm):
    """
    EN: Form bound to the Band model.
    FR : Formulaire lié au modèle Band.
    """

    class Meta:
        model = Band
        # EN: Include all fields except 'active' and 'official_homepage'
        # FR : Inclure tous les champs sauf 'active' et 'official_homepage'
        exclude = ("active", "official_homepage")


# ====================================
#  Listing form / Formulaire d'annonce
# ====================================
class ListingForm(forms.ModelForm):
    """
    EN: Form bound to the Listing model.
    FR : Formulaire lié au modèle Listing.
    """

    class Meta:
        model = Listing
        # EN: Use all fields from the Listing model
        # FR : Utiliser tous les champs du modèle Listing
        fields = "__all__"
