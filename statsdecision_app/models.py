# Create your models here.
from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()  # Utilisez cette méthode partout

# OU directement pour les relations :
user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# Mise à jour du modèle pour inclure des fichiers multimédias
class Evenement(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    organisateur = models.CharField(max_length=255)
    TYPE_CHOICES = [
        ('Conférence', 'Conférence'),
        ('Réunion', 'Réunion'),
        ('Formation', 'Formation'),
        ('Autre', 'Autre'),
    ]
    type_evenement = models.CharField(max_length=50, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='images_evenements/', blank=True, null=True)
   
    def __str__(self):
        return self.titre



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="documents")
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MessageContact(models.Model):
    # Informations de l'utilisateur
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    
    # Consentement pour utiliser les données
    consentement = models.BooleanField(default=False)

    # Date de création du message
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.prenom} {self.nom} - {self.sujet}"

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"





    # models.py
from django.db import models
from django.core.validators import URLValidator

class ImportantLinkCategory(models.Model):
    """Catégorie pour organiser les liens importants"""
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7, default='#3B82F6')  # Code couleur hexadécimal
    icon = models.CharField(max_length=50, default='fas fa-link')  # Classe d'icône Font Awesome
    
    class Meta:
        verbose_name = "Catégorie de lien"
        verbose_name_plural = "Catégories de liens"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class ImportantLink(models.Model):
    """Modèle pour stocker les liens importants"""
    title = models.CharField(max_length=200, verbose_name="Titre")
    url = models.URLField(max_length=500, validators=[URLValidator()], verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Description")
    category = models.ForeignKey(
        ImportantLinkCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Catégorie"
    )

    is_featured = models.BooleanField(default=False, verbose_name="À la une")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    created_by = models.ForeignKey(
        'auth.User', 
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name="Créé par"
    )
    
    # Statistiques
    click_count = models.PositiveIntegerField(default=0, verbose_name="Nombre de clics")
    last_clicked = models.DateTimeField(null=True, blank=True, verbose_name="Dernier clic")
    
    class Meta:
        verbose_name = "Lien important"
        verbose_name_plural = "Liens importants"
        ordering = ['-is_featured', 'title']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['category']),
            models.Index(fields=['is_featured']),
        ]
    
    def __str__(self):
        return f"{self.title} ({self.url})"
    
    