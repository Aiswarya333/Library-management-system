from __future__ import unicode_literals
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import HttpResponse, redirect, render
from .models import Book, User
from .forms import BookForm
from django.shortcuts import get_object_or_404
import json





def index(request):
    return render(request, 'lib/index.html')


def update(request):
    return render(request,"lib/update.html")


def delete(request):
    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    data = {}
    download_id_array = request.POST.get('checked_array')
    final_array = json.loads(download_id_array)

    for id in final_array:
        obj=Book.objects.filter(id=id)
        obj.delete()
    data['error_flag'] = 0

    return HttpResponse(json.dumps(data), content_type="application/json")

   

def addbook(request):
    if request.method == 'POST':
        print('entryyyyyyyyyyyyy')
        form = BookForm(request.POST)
        if form.is_valid():
            author = request.POST.get('author')
            title = request.POST.get('title')
            published_date=request.POST.get('published_date')
            availability=request.POST.get('availability')
            print(author)
            p = Book(author=author, title = title, published_date = published_date,availability = availability)
            p.save()
            print('success!!!')
            return render(request, 'lib/final.html')
        else:
            return render(request, 'lib/final.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'lib/login.html', {'form': form})

def logins(request):
    return render(request, 'lib/login.html')




def button(request):
    set=Book.objects.all()
    context={
        "objects":set,
        "details":"List"
    }
    return render(request,"lib/button.html",context)
   





