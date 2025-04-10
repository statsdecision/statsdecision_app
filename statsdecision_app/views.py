from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, Evenement, Document
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import VideoForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import MessageContact
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import MessageContact
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



from django.shortcuts import render
from .models import Video, Document, ImportantLink

def resource_center(request):
    return render(request, 'video_list.html', {
        'videos': Video.objects.all(),
        'documents': Document.objects.all().select_related('category'),
        'links': ImportantLink.objects.all()
    })

from django.shortcuts import render
from .models import Document, Category

def document_list(request):
    return render(request, 'documents.html', {
        'documents': Document.objects.all().select_related('category'),
        'categories': Category.objects.all()
    })

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = VideoForm()

    videos = Video.objects.all()  #  Récupère toutes les vidéos enregistrées
    return render(request, 'upload_video.html', {'form': form, 'videos': videos})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')  # Rediriger vers une page d'accueil ou un tableau de bord
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "connexion réussie ! Veuillez vous connecter.")
            return redirect('home')  # Redirige vers la page d'accueil ou autre
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def Evennement(request):
    Evennements=Evenement.objects.all()
    return render(request, 'Evennement.html', {'Evennements': Evennements})

def document(request):
    document=Document.object.all()
    return render(request, "video_list" , {'document': document})


@login_required
def profile_view(request):
    return render(request, 'profile.html', {
        'user': request.user
    })

# Vue pour le formulaire de demande de réinitialisation
class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    html_email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

# Vue après l'envoi de l'email
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

# Vue pour la confirmation du nouveau mot de passe
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

# Vue après réinitialisation réussie
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'




def contact_view(request):
    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        consentement = request.POST.get('consentement') == 'on'  # Si la case est cochée

        # Validation de l'email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Email invalide.")
            return redirect('contact')  # Rediriger vers la page de contact avec le message d'erreur
        
        # Validation des autres champs
        if not prenom or not nom or not sujet or not message or not consentement:
            messages.error(request, "Veuillez remplir tous les champs obligatoires et accepter les conditions.")
            return redirect('contact')  # Rediriger vers la page de contact avec le message d'erreur
        
        # Créez une nouvelle instance du modèle MessageContact
        new_message = MessageContact(
            prenom=prenom,
            nom=nom,
            email=email,
            sujet=sujet,
            message=message,
            consentement=consentement
        )

        # Enregistrez le message dans la base de données
        new_message.save()

        # Message de succès pour l'utilisateur sur le site
        messages.success(request, "Votre message a été envoyé avec succès. Nous vous contacterons bientôt.")

        # Envoi d'un e-mail de confirmation à l'utilisateur
        subject = "Confirmation de réception de votre message"
        message_body = f"Bonjour {prenom} {nom},\n\nMerci d'avoir pris contact avec nous. Nous avons bien reçu votre message concernant '{sujet}'. Nous reviendrons vers vous dès que possible.\n\nCordialement,\nL'équipe StatDecision Consulting"
        from_email = "kaborealphonse75@gmail.com"
        recipient_list = [email]

        send_mail(subject, message_body, from_email, recipient_list)

        # Rediriger vers la page de contact après l'envoi du message
        return redirect('contact')  # Vous pouvez également rediriger vers une page de remerciement

    return render(request, 'contact.html')





