from django.shortcuts import render, redirect
from Contacto.forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):

    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            mnsj = form.cleaned_data["contenido"]
            mail = EmailMessage(
                "Mensaje de app de django",
                f"La persona {nombre} con el email {email} desea ponerse en contacto con usted.\n\n{mnsj}.",
                "",
                [],
            )
            try:
                mail.send()
                return redirect('/contacto/enviado/')
            except:
                return render(request, "contacto/contacto.html", {"error": "Ocurrio un error"})
    else:
        form = FormularioContacto()
    return render(request, "contacto/contacto.html", {"form":form})

def enviado(request):
    return render(request, 'contacto/enviado.html')
