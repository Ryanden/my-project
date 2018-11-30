from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import StoreModelForm, StoreForm
from ..models import Store

__all__ = (
    'store_create',
)


def store_create(request):
    # PostModelForm을 사용
    #  form = PostModelForm(request.POST, request.FILES)
    #  post = form.save(commit=False)
    #  post.author = request.user
    #  post.save()
    if request.method == 'POST':
        form = StoreModelForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.author = request.user
            store.save()
            return redirect('stores:store-detail', pk=store.pk)
    else:
        form = StoreModelForm()
    context = {
        'form': form,
    }
    return render(request, 'stores/store_create.html', context)


@login_required
def store_create_with_form(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(author=request.user)
            return redirect('stores:store-detail', pk=store.pk)
    else:
        form = StoreForm()
    context = {
        'form': form,
    }
    return render(request, 'stores/store_create.html', context)


def store_create_without_form(request):
    if request.method == 'POST':
        store = Store(
            author=request.user,
            photo=request.FILES['photo'],
            content=request.POST['content'],
        )
        store.save()
        return redirect('stores:store-detail', pk=store.pk)
    return render(request, 'stores/store_create.html')
