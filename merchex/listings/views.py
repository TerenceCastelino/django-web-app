"""
EN: Clean, commented Django views for the "listings" app. All key comments are bilingual (EN/FR).
FR : Vues Django propres et commentées pour l'application "listings". Tous les commentaires clés sont bilingues (EN/FR).
"""

from __future__ import annotations

# EN: Django imports
# FR : Importations Django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# EN: Local app imports (models and forms from this app)
# FR : Importations locales de l'app (modèles et formulaires de cette app)
from listings.forms import BandForm, ContactUsForm, ListingForm
from listings.models import Band, Listing


# ==============================
#           BAND (CRUD)
# ==============================

def band_create(request: HttpRequest) -> HttpResponse:
    """
    FR : Crée un nouveau Band et redirige vers son détail en cas de succès.
         Préconditions : méthode POST avec données valides (BandForm). Retour : HttpResponse (formulaire) ou redirection.
         Erreurs : validation formulaire (affiche le formulaire avec erreurs).
    EN : Create a new Band and redirect to its detail on success.
         Preconditions: POST with valid data (BandForm). Returns: HttpResponse (form) or redirect.
         Errors: form validation errors (form re-rendered).
    """
    if request.method == "POST":
        form = BandForm(request.POST)  # EN: bind POST data / FR : lier données POST
        if form.is_valid():
            band = form.save()  # EN/FR: persist instance
            return redirect("band-detail", id=band.id)  # EN: URL name used as provided / FR : nom d'URL tel quel
    else:
        form = BandForm()  # EN: empty form / FR : formulaire vide

    return render(request, "listings/band_create.html", {"form": form})


def band_list(request: HttpRequest) -> HttpResponse:
    """
    FR : Affiche la liste de tous les groupes.
         Préconditions : aucune. Retour : HttpResponse avec contexte {"bands"}.
         Erreurs : aucune (penser à la pagination si gros volume).
    EN : Display all bands.
         Preconditions: none. Returns: HttpResponse with {"bands"}.
         Errors: none (consider pagination for large datasets).
    """
    bands = Band.objects.all()  # EN: could paginate / FR : pagination possible
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request: HttpRequest, id: int) -> HttpResponse:
    """
    FR : Affiche les détails d'un groupe par id (404 si absent).
         Préconditions : id valide. Retour : HttpResponse avec contexte {"band"}.
         Erreurs : 404 si non trouvé.
    EN : Show a single band's details by id (404 if missing).
         Preconditions: valid id. Returns: HttpResponse with {"band"}.
         Errors: 404 when not found.
    """
    band = get_object_or_404(Band, id=id)  # EN/FR: safer retrieval (404 on miss)
    return render(request, "listings/band_detail.html", {"band": band})


def band_update(request: HttpRequest, id: int) -> HttpResponse:
    """
    FR : Met à jour un Band existant et redirige vers son détail.
         Préconditions : id existant, POST avec données valides. Retour : HttpResponse ou redirection.
         Erreurs : 404 si id invalide ; validation formulaire sinon.
    EN : Update an existing Band and redirect to its detail.
         Preconditions: existing id, POST with valid data. Returns: HttpResponse or redirect.
         Errors: 404 if invalid id; form validation otherwise.
    """
    band = get_object_or_404(Band, id=id)

    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect("band-detail", id=band.id)
    else:
        form = BandForm(instance=band)  # EN: pre-filled / FR : pré-rempli

    return render(request, "listings/band_update.html", {"form": form})


def band_delete(request, id):
    """
    FR : Supprime un Band après confirmation (POST), sinon affiche la page de confirmation.
         Préconditions : id existant. Retour : HttpResponse ou redirection vers la liste des groupes.
         Erreurs : Band.DoesNotExist si id invalide (non interceptée ici).
    EN : Delete a Band after POST confirmation; otherwise renders confirmation.
         Preconditions: existing id. Returns: HttpResponse or redirect to bands list.
         Errors: Band.DoesNotExist if invalid id (not handled here).
    """
    band = Band.objects.get(id=id)  # EN: used for both GET and POST / FR : utilisé pour GET et POST

    if request.method == 'POST':
        band.delete()
        return redirect('bands')  # EN: as provided / FR : tel quel

    return render(request, 'listings/band_delete.html', {'band': band})


# ===============================
#          LISTING (CRUD)
# ===============================

