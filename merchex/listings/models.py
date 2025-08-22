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
    FR : Représente un groupe de musique (genre, biographie, statut d'activité, site officiel).
         Préconditions : aucune. Champs clés : name, genre, year_formed, active, official_page.
         Erreurs : contraintes de validation (Min/Max sur year_formed, choix sur genre).
    EN : Represents a music band (genre, bio, active status, official site).
         Preconditions: none. Key fields: name, genre, year_formed, active, official_page.
         Errors: validation constraints (Min/Max on year_formed, choices on genre).
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

    # EN: Genre with predefined choices (default = Hip-Hop)
    # FR : Genre avec choix prédéfinis (défaut = Hip-Hop)
    genre = models.CharField(
        choices=Genre.choices,
        max_length=5,
        default=Genre.HIP_HOP,
    )

    # EN: Short biography (optional)
    # FR : Biographie courte (optionnelle)
    biography = models.CharField(max_length=1000, null=True, blank=True)

    # EN: Year formed, validated within [1900, 2100]
    # FR : Année de formation, validée dans [1900, 2100]
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
        default=2000,
    )

    # EN: Whether the band is currently active
    # FR : Indique si le groupe est actuellement actif
    active = models.BooleanField(default=True)

    # EN: Optional official website
    # FR : Site officiel (optionnel)
    official_page = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        """
        FR : Représentation lisible (admin, shell). Retour : « name (year_formed) ».
        EN : Human-readable representation (admin, shell). Returns: "name (year_formed)".
        """
        return f"{self.name} ({self.year_formed})"


# ====================================
#  Listing model / Modèle d'annonce
# ====================================
class Listing(models.Model):
    """
    FR : Représente une annonce de merchandising (disques, vêtements, posters, etc.).
         Préconditions : aucune. Champs clés : title, description, sold, year, official_page, type, band.
         Erreurs : contraintes de validation (Min/Max sur year, choix sur type).
    EN : Represents a merchandise listing (records, clothing, posters, etc.).
         Preconditions: none. Key fields: title, description, sold, year, official_page, type, band.
         Errors: validation constraints (Min/Max on year, choices on type).
    """

    # EN: Inner class for item type choices
    # FR : Classe interne pour les choix de type d'article
    class Type(models.TextChoices):
        RECORDS = "R", "Records"
        CLOTHING = "C", "Clothing"
        POSTERS = "P", "Posters"
        MISC = "M", "Miscellaneous"

    # EN: Title (max 100 chars)
    # FR : Titre (max 100 caractères)
    title = models.CharField(max_length=100)

    # EN: Short description (max 400 chars)
    # FR : Courte description (max 400 caractères)
    description = models.CharField(max_length=400)

    # EN: Whether the item has been sold (default True as provided)
    # FR : Indique si l'article est vendu (défaut True, conservé tel quel)
    sold = models.BooleanField(default=True)

    # EN: Year of the item (optional; validated within [1800, 2100])
    # FR : Année de l'article (optionnelle ; validée dans [1800, 2100])
    year = models.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2100)],
        null=True,
        blank=True,
    )

    # EN: Optional external link (e.g., product page)
    # FR : Lien externe optionnel (ex. page produit)
    official_page = models.URLField(null=True, blank=True)

    # EN: Item type (records, clothing, etc.)
    # FR : Type d'article (disques, vêtements, etc.)
    type = models.CharField(
        choices=Type.choices,
        max_length=2,
        default=Type.MISC,
    )

    # EN: Relation to a band (nullable; on band deletion set to NULL)
    # FR : Relation avec un groupe (nullable ; en cas de suppression du groupe → NULL)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        """
        FR : Représentation lisible (admin, shell). Retour : « title (type lisible) ».
        EN : Human-readable representation (admin, shell). Returns: "title (human-readable type)".
        """
        return f"{self.title} ({self.get_type_display()})"
