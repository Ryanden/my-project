from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..models import Product

__all__ = (
    'product_delete',
)


@require_POST
@login_required
def product_delete(request, pk):
    # if request.method != 'POST':
    #     return HttpResponseNotAllowed()
    # if not request.user.is_authenticated:
    #     return redirect('members:login')
    product = get_object_or_404(Product, pk=pk)
    if product.author != request.user:
        raise PermissionDenied('지울 권한이 없습니다')
    product.delete()
    return redirect('products:product-list')
