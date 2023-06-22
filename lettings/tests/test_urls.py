from django.urls import reverse, resolve
from django.test import Client
from bs4 import BeautifulSoup
import pytest


class TestLettingsUrls:

    def test_lettings_index_url(self):

        url = reverse('lettings:index')
        assert resolve(url).view_name == 'lettings:index'
        assert resolve(url).url_name == 'index'

    @pytest.mark.django_db
    def test_lettings_letting_url(self, get_datas):

        client = Client()

        index = reverse('lettings:index')
        index_response = client.get(index)

        soup = BeautifulSoup(index_response.content, 'html.parser')

        for li in soup.find_all('li'):
            for a in li.find_all('a', href=True):

                url_split = a['href'].split("/")
                letting_id = url_split[-2]
                url = reverse('lettings:letting', kwargs={'letting_id': letting_id})

                assert resolve(url).view_name == 'lettings:letting'
                assert resolve(url).url_name == 'letting'
