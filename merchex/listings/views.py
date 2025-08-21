"""
EN: Clean, commented Django views for the "listings" app. All key comments are bilingual (EN/FR).
FR : Vues Django propres et commentées pour l'application "listings". Tous les commentaires clés sont bilingues (EN/FR).
"""

from __future__ import annotations

# EN: Standard library imports (none needed here)
# FR : Importations de la bibliothèque standard (aucune nécessaire ici)

# EN: Django imports
# FR : Importations Django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# EN: Local app imports (models and forms from this app)
# FR : Importations locales de l'app (modèles et formulaires de cette app)
from listings.forms import BandForm, ContactUsForm, ListingForm
from listings.models import Band, Listing


# ==========================
#  Contact view / Vue contact
# ==========================

def contact(request: HttpRequest) -> HttpResponse:
    """
    EN: Handle the contact form: display on GET, validate and send email on POST.
    FR : Gère le formulaire de contact : affichage en GET, validation et envoi d'email en POST.
    """
    if request.method == "POST":
        # EN: Bind POST data to the form
        # FR : Lier les données POST au formulaire
        form = ContactUsForm(request.POST)

        if form.is_valid():
            # EN: Send the email using validated/cleaned data
            # FR : Envoyer l'email en utilisant les données validées/nettoyées
            send_mail(
                subject=(
                    f"Message from {form.cleaned_data['name'] or 'anonyme'} "
                    "via MerchEx Contact Us form"
                ),
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            # EN: After success, redirect to the bands list page
            # FR : Après succès, rediriger vers la page de liste des groupes
            return redirect("bands")
    else:
        # EN: GET request ⇒ instantiate an empty form
        # FR : Requête GET ⇒ instancier un formulaire vide
        form = ContactUsForm()

    # EN: Render the contact template with the form (bound or unbound)
    # FR : Rendre le template de contact avec le formulaire (lié ou non)
    return render(request, "listings/contact.html", {"form": form})


# ==============================
#  Bands list / Liste des groupes
# ==============================

def band_list(request: HttpRequest) -> HttpResponse:
    """
    EN: Display all bands.
    FR : Affiche tous les groupes.
    """
    # EN: Query all Band instances (consider pagination for large datasets)
    # FR : Récupérer toutes les instances Band (penser à la pagination pour de gros volumes)
    bands = Band.objects.all()

    # EN: Render the list template with the queryset
    # FR : Rendre le template de liste avec le queryset
    return render(request, "listings/band_list.html", {"bands": bands})


# ======================
#  About view / À propos
# ======================

def about(request: HttpRequest) -> HttpResponse:
    """
    EN: Static "About us" page.
    FR : Page statique "À propos".
    """
    return render(request, "listings/about.html")


# ========================================
#  Listings list / Liste des annonces
# ========================================

def listings(request: HttpRequest) -> HttpResponse:
    """
    EN: Display all listings.
    FR : Affiche toutes les annonces.
    """
    # EN: Query all Listing instances
    # FR : Récupérer toutes les instances Listing
    items = Listing.objects.all()

    return render(request, "listings/listings.html", {"listings": items})


# ==============================
#  Band detail / Détails d'un groupe
# ==============================

def band_detail(request: HttpRequest, id: int) -> HttpResponse:
    """
    EN: Display details for a single band by id. 404 if not found.
    FR : Affiche les détails d'un groupe par id. 404 si non trouvé.
    """
    # EN: Safer than Band.objects.get(id=id) ⇒ raises 404 automatically
    # FR : Plus sûr que Band.objects.get(id=id) ⇒ lève 404 automatiquement
    band = get_object_or_404(Band, id=id)

    return render(request, "listings/band_detail.html", {"band": band})


# ============================
#  Band create / Création groupe
# ============================

def band_create(request: HttpRequest) -> HttpResponse:
    """
    EN: Create a new Band. On success, redirect to its detail page.
    FR : Crée un nouveau Band. En cas de succès, redirige vers sa page de détails.
    """
    if request.method == "POST":
        # EN: Bind POST data to the form
        # FR : Lier les données POST au formulaire
        form = BandForm(request.POST)
        if form.is_valid():
            # EN: Save and get the newly created band instance
            # FR : Sauvegarder et récupérer l'instance nouvellement créée
            band = form.save()
            # EN: Redirect to the band detail page using URL name 'band-detail'
            # FR : Rediriger vers la page de détail en utilisant le nom d'URL 'band-detail'
            return redirect("band-detail", id=band.id)
    else:
        # EN: Render an empty form on GET
        # FR : Rendre un formulaire vide en GET
        form = BandForm()

    return render(request, "listings/band_create.html", {"form": form})


# =====================================
#  Listing create / Création d'annonce
# =====================================

def listing_create(request: HttpRequest) -> HttpResponse:
    """
    EN: Create a new Listing. On success, redirect to the listings list.
    FR : Crée une nouvelle annonce. En cas de succès, redirige vers la liste des annonces.
    """
    if request.method == "POST":
        # EN: Bind POST data to the form
        # FR : Lier les données POST au formulaire
        form = ListingForm(request.POST)
        if form.is_valid():
            # EN: Save the listing; you could also redirect to a detail view if available
            # FR : Sauvegarder l'annonce ; on peut aussi rediriger vers une page de détail si elle existe
            listing = form.save()
            return redirect("listings")
    else:
        # EN: GET request ⇒ empty form
        # FR : Requête GET ⇒ formulaire vide
        form = ListingForm()

    return render(request, "listings/listing_create.html", {"form": form})


# ==================================
#  Band update / Mise à jour groupe
# ==================================

def band_update(request: HttpRequest, id: int) -> HttpResponse:
    """
    EN: Update an existing Band by id. On success, redirect to its detail page.
    FR : Met à jour un Band existant par id. En cas de succès, redirige vers sa page de détails.
    """
    # EN: Retrieve or 404 if not found
    # FR : Récupérer ou lever 404 si absent
    band = get_object_or_404(Band, id=id)

    if request.method == "POST":
        # EN: Bind POST data to the form with the instance to update
        # FR : Lier les données POST au formulaire avec l'instance à mettre à jour
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # EN: Save changes to the existing band
            # FR : Sauvegarder les modifications du groupe existant
            form.save()
            # EN: Redirect to the updated band's detail page
            # FR : Rediriger vers la page de détail du groupe mis à jour
            return redirect("band-detail", id=band.id)
    else:
        # EN: Pre-fill the form with the existing instance on GET
        # FR : Pré-remplir le formulaire avec l'instance existante en GET
        form = BandForm(instance=band)

    return render(request, "listings/band_update.html", {"form": form})
