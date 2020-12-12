from django.shortcuts import render
from .models import Contact,Rate

def homepage(request):
	
	r = Rate.objects.all()
	# empty = []
	# c = Rate.objects.values()
	if request.method=="POST":
		name = request.POST.get('name', '')
		tel = request.POST.get('tel', '')
		email = request.POST.get('email', '')
		message = request.POST.get('message', '')
		contact = Contact(name=name, tel=tel, email=email, message=message)
		contact.save()
	return render(request, 'index.html')


def Zoo(request):
    return render(request, 'Chamarajendra.html')

def Palace(request):
    return render(request, 'PALACE.html')

def Hills(request):
    return render(request, 'Chamundi.html')

def Gardens(request):
    return render(request, 'Brindavan.html')
