from django.shortcuts import render, redirect
from .forms import RegistrationForm
#from django.contrib.auth import logout



def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.created_by = request.user
            data.save()
            return redirect('/register/login/')

    else:
        form = RegistrationForm()
    
    context = {
        'form': form
    }
    return render(request, 'register/signup.html', context)



#def logout_view(request):
   # logout(request)
    #return redirect('/login/')
