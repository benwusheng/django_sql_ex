from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from users.forms import BookForm
from users.models import BookInfo


class BookView(View):

    def get(self,request):
        data={
            'title':'网页标题',
            'book_list':BookInfo.objs.all().order_by('-id'),
            'form':BookForm()
        }

        return render(request,'index.html',data)

    def post(self,request):

        form=BookForm(request.POST)

        print(form.is_valid())

        if form.is_valid():
            print(request.POST)
            print(form.cleaned_data)

            books = BookInfo(
                btitle=form.cleaned_data['title'],
                bpub_date=form.cleaned_data['pub_date']
            )

            books.save()

            return render(request,'index.html',{'form':form})
        else:
            return render(request,'index.html',{'form':form})

class TemplateView(View):
    def get(self,request):
        data={

        }

        return render(request,'list.html',data)
