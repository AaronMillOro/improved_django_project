from django.contrib.auth.models import User
from django.core.urlresolvers import reverse # for Django 1.9
from django.test import TestCase
from django.utils import timezone

from menu.forms import *
from menu.models import *


class MenuModelTest(TestCase):
    def test_new_menu(self):
        menu = Menu.objects.create(
            season= 'New season',
            expiration_date= '2020-11-02',
            created_date = timezone.now(),
        )
        menu_test = Menu.objects.get(season = 'New season')
        self.assertEqual(menu_test.season, 'New season')


class ViewsTest(TestCase):
    def setUp(self):
        '''User to test ForeignKey in Item Model'''
        user = User.objects.create(
            id='1',
            email='mail@mail.com',
            is_superuser=1,
            username='theUser',
        )
        self.menu1 = Menu.objects.create(
            season= 'Season 1',
            expiration_date= '2022-11-02',
            created_date = timezone.now(),
        )
        self.menu2 = Menu.objects.create(
            season= 'Season 2',
            expiration_date= '2022-01-22',
            created_date = timezone.now(),
        )
        self.menu1.item1 = self.menu1.items.create(
            name = 'chocho chocho',
            description = 'Delicious',
            chef = user,
            created_date = timezone.now(),
            standard = 'False',
        )
        self.menu1.item2 = self.menu1.items.create(
            name = 'perita perita',
            description = 'Good',
            chef = user,
            created_date = timezone.now(),
            standard = 'False',
        )
        self.menu1.item1.ingredient1 = self.menu1.item1.ingredients.create(
            name = 'sugar everywhere',
        )

    def test_list_view(self):
        response = self.client.get(reverse('menu_list'))
        self.assertTemplateUsed(response,
            'menu/list_all_current_menus.html', 'layout.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.menu1, response.context['menus'])
        self.assertIn(self.menu2, response.context['menus'])

    def test_menu_detail_view(self):
        response = self.client.get(
            reverse('menu_detail',kwargs={'pk':self.menu1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
            'menu/menu_detail.html', 'layout.html')
        self.assertEqual(self.menu1, response.context['menu'])

    def test_menu_item_view(self):
        response = self.client.get(
            reverse('item_detail', kwargs={'pk': self.menu1.item1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
            'menu/item_detail.html', 'layout.html')
        self.assertEqual(self.menu1.item1, response.context['item'])

    def test_new_menu(self):
        response = self.client.get(reverse('menu_new'))
        self.assertTemplateUsed(response,
            'menu/new_menu.html', 'layout.html')


class MenuFormTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(
            season= 'Season 1',
            expiration_date= '2022-11-02',
            created_date = timezone.now(),
        )

    def test_invalid_menu_form(self):
        response = self.client.get(
            reverse('menu_edit', kwargs={'pk': self.menu1.pk}))
        form = MenuForm(data={
            'season':'Aztec Season',
            'items': 'False string',
            'expiration_date': '2022-11-02',
        })
        self.assertFalse(form.is_valid())
        self.assertTemplateUsed(response,
            'menu/change_menu.html', 'layout.html')

    def test_invalid_new_menu_form(self):
        response = self.client.get(reverse('menu_new'))
        form = MenuForm(data={
            'season':'Aztec Season',
            'item_id': '?????',
            'expiration_date': '2022-11-02',
        })
        self.assertFalse(form.is_valid())
        self.assertTemplateUsed(response,'menu/new_menu.html', 'layout.html')
