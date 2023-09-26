from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Advert, Category, City


class AdvertAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Test Category")
        self.city = City.objects.create(name="Test City")
        self.advert = Advert.objects.create(
            title="Test Advert",
            description="Test description",
            city=self.city,
            category=self.category,
        )
        self.url = reverse("advert-list")

    def test_list_adverts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.advert.title)

    def test_create_advert(self):
        data = {
            "title": "New Advert",
            "description": "New description",
            "city": self.city.id,
            "category": self.category.id,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advert.objects.count(), 2)

    def test_retrieve_advert(self):
        retrieve_url = reverse("advert-detail", args=[self.advert.id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.advert.title)

    def test_update_advert(self):
        update_data = {
            "title": "Updated Advert",
            "description": "Updated description",
            "city": self.city.id,
            "category": self.category.id,
        }
        update_url = reverse("advert-detail", args=[self.advert.id])
        response = self.client.put(update_url, update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.advert.refresh_from_db()
        self.assertEqual(self.advert.title, "Updated Advert")

    def test_delete_advert(self):
        delete_url = reverse("advert-detail", args=[self.advert.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Advert.objects.count(), 0)
