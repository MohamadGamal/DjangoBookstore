from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^signin', views.signin, name='signin'),
     url(r'^add$', views.AddUserView.as_view(), name="addbook"),
     url(r'^home', views.realhome, name='home'),
      url(r'^fakehome', views.home, name='fhome'),
      url(r'^test', views.test, name='test'),
        url(r'^books', views.books, name='books'),
         url(r'^authors', views.authors, name='authors'),
           url(r'^notifications', views.notlist, name='notifications'),
         url(r'^categories', views.categories, name='categories'),
 url(r'^favourites', views.favlist, name='favourites'),
         url(r'^author/(?P<author_id>[0-9]+)/books', views.bauthors, name='authourbooks'),
         url(r'^category/(?P<category_id>[0-9]+)/books', views.bcategs, name='categorybooks'),
  url(r'^logout', views.logout, name='logout'),
        url(r'^srvice', views.servicebooks, name='srvcbooks'),
        url(r'^service/like/(?P<book_id>[0-9]*)', views.likebook),
        url(r'^service/wish/(?P<book_id>[0-9]*)', views.wishesbook),
        url(r'^service/read/(?P<book_id>[0-9]*)', views.readbook),
        url(r'^service/rate/(?P<book_id>[0-9]*)', views.ratesbook),
        url(r'^service/follow/(?P<author_id>[0-9]*)', views.followauthor),
        url(r'^service/favourites/(?P<category_id>[0-9]*)', views.favouritecategory),

]
