from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from menu.models import *
from menu.forms import *


def menu_list(request):
    """
    Displays menus with a valid expiration date and ordered by
    season name
    """
    menus = Menu.objects.only('season').filter(
        Q(expiration_date__gte=timezone.now())|
        Q(expiration_date__isnull=True)).order_by('season')
    return render(request, 'menu/list_all_current_menus.html', {'menus':menus})


def menu_detail(request, pk):
    """
    Displays the elements of the selected menu, if is the case it includes
    expiration date
    """
    menu = Menu.objects.get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    """
    Displays the ingredients for the selected element of a given menu
    """
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'menu/item_detail.html', {'item': item})


def create_new_menu(request):
    """ View of form to add a new menu """
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save()
            menu.created_date = timezone.now()
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    return render(request, 'menu/new_menu.html', {'form': form})


def edit_menu(request, pk):
    """ View to edit an existing menu """
    menu = get_object_or_404(Menu, pk=pk)
    form_edit = MenuForm(instance = menu)
    if request.method == "POST":
        form_edit = MenuForm(data=request.POST, instance = menu)
        if form_edit.is_valid():
            form_edit.save()
            return redirect('menu_detail', pk=menu.pk)
    return render(request, 'menu/change_menu.html', {'form_edit': form_edit})
