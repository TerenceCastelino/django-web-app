"""
EN: Clean, commented Django models for the "listings" app. All key comments are bilingual (EN/FR).
FR : Modèles Django propres et commentés pour l'application "listings". Tous les commentaires clés sont bilingues (EN/FR).
"""

from __future__ import annotations

# EN: Import Django ORM base classes and field validators
# FR : Importation des classes de base de l'ORM Django et des validateurs de champs
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# ===============================
#  Band model / Modèle de groupe
# ===============================
class Band(models.Model):
    """
    EN: Represents a music band with genre, biography, and activity status.
    FR : Représente un groupe de musique avec genre, biographie et statut d'activité.
    """

    # EN: Inner class for genre choices
    # FR : Classe interne pour les choix de genre
    class Genre(models.TextChoices):
        HIP_HOP = "HH", "Hip-Hop"
        SYNTH_POP = "SP", "Synth Pop"
        ALTERNATIVE_ROCK = "AR", "Alternative Rock"
        JAZZ = "JZ", "Jazz"
        METAL = "MT", "Metal"

    # EN: Band name (max 100 chars)
    # FR : Nom du groupe (max 100 caractères)
    name = models.CharField(max_length=100)

    # EN: Genre field with predefined choices (default = Hip-Hop)
    # FR : Champ genre avec choix prédéfinis (par défaut = Hip-Hop)
    genre = models.CharField(
        choices=Genre.choices,
        max_length=5,
        default=Genre.HIP_HOP,
    )

    # EN: Biography text (optional)
    # FR : Texte de biographie (optionnel)
    biography = models.CharField(max_length=1000, null=True, blank=True)

    # EN: Year formed with validation constraints
    # FR : Année de formation avec contraintes de validation
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
        default=2000,
    )

    # EN: Whether the band is currently active
    # FR : Indique si le groupe est actuellement actif
    active = models.BooleanField(default=True)

    # EN: Optional URL for the band's official website
    # FR : URL facultative pour le site officiel du groupe
    official_page = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        # EN: String representation = name + year formed
        # FR : Représentation en chaîne = nom + année de formation
        return f"{self.name} ({self.year_formed})"


# ====================================
#  Listing model / Modèle d'annonce
# ====================================
class Listing(models.Model):
    """
    EN: Represents a listing of merchandise items (records, posters, clothing, etc.).
    FR : Représente une annonce d'articles de merchandising (disques, posters, vêtements, etc.).
    """

    # EN: Inner class for type choices
    # FR : Classe interne pour les choix de type
    class Type(models.TextChoices):
        RECORDS = "R", "Records"
        CLOTHING = "C", "Clothing"
        POSTERS = "P", "Posters"
        MISC = "M", "Miscellaneous"

    # EN: Title of the listing (max 100 chars)
    # FR : Titre de l'annonce (max 100 caractères)
    title = models.CharField(max_length=100)

    # EN: Short description (max 400 chars)
    # FR : Courte description (max 400 caractères)
    description = models.CharField(max_length=400)

    # EN: Whether the item has been sold
    # FR : Indique si l'article est vendu
    sold = models.BooleanField(default=True)

    # EN: Year of the item (optional, with validation)
    # FR : Année de l'article (optionnelle, avec validation)
    year = models.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2100)],
        null=True,
        blank=True,
    )

    # EN: Optional external link (e.g., product page)
    # FR : Lien externe optionnel (ex. page produit)
    official_page = models.URLField(null=True, blank=True)

    # EN: Type of item (records, clothing, etc.)
    # FR : Type d'article (disques, vêtements, etc.)
    type = models.CharField(
        choices=Type.choices,
        max_length=2,
        default=Type.MISC,
    )

    # EN: Relation to a band (nullable, if band deleted → set null)
    # FR : Relation avec un groupe (nullable, si groupe supprimé → set null)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        # EN: String representation = title + human-readable type
        # FR : Représentation en chaîne = titre + type lisible
        return f"{self.title} ({self.get_type_display()})"
