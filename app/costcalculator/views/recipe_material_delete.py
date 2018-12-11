from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..models import CostCalculator

__all__ = (
    'recipe_material_delete',
)


@require_POST
@login_required
def recipe_material_delete(request, pk):
    item = get_object_or_404(CostCalculator, pk=pk)
    item.delete()
    return redirect('costcalculator:recipe-detail', pk)
