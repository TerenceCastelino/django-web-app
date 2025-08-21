from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render,redirect

from listings.models import Band, Listing

from listings.forms import ContactUsForm,BandForm,ListingForm

from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('bands')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
            'listings/contact.html',
            {'form': form})

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    items = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': items})

# def contact_us(request):
#     return render(request, 'listings/contact.html')

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def band_detail(request, id):
    band = get_object_or_404(Band, id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

# def band_create(request):
#     return render(request, 'listings/band_create.html')

# listings/views.py

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            
            listing = form.save()
           
            # return redirect('band-detail', band.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})
