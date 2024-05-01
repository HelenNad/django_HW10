from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.

from .utils import get_mongodb
from .models import Author, AuthorAdd, QuoteAdd
from .forms import AuthorForm, QuoteForm


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    authors_add_in_bd = AuthorAdd.objects.all()
    quotes_add_in_bd = QuoteAdd.objects.all()
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page,
                                                         'authors_add_in_bd': authors_add_in_bd,
                                                         'quotes_add_in_bd': quotes_add_in_bd})


def description_auth(request, id_):
    authors = Author.objects.filter(pk=id_).all()
    return render(request, template_name='quotes/descript_author.html', context={'authors': authors})


def auth_ur(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})


def quote_ur(request):
    author = AuthorAdd.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_author = AuthorAdd.objects.filter(name__in=request.POST.getlist('author'))
            for aut in choice_author.iterator():
                new_quote.author.add(aut)

            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_quote.html', {"author": author, 'form': form})

    return render(request, 'quotes/add_quote.html', {"author": author, 'form': QuoteForm()})