def listing_create(request: HttpRequest) -> HttpResponse:
    """
    FR : Crée une nouvelle annonce et redirige vers la liste (ou autre vue si souhaité).
         Préconditions : POST avec données valides (ListingForm). Retour : HttpResponse ou redirection.
         Erreurs : validation formulaire (ré-affichage avec erreurs).
    EN : Create a new Listing and redirect to the listings list (or a detail view if desired).
         Preconditions: POST with valid data (ListingForm). Returns: HttpResponse or redirect.
         Errors: form validation errors (re-rendered).
    """
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect("listings")  # EN/FR: route name kept as provided
    else:
        form = ListingForm()

    return render(request, "listings/listing_create.html", {"form": form})


def listings(request: HttpRequest) -> HttpResponse:
    """
    FR : Affiche toutes les annonces.
         Préconditions : aucune. Retour : HttpResponse avec contexte {"listings"}.
         Erreurs : aucune (penser pagination/tri).
    EN : Display all listings.
         Preconditions: none. Returns: HttpResponse with {"listings"}.
         Errors: none (consider pagination/sorting).
    """
    items = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings": items})


def listing_detail(request, id):
    """
    FR : Affiche le détail d'une annonce (404 si absente).
         Préconditions : id valide. Retour : HttpResponse avec contexte {"listing"}.
         Erreurs : 404 si non trouvée.
    EN : Show a single listing (404 if missing).
         Preconditions: valid id. Returns: HttpResponse with {"listing"}.
         Errors: 404 when not found.
    """
    listing = get_object_or_404(Listing, id=id)  # EN: safer retrieval / FR : récupération plus sûre
    return render(request, "listings/listing_detail.html", {"listing": listing})


def listing_update(request, id):
    """
    FR : Met à jour une annonce existante et redirige vers son détail.
         Préconditions : id existant, POST valide. Retour : HttpResponse ou redirection.
         Erreurs : 404 si id invalide ; erreurs de formulaire sinon.
    EN : Update an existing Listing and redirect to its detail.
         Preconditions: existing id, valid POST. Returns: HttpResponse or redirect.
         Errors: 404 if invalid id; form errors otherwise.
    """
    listing = get_object_or_404(Listing, id=id)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listing_detail", id=listing.id)  # EN/FR: name with underscore kept
    else:
        form = ListingForm(instance=listing)

    return render(request, "listings/listing_update.html", {"form": form})


def listing_delete(request, id):
    """
    FR : Supprime une annonce après confirmation (POST), sinon affiche la confirmation.
         Préconditions : id existant. Retour : HttpResponse ou redirection vers la liste des annonces.
         Erreurs : 404 si id invalide.
    EN : Delete a listing after POST confirmation; otherwise render the confirmation.
         Preconditions: existing id. Returns: HttpResponse or redirect to listings list.
         Errors: 404 if invalid id.
    """
    listing = get_object_or_404(Listing, id=id)

    if request.method == "POST":
        listing.delete()
        return redirect("listings")  # ← list route name kept

    return render(request, "listings/listing_delete.html", {"listing": listing})


# ==============================
#          PAGES / DIVERS
# ==============================

def about(request: HttpRequest) -> HttpResponse:
    """
    FR : Page statique « À propos ».
         Préconditions : aucune. Retour : HttpResponse simple.
         Erreurs : aucune.
    EN : Static "About" page.
         Preconditions: none. Returns: plain HttpResponse.
         Errors: none.
    """
    return render(request, "listings/about.html")


def contact(request: HttpRequest) -> HttpResponse:
    """
    FR : Gère le formulaire de contact : affichage en GET, validation + envoi d'email en POST.
         Préconditions : configuration d'email valide (Django). Retour : HttpResponse ou redirection vers la liste des groupes.
         Erreurs : erreurs de formulaire ; erreurs d'envoi email si configuration invalide.
    EN : Handle the contact form: show on GET, validate + send email on POST.
         Preconditions: valid email backend configuration. Returns: HttpResponse or redirect to bands list.
         Errors: form errors; email send failures if misconfigured.
    """
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=(
                    f"Message from {form.cleaned_data['name'] or 'anonyme'} "
                    "via MerchEx Contact Us form"
                ),
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("bands")  # EN/FR: as provided
    else:
        form = ContactUsForm()

    return render(request, "listings/contact.html", {"form": form})
