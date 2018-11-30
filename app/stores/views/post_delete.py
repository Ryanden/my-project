from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..models import Store

__all__ = (
    'store_delete',
)


@require_POST
@login_required
def store_delete(request, pk):
    # if request.method != 'POST':
    #     return HttpResponseNotAllowed()
    # if not request.user.is_authenticated:
    #     return redirect('members:login')
    store = get_object_or_404(Store, pk=pk)
    if store.author != request.user:
        raise PermissionDenied('지울 권한이 없습니다')
    store.delete()
    return redirect('stores:store-list')
