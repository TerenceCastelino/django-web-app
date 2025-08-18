from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH', 'Hip-Hop'
        SYNTH_POP = 'SP', 'Synth Pop'
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'
        JAZZ = 'JZ', 'Jazz'
        METAL = 'MT', 'Metal'

    name = models.CharField(max_length=100)

    # Champ avec choix limités
    genre = models.CharField(choices=Genre.choices, max_length=5, default=Genre.HIP_HOP)

    # Champ texte plus long
    biography = models.CharField(max_length=1000, null=True, blank=True)

    # Année de formation avec contraintes
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
        default=2000
    )

    # Groupe actif ou non
    active = models.BooleanField(default=True)

    # ✅ URL facultative pour le site officiel
    official_page = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.year_formed})"


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'R', 'Records'
        CLOTHING = 'C', 'Clothing'
        POSTERS = 'P', 'Posters'
        MISC = 'M', 'Miscellaneous'

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=400)

    sold = models.BooleanField(default=True)

    year = models.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2100)],
        null=True,
        blank=True
    )

    # ✅ Nouvelle colonne pour un lien externe
    official_page = models.URLField(null=True, blank=True)

    # ✅ Champ type (avec choix limités)
    type = models.CharField(
        choices=Type.choices,
        max_length=2,
        default=Type.MISC
    )

    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"
