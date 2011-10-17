from ModelForm.books.models import AuthorForm, Author
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def AuthorView(request):
    i = Author.objects.get(id=1)
    form = AuthorForm(instance=i)
    if request.method == 'POST':   
        form = AuthorForm(request.POST, instance=i)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bye/')
    return render_to_response('model.html',{'form':form})