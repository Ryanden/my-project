from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..models import CostCalculator

__all__ = (
    'item_ingredient_delete',
)


@require_POST
@login_required
def item_ingredient_delete(request, pk):
    ingredient = get_object_or_404(CostCalculator, pk=pk)
    ingredient.delete()
    return redirect('costcalculator:item-detail', pk)
