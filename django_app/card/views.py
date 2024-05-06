import random
from card.models import Card 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import CardForm

@login_required(login_url="/admin/login/")
def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'qr_url.html', {'pk': form.instance.pk})
    else:
        form = CardForm()
    return render(request, 'add.html', {'form': form})


@login_required(login_url="/admin/login/")
def show_card(request, pk):
    card_instance = get_object_or_404(Card, pk=pk)
    return render(request, 'show_card.html', {'card': card_instance})

@login_required(login_url="/admin/login/")
def send_card(request):
    # SOME LOGIC
    return render(request, 'send_card.html')

@login_required(login_url="/admin/login/")
def send_to_ceremeo(request, pk, step_number):
    card_instance = get_object_or_404(Card, pk=pk)
    if step_number in (1,2,3):
        phone_number = request.POST.get('phone_number')
        # need number validation

    if int(step_number) == 1:
        """
        SEND DO CEREMEO
            {
                "campaign_token": "{campaign_token}",
                "phone": phone_number
            }
 
        """ 
        return render(request, 'ceremeo_1.html', {'phone_number': phone_number, 'card': card_instance})
    
    elif int(step_number) == 2:
        first_last_name = request.POST.get('first_last_name')
        email = request.POST.get('email')
        company_name = request.POST.get('company_name')
        # need email validation
        """
        !!!SKORO DO CEREMEO TRZEBA WYSYŁAĆ IMIĘ I NAZWISKO OSOBNO 
        TO W BAZIE I FORMULARZU TEŻ POWINNO BYĆ OSOBNO

        SEND DO CEREMEO
            {
                "campaign_token": "{campaign_token}",
                "phone": phone_number,
                ....     
            }
 
        """ 
        return render(request, 'ceremeo_2.html', {'phone_number': phone_number, 'card': card_instance})
    
    elif int(step_number) == 3:
        date = request.POST.get('date')
        description = request.POST.get('description')
        """
        SEND DO CEREMEO
            {
                "campaign_token": "{campaign_token}",
                "phone": phone_number,
                ....     
            }
 
        """ 
        return render(request, 'ceremeo_3.html', {'card': card_instance, 'number': random.randint(1,8)})
    
    else:
        return render(request, 'ceremeo_3.html', {'card': card_instance, 'number': random.randint(1,8)})

