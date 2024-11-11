from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('created_at')
    items_per_page = request.GET.get('items_per_page', 2)
    if items_per_page is None or items_per_page == '':
        items_per_page = 2
    else:
        items_per_page = int(items_per_page)
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html', {
        'page_obj': page_obj,
        'items_per_page': items_per_page,
    })

# Create your views here.
