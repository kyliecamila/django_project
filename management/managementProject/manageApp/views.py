from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from .models import Post, Category, List
from .forms import PostForm
from django.urls import reverse_lazy

# class HomeView(ListView):
def CategoryView(request, cats):
    category_posts = Post.objects.filter(district=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts} )



def HomeView(request):
    my_posts = Post.objects.filter(owner='탑공인중개사')
    return render(request, 'home.html', {'my_posts':my_posts} )
   

def YungchangView(request):
    category_posts = Post.objects.filter(district='융창지구')
    return render(request, 'yungchang.html', {'category_posts':category_posts} )
   

def BisanView(request):
    category_posts = Post.objects.filter(district='비산초교')
    return render(request, 'bisan.html', {'category_posts':category_posts} )

    
def DuckheonView(request):
    category_posts = Post.objects.filter(district='덕현지구')
    return render(request, 'duckheon.html', {'category_posts':category_posts} )


def HogaeView(request):
    category_posts = Post.objects.filter(district='호계구사거리지구')
    return render(request, 'hogae.html', {'category_posts':category_posts} )

def ImgokView(request):
    category_posts = Post.objects.filter(district='임곡지구 비산자이아이파크')
    return render(request, 'imgok.html', {'category_posts':category_posts} )

def MiryungView(request):
    category_posts = Post.objects.filter(district='미륭아파트')
    return render(request, 'miryung.html', {'category_posts':category_posts} )


def OncheonView(request):
    category_posts = Post.objects.filter(district='온천지구')
    return render(request, 'oncheon.html', {'category_posts':category_posts} )


def SamsinView(request):
    category_posts = Post.objects.filter(district='삼신6차')
    return render(request, 'samsin.html', {'category_posts':category_posts} )

    
def NewtownView(request):
    category_posts = Post.objects.filter(district='뉴타운맨션 삼호')
    return render(request, 'newtown.html', {'category_posts':category_posts} )

def NangcheonView(request):
    category_posts = Post.objects.filter(district='냉천지구')
    return render(request, 'nangcheon.html', {'category_posts':category_posts} )

def ArtView(request):
    category_posts = Post.objects.filter(district='안양예술공원 아르테자이')
    return render(request, 'art.html', { 'category_posts':category_posts} )

def NaesondaView(request):
    category_posts = Post.objects.filter(district='내손다구역')
    return render(request, 'naesonda.html', {'category_posts':category_posts} )

def NaesonraView(request):
    category_posts = Post.objects.filter(district='내손라구역')
    return render(request, 'naesonra.html', {'category_posts':category_posts} )

def GocheongaView(request):
    category_posts = Post.objects.filter(district='고천가구역')
    return render(request, 'gocheonga.html', {'category_posts':category_posts} )

def GocheonnaView(request):
    category_posts = Post.objects.filter(district='고천나구역')
    return render(request, 'gocheonna.html', { 'category_posts':category_posts} )

def OjunnaView(request):
    category_posts = Post.objects.filter(district='오전나구역')
    return render(request, 'ojunna.html', {'category_posts':category_posts} )

def OjundaView(request):
    category_posts = Post.objects.filter(district='오전다구역')
    return render(request, 'ojunda.html', {'category_posts':category_posts} )

def AnyangstationView(request):
    category_posts = Post.objects.filter(district='안양역세권주변지구')
    return render(request, 'anyangstation.html', {'category_posts':category_posts} )

def SangrokView(request):
    category_posts = Post.objects.filter(district='상록지구')
    return render(request, 'sangrok.html', {'category_posts':category_posts} )

def HwachangView(request):
    category_posts = Post.objects.filter(district='화창지구')
    return render(request, 'hwachang.html', {'category_posts':category_posts} )




class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    # fields = ['district', 'price', 'area', 'owner', 'date','memo']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



