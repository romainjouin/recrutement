from django 	import forms
from .models 	import Candidat
from django.core.validators import MinValueValidator, MaxValueValidator

def get_Integerfield(label, min, max):
	attrs	=	{'min': min, 
				 'max': max}
	widget	=	forms.NumberInput(attrs=attrs)
	result 	= 	forms.IntegerField(widget =widget )
	return result

def get_Charfield(label, widget):
	error 		= ""
	max_length 	= 500
	result 		= forms.CharField(	label 			= label 	,
									widget 			= widget	,
									max_length     	= max_length,
			       					error_messages 	= error  	)
	return result

def get_TextField(label, placeholder):
	classe 	=	'form-control'
	attrs 	= {	'class'			: classe		,
				'placeholder'	: placeholder	}
	widget 	= forms.TextInput(attrs)
	return get_Charfield(label, widget)


def get_Textarea(label, placeholder):
	n_rows 	= 4
	classe 	= 'form-control'
	attrs 	=	{ 	'rows' 			: n_rows		,
					'class'			: classe	 	,
					'placeholder' 	: placeholder	}
	widget	= forms.Textarea(attrs=attrs)

	return get_Charfield(label, widget)

class CandidatForm(forms.ModelForm):
	class Meta:
		model  =  Candidat
		fields = (	"nom_prenom",	"email",	"telephone",
					"nb_annee_experience_data", "age", 
					"meilleur_experience", "point_clef_sur_l_offre")

	nom_prenom					= get_TextField("Identité "	, " Nom, prénom." 					)
	email						= get_TextField("E-mail " 		, "example@gmail.com"				)  
	telephone 					= get_TextField("Téléphone "	, ""							)
	meilleur_diplome 			= get_Textarea("Meilleur diplôme pour le poste "	, "Votre diplôme qui vous semble le plus pertinent."	)
	meilleur_experience	 		= get_Textarea("Meilleure expérience pour le poste"	, "Votre expérience qui répond le mieux aux enjeux du poste."	)
	age 						= get_Integerfield("Age", 18,70)
	nb_annee_experience_data 	= get_Integerfield("Age", 0, 20)
	point_clef_sur_l_offre		= get_Textarea("Atout majeur pour le poste"	, "Pourquoi vous plutôt qu'un autre ?  "	)
	#nb_annee_experience_data = get_CharField("Meilleur diplôme : "	, "Meilleur diplôme pour le poste "	)