from ModelForm.books.models import AuthorForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def AuthorView(request):
    form = AuthorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bye/')
    return render_to_response('model.html',{'form':form})