from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger

# Create your views here.
def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,
                           
                           status=Post.Status.PUBLISHED,
                           slug=post,
                           publish_year=year,
                           publish_month=month,
                           publish_day=day
                           
                           )

    
    switch={'post':post}
    return render(request,
                  'reader/post/detail.html',switch)

def post_list(request):
    post_list=Post.published.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page',2)

    try:
        posts=paginator.page(page_number)

    except PageNotAnInteger:
        posts=paginator.page(1)   
    
    
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    


    switch={'posts': posts}
    return render(request,
                  'reader/post/list.html',switch)
