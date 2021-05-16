from django import forms
from .models import Article, Category,Memo

district_choices = Category.objects.all().values_list('name','name')
choice_list =[]

for item in district_choices:
    choice_list.append(item)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('district', 'price', 'area', 'owner', 'date', 'memo')
        widgets = {
            'district': forms.Select(choices = choice_list, attrs={'class': 'form-control' }),
            'price':forms.TextInput(attrs={'class': 'form-control', 'placeholder': '가격을 입력하세요.'}),
            'area':forms.TextInput(attrs={'class': 'form-control', 'placeholder': '지정 평형을 입력하세요.'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '부동산 이름을 입력하세요.'}),
            'date':forms.TextInput(attrs={'class': 'form-control', 'placeholder': '개시 날짜를 입력하세요.'}),
            'memo':forms.Textarea(attrs={'class': 'form-control', 'placeholder': '메모 공간.'}),
        }

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('district', 'district_memo')
        widgets = {
            'district': forms.Select(choices = choice_list, attrs={'class': 'form-control' }),
            'district_memo':forms.Textarea(attrs={'class': 'form-control', 'placeholder': '메모 공간.'}),
        }