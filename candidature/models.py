from django.db import models

# Create your models here.

class Candidat(models.Model):
	nom_prenom					=	models.CharField(max_length=500)
	email		 				=	models.CharField(max_length=500)	
	telephone					=	models.CharField(max_length=500)
	age							=	models.IntegerField()
	nb_annee_experience_data	=	models.IntegerField()
	meilleur_diplome 			=	models.CharField(max_length=500)
	meilleur_experience 		=	models.CharField(max_length=500)
	point_clef_sur_l_offre 		=	models.CharField(max_length=500)
	
	def __str__(self):
		return 'candidat : ' + self.nom_prenom