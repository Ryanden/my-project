from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..forms import QualityTestForm

__all__ = (
    'quality_test_create',
)


def quality_test_create(request):

    return HttpResponse('aa')

