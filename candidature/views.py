from django.shortcuts import render
from .forms import CandidatForm

# Create your views here.
def candidater(request):
	template_create 	= "candidater.html"
	template_success 	= "merci.html"
	template_error 		= "error.html"
	form     = CandidatForm(request.POST or None)

	if request.method == "GET":
		print ("request.method")
		print (request.method)
		return render(request, template_create, locals())

	if request.method == "POST":
		if form.is_valid():
			form.save()
			return render(request, template_success, locals())
	return render(request, template_error, locals())