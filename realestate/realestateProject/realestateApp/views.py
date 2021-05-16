from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Article, Category, Memo
from .forms import ArticleForm
from django.urls import reverse_lazy

def CategoryView(request, cats):
    category_articles = Article.objects.filter(district=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_articles':category_articles} )

def HomeView(request):
    my_articles = Article.objects.filter(owner='탑공인중개사')
    return render(request, 'home.html', {'my_articles':my_articles} )
   

class DetailView(DetailView):
    model = Article
    template_name = 'detail.html'

class AddView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name ='add.html'

def AddMemoView(request):
    if request.method =='POST':
        new_memo = Memo.objects.create(
            district = request.POST['district'],
            district_memo = request.POST['district_memo'],
          
        )
        return redirect('home')
    return render(request, 'add_memo.html')

def DeleteMemoView(request, memo_pk):
    memo = Memo.objects.get(pk=memo_pk)
    memo.delete()
    return redirect('home')

def EditMemoView(request, memo_pk):
    memo = Memo.objects.get(pk=memo_pk)
    if request.method =='POST':
        Memo.objects.filter(pk=memo_pk).update(
            district_memo = request.POST['district_memo'],
          
        )
        return redirect('home')
    return render(request, 'edit_memo.html',{'memo': memo})

class EditView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'edit.html'

class DeleteView(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

def YungchangView(request):
    memos= Memo.objects.filter(district='융창지구')
    category_articles = Article.objects.filter(district='융창지구')
    return render(request, 'districts/yungchang.html', {'category_articles':category_articles,'memos':memos})

   

def BisanView(request):
    memos= Memo.objects.filter(district='비산초교')
    category_articles = Article.objects.filter(district='비산초교')
    return render(request, 'districts/bisan.html', {'category_articles':category_articles,'memos':memos})

    
def DuckheonView(request):
    memos= Memo.objects.filter(district='덕현지구')
    category_articles = Article.objects.filter(district='덕현지구')
    return render(request, 'districts/duckheon.html', {'category_articles':category_articles,'memos':memos})

def HogaeView(request):
    memos= Memo.objects.filter(district='호계구사거리지구')
    category_articles = Article.objects.filter(district='호계구사거리지구')
    return render(request, 'districts/hogae.html', {'category_articles':category_articles,'memos':memos})

def ImgokView(request):
    memos= Memo.objects.filter(district='임곡지구 비산자이아이파크')
    category_articles = Article.objects.filter(district='임곡지구 비산자이아이파크')
    return render(request, 'districts/imgok.html', {'category_articles':category_articles,'memos':memos})

def MiryungView(request):
    memos= Memo.objects.filter(district='미륭아파트')
    category_articles = Article.objects.filter(district='미륭아파트')
    return render(request, 'districts/miryung.html', {'category_articles':category_articles,'memos':memos})


def OncheonView(request):
    memos= Memo.objects.filter(district='온천지구')
    category_articles = Article.objects.filter(district='온천지구')
    return render(request, 'districts/oncheon.html', {'category_articles':category_articles,'memos':memos})


def SamsinView(request):
    memos= Memo.objects.filter(district='삼신 6차')
    category_articles = Article.objects.filter(district='삼신 6차')
    return render(request, 'districts/samsin.html', {'category_articles':category_articles,'memos':memos})

    
def NewtownoneView(request):
    memos= Memo.objects.filter(district='뉴타운맨션 삼호 1~3차')
    category_articles = Article.objects.filter(district='뉴타운맨션 삼호 1~3차')
    return render(request, 'districts/newtown1.html', {'category_articles':category_articles,'memos':memos})

def NewtownfourView(request):
    memos= Memo.objects.filter(district='뉴타운맨션 삼호 4차')
    category_articles = Article.objects.filter(district='뉴타운맨션 삼호 4차')
    return render(request, 'districts/newtown4.html', {'category_articles':category_articles,'memos':memos})

def NewtownfiveView(request):
    memos= Memo.objects.filter(district='뉴타운맨션 삼호 5차')
    category_articles = Article.objects.filter(district='뉴타운맨션 삼호 5차')
    return render(request, 'districts/newtown5.html', {'category_articles':category_articles,'memos':memos})

def NewtownsixView(request):
    memos= Memo.objects.filter(district='뉴타운맨션 삼호 6차')
    category_articles = Article.objects.filter(district='뉴타운맨션 삼호 6차')
    return render(request, 'districts/newtown6.html', {'category_articles':category_articles,'memos':memos})


def NangcheonView(request):
    memos= Memo.objects.filter(district='냉천지구')
    category_articles = Article.objects.filter(district='냉천지구')
    return render(request, 'districts/nangcheon.html', {'category_articles':category_articles,'memos':memos})

def ArtView(request):
    memos= Memo.objects.filter(district='안양예술공원 아르테자이')
    category_articles = Article.objects.filter(district='안양예술공원 아르테자이')
    return render(request, 'districts/art.html', {'category_articles':category_articles,'memos':memos})

def NaesondaView(request):
    memos= Memo.objects.filter(district='내손다구역')
    category_articles = Article.objects.filter(district='내손다구역')
    return render(request, 'districts/naesonda.html', {'category_articles':category_articles,'memos':memos})

def NaesonraView(request):
    memos= Memo.objects.filter(district='내손라구역')
    category_articles = Article.objects.filter(district='내손라구역')
    return render(request, 'districts/naesonra.html', {'category_articles':category_articles,'memos':memos})

def GocheongaView(request):
    memos= Memo.objects.filter(district='고천가구역')
    category_articles = Article.objects.filter(district='고천가구역')
    return render(request, 'districts/gocheonga.html', {'category_articles':category_articles,'memos':memos})

def GocheonnaView(request):
    memos= Memo.objects.filter(district='고천나구역')
    category_articles = Article.objects.filter(district='고천나구역')
    return render(request, 'districts/gocheonna.html', {'category_articles':category_articles,'memos':memos})

def OjunnaView(request):
    memos= Memo.objects.filter(district='오전나구역')
    category_articles = Article.objects.filter(district='오전나구역')
    return render(request, 'districts/ojunna.html', {'category_articles':category_articles,'memos':memos})

def OjundaView(request):
    memos= Memo.objects.filter(district='오전다구역')
    category_articles = Article.objects.filter(district='오전다구역')
    return render(request, 'districts/ojunda.html', {'category_articles':category_articles,'memos':memos})

def AnyangstationView(request):
    memos= Memo.objects.filter(district='안양역세권주변지구')
    category_articles = Article.objects.filter(district='안양역세권주변지구')
    return render(request, 'districts/station.html', {'category_articles':category_articles,'memos':memos})

def SangrokView(request):
    memos= Memo.objects.filter(district='상록지구')
    category_articles = Article.objects.filter(district='상록지구')
    return render(request, 'districts/sangrok.html', {'category_articles':category_articles,'memos':memos})

def HwachangView(request):
    memos= Memo.objects.filter(district='화창지구')
    category_articles = Article.objects.filter(district='화창지구')
    return render(request, 'districts/hwachang.html', {'category_articles':category_articles,'memos':memos})
