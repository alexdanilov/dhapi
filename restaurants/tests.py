from django.conf import settings
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from .models import Restaurant


class AccountTests(APITestCase, URLPatternsTestCase):
    fixtures = ['initial_data.json']
    urlpatterns = [
        path('api/v1/', include('restaurants.urls')),
    ]

    TIME_FORMAT = settings.REST_FRAMEWORK['TIME_FORMAT']

    def test_get_restaurants(self):
        """
        Ensure we can get a list of restaurants.
        """
        url = reverse('restaurant-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

        resto = response.data[0]
        self.assertTrue('id' in resto)
        self.assertTrue('name' in resto)
        self.assertTrue('opens_at' in resto)
        self.assertTrue('closes_at' in resto)

    def test_get_restaurant(self):
        """
        Ensure we can get a detail data of restaurant.
        """
        resto_id = Restaurant.objects.first().id

        url = reverse('restaurant-detail', kwargs={'pk': resto_id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        resto = Restaurant.objects.get(id=resto_id)
        self.assertEqual(response.data['id'], resto.id)
        self.assertEqual(response.data['name'], resto.name)
        self.assertEqual(response.data['opens_at'], resto.opens_at.strftime(self.TIME_FORMAT))
        self.assertEqual(response.data['closes_at'], resto.closes_at.strftime(self.TIME_FORMAT))

    def test_create_restaurant(self):
        """
        Ensure we can create a new restaurant.
        """
        data = {'name': 'Pizza', 'opens_at': '08:00', 'closes_at': '23:00'}

        url = reverse('restaurant-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        resto = Restaurant.objects.get(id=response.data['id'])
        self.assertEqual(response.data['name'], resto.name)
        self.assertEqual(response.data['opens_at'], resto.opens_at.strftime(self.TIME_FORMAT))
        self.assertEqual(response.data['closes_at'], resto.closes_at.strftime(self.TIME_FORMAT))

    def test_change_restaurant(self):
        """
        Ensure we can change data of an exists restaurant.
        """
        resto = Restaurant.objects.create(name='Test Pastoteca', opens_at='10:00', closes_at='22:00')
        data = {'name': 'Pastateca', 'opens_at': '09:00'}

        url = reverse('restaurant-detail', kwargs={'pk': resto.id})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        exists_resto = Restaurant.objects.get(id=resto.id)
        self.assertEqual(data['name'], exists_resto.name)
        self.assertEqual(data['opens_at'], exists_resto.opens_at.strftime(self.TIME_FORMAT))

    def test_delete_restaurant(self):
        """
        Ensure we can delete an exists restaurant.
        """
        resto = Restaurant.objects.create(name='Test', opens_at='10:00', closes_at='22:00')

        url = reverse('restaurant-detail', kwargs={'pk': resto.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Restaurant.objects.filter(id=resto.id).exists())
