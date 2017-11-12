from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# a semple request you will get with some data  >> POST as defined in HTML FILE " index.html "
def index (request):
    formData = {}
    if request.method == 'POST':
        #get your request data
        name = str(request.POST.get('name'))
        from_email =str(request.POST.get('email'))
        message = str(request.POST.get('comments'))
        phone = str(request.POST.get('phone'))
        #save them as dict to use them
        formData = {
            'name' : name ,
            'email' : from_email,
            'message' : message,
            'phone' : phone,

            }

        try:
            #use the mail library and send your data to the mail
            send_mail(name, message +"\n via " +from_email, from_email, ['test199651@gmail.com',],fail_silently=True)

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        #redirect to success method
        return redirect('success')

    return render(request, "index.html", context={'form': formData})


def success (request):
    return render(request ,'success.html')
