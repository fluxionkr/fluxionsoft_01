from django.views.generic import ListView, DetailView
from firstapp.models import Memo

# Create your views here.
class MemoList(ListView) :
    model = Memo

class MemoDetail(DetailView) :
    model = Memo