from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Candidat


# Register your models here.

class CandidatAdmin(admin.ModelAdmin):
    list_display   = (	"nom_prenom",
						"email",
						"telephone",
						"age",
						"nb_annee_experience_data")

admin.site.register( Candidat ,	CandidatAdmin)