from django import template
from bookapi.models import Rate
from django.db.models import Avg

register = template.Library()
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return False
def haselem(value,arg):
#    return True
   # print("CALLED!!!!!!!!!!!!!!!!!!111")
    return bool(value.users_likes.filter(pk=arg) )
@register.filter
def isread(value,arg):
#    return True
   # print("CALLED!!!!!!!!!!!!!!!!!!111")
    return bool(value.users_read.filter(pk=arg) )
@register.filter
def iswished(value,arg):
#    return True
   # print("CALLED!!!!!!!!!!!!!!!!!!111")
    return bool(value.users_wishes.filter(pk=arg) )
@register.filter
def aggregaterate(value):

    rate=Rate.objects.filter(book_id=value.id).aggregate(Avg('rate'))['rate__avg']
    if rate:
        return rate
    else:
        return "-"
    return bool(value.users_wishes.filter(pk=arg) )
@register.filter
def israted(value,arg):
    return bool(value.users_rated.filter(pk=arg) )
#    return True
   # print("CALLED!!!!!!!!!!!!!!!!!!111")
@register.filter
def followed(value,arg):
    return bool(value.user_set.filter(pk=arg) ) 
    

@register.filter
def favourited(value,arg):
    return bool(value.user_set.filter(pk=arg) ) 

register.filter('haselem', haselem)