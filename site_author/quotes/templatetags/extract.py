from django import template

from ..utils import get_mongodb
from ..models import Author, AuthorAdd, QuoteAdd
from bson.objectid import ObjectId
register = template.Library()


def get_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']


register.filter('get_author', get_author)


def transition_do_db(id_):
    db = get_mongodb()
    author_mongo = db.authors.find_one({'_id': ObjectId(id_)})
    fullname = author_mongo["fullname"]
    authors = Author.objects.filter().all()
    for a in authors:
        if fullname == a.fullname:
            return a.id


register.filter('transition', transition_do_db)


def link_author(id_):
    authors = Author.objects.filter({'id': id_}).all()
    for a in authors:
        c = a.fullname.replace(" ", "-").replace("'", "").replace("é", "e").replace(".", "-").replace("--", "-")
        if c.endswith("-"):
            x = c.rfind("-")
            y = c[:x]
            return y
        return c


register.filter('author_link', link_author)


def search_author(author):
    authors_db = AuthorAdd.objects.all()
    quotes_db = QuoteAdd.objects.filter({'author': author})
    for au in authors_db:
        if quotes_db == au.name:
            return au.name


register.filter('search_author', search_author)
