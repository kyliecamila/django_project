from django.urls import path
from manageApp import views
from .views import HomeView, DetailView, AddPostView, EditPostView,DeletePostView, AddCategoryView, CategoryView
from .views import BisanView, NewtownView, YungchangView, DuckheonView, HogaeView, ImgokView, MiryungView, OncheonView, SamsinView
from .views import NangcheonView, ArtView, NaesondaView, NaesonraView, GocheongaView, GocheonnaView, OjundaView, OjunnaView,AnyangstationView
from .views import SangrokView, HwachangView
urlpatterns = [
    path('', HomeView, name="home"),
    path('article/<int:pk>', DetailView.as_view(), name="detail"),
    path('add_post/', AddCategoryView.as_view(), name ='add_category'),
    path('add_category/', AddPostView.as_view(), name ='add_post'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name ='edit_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name ='delete_post'),
    path('category/<str:cats>/', CategoryView, name = 'category' ),

    path('bisan', BisanView, name="bisan"),
    path('newtown', NewtownView, name="newtown"),
    path('yungchang', YungchangView, name="yungchang"),
    path('duckheon', DuckheonView, name="duckheon"),
    path('hogae', HogaeView, name="hogae"),
    path('imgok', ImgokView, name="imgok"),
    path('miryung', MiryungView, name="miryung"),
    path('oncheon', OncheonView, name="oncheon"),
    path('samsin', SamsinView, name="samsin"),
    path('nangcheon', NangcheonView, name="nangcheon"),
    path('art', ArtView, name="art"),
    path('naesonda', NaesondaView, name="naesonda"),
    path('naesonra', NaesonraView, name="naesonra"),
    path('gocheonga', GocheongaView, name="gocheonga"),
    path('gocheonna', GocheonnaView, name="gocheonna"),
    path('ojunda', OjundaView, name="ojunda"),
    path('ojunna', OjunnaView, name="ojunna"),
    path('anyangstation', AnyangstationView, name="anyangstation"),
    path('sangrok', SangrokView, name="sangrok"),
    path('hwachang', HwachangView, name="hwachang"),
   
]
