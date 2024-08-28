from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import Utilisateur

class UtilisateurCreationForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ('pseudo',)

class UtilisateurChangeForm(UserChangeForm):
    class Meta:
        model = Utilisateur
        fields = ('pseudo',)