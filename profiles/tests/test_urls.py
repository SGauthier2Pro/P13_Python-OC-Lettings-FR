from django.urls import reverse, resolve
from django.test import Client
from bs4 import BeautifulSoup
import pytest


class TestProfilesUrls:

    def test_profiles_index_url(self):

        url = reverse('profiles:index')
        assert resolve(url).view_name == 'profiles:index'
        assert resolve(url).url_name == 'index'

    @pytest.mark.django_db
    def test_profiles_profile_url(self, get_datas):

        client = Client()

        index = reverse('profiles:index')
        index_response = client.get(index)

        soup = BeautifulSoup(index_response.content, 'html.parser')

        for li in soup.find_all('li'):
            for a in li.find_all('a', href=True):

                url_split = a['href'].split("/")
                profile_username = url_split[-2]
                url = reverse('profiles:profile', kwargs={'username': profile_username})

                assert resolve(url).view_name == 'profiles:profile'
                assert resolve(url).url_name == 'profile'
