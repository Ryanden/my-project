from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

from ..models import Recipe

__all__ = (
    'recipe_delete',
)


@require_POST
@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('costcalculator:calculator-menu')
