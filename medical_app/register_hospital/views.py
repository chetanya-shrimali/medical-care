from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from register_hospital.forms import HospitalForm
from register_hospital.models import Hospital


def login(request):
    return HttpResponse("Login")


def validate(request, pk):
    detail = Hospital.objects.get(pk=pk)
    user = User(username=detail.name, password=detail.password,
                email=detail.email, pk=pk)
    return HttpResponse("You have been validated successfully!!")


class SignUpFormView(View):
    form_class = HospitalForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(self.request.user)
        if form.is_valid():
            note = form.save(commit=False)
            name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            password = form.cleaned_data['password']
            license_id = form.cleaned_data['license_id']
            link = "localhost:8000/register/" + str(form.id) + "validate/"
            print(link)
            form.save()

            if note is not None:
                email = EmailMessage('Confirmation Mail from Medi-care',
                                     "Hey " + name + "\n\n"
                                                     "Please Click the link "
                                                     "below to confirm" +
                                     "\n" +
                                     link,
                                     to=['chetanyashrimalie5@gmail.com',
                                         'nkchoudhary696@gmail.com'])
                email.send()

                # email = EmailMessage('Regarding feedback', "Hey " + name +
                #  ",\n\n" + "We have successfully recieved your note!!",
                # to=[email_address]) email.send()
                print('reached')
                return redirect('hospital_detail:details')
        return render(request, self.template_name, {'form': form})
