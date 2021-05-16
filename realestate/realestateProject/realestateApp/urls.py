from django.urls import path
# from .import views
from .views import HomeView, DetailView, AddView, EditView, DeleteView,CategoryView
from .views import AddMemoView,DeleteMemoView,EditMemoView
from .views import BisanView, YungchangView, DuckheonView, HogaeView, ImgokView, MiryungView, OncheonView, SamsinView
from .views import NangcheonView, ArtView, NaesondaView, NaesonraView, GocheongaView, GocheonnaView, OjundaView, OjunnaView,AnyangstationView
from .views import SangrokView, HwachangView,NewtownoneView,NewtownfourView
from .views import NewtownfiveView,NewtownsixView
urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView, name="home"),
    path('article/<int:pk>', DetailView.as_view(), name="detail"),
    path('add/', AddView.as_view(), name="add"),
    path('article/edit/<int:pk>', EditView.as_view(), name ='edit'),
    path('article/<int:pk>/delete', DeleteView.as_view(), name ='delete'),
    path('category/<str:cats>/', CategoryView, name = 'category' ),
    path('add_memo/', AddMemoView, name="add_memo"),
    path('delete_memo/<int:memo_pk>', DeleteMemoView, name="delete_memo"),
    path('edit_memo/<int:memo_pk>', EditMemoView, name="edit_memo"),

    path('bisan', BisanView, name="bisan"),
    path('newtown1', NewtownoneView, name="newtown1"),
    path('newtown4', NewtownfourView, name="newtown4"),
    path('newtown5', NewtownfiveView, name="newtown5"),
    path('newtown6', NewtownsixView, name="newtown6"),
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
    path('station', AnyangstationView, name="station"),
    path('sangrok', SangrokView, name="sangrok"),
    path('hwachang', HwachangView, name="hwachang"),
]
