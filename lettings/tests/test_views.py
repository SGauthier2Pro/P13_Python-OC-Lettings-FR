from django.urls import reverse
from django.test import Client
from bs4 import BeautifulSoup
import pytest


class TestLettingsIndexView:

    client = Client()
    index_url = reverse('lettings:index')

    @pytest.mark.django_db
    def test_lettings_index_views_with_empty_db(self):

        response = self.client.get(self.index_url)

        assert response.status_code == 200
        assert '<title>Lettings</title>' in str(response.content)
        assert '<p>No lettings are available.</p>' in str(response.content)

    @pytest.mark.django_db
    def test_lettings_index_views_with_filed_db(self, get_datas):

        response = self.client.get(self.index_url)

        assert response.status_code == 200
        assert '<title>Lettings</title>' in str(response.content)

        soup = BeautifulSoup(response.content, 'html.parser')

        lettings_count = 0

        for li in soup.find_all('li'):
            lettings_count += 1
            assert li.find('a', href=True)
            assert li.a['href'] == reverse(
                'lettings:letting',
                kwargs={'letting_id': get_datas['letting' + str(lettings_count)].id}
                                           )

        for i in range(1, lettings_count+1):
            assert get_datas['letting' + str(i)].title in str(response.content)

    @pytest.mark.django_db
    def test_nav_links_present_in_lettings_index_view(self):

        response = self.client.get(self.index_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        home_link_found = False
        url_home = ''
        profiles_link_found = False
        url_profiles = ''

        if soup.find('div'):
            for div in soup.find_all('div'):
                if div.find('a', href=True):
                    if div.a.string == 'Home':
                        home_link_found = True
                        url_home = div.a['href']
                    elif div.a.string == 'Profiles':
                        profiles_link_found = True
                        url_profiles = div.a['href']

        assert home_link_found
        assert url_home == reverse('index')
        assert profiles_link_found
        assert url_profiles == reverse('profiles:index')


class TestLettingsLettingView:

    client = Client()

    @pytest.mark.django_db
    def test_lettings_letting_view_with_existing_id(self, get_datas):

        letting_to_test = get_datas['letting1']

        letting_url = reverse(
                'lettings:letting',
                kwargs={'letting_id': letting_to_test.id}
                                           )

        response = self.client.get(letting_url)

        assert response.status_code == 200
        assert '<title>' + letting_to_test.title + '</title>' in str(response.content)
        assert '<p>' + str(letting_to_test.address.number) + ' '\
               + letting_to_test.address.street + '</p>' in str(response.content)
        assert '<p>' + letting_to_test.address.city + ', '\
               + letting_to_test.address.state + ' ' \
               + str(letting_to_test.address.zip_code) + '</p>' in str(response.content)
        assert '<p>' + letting_to_test.address.country_iso_code + '</p>' in str(response.content)

    @pytest.mark.django_db
    def test_nav_links_present_in_lettings_letting_view(self, get_datas):
        letting_to_test = get_datas['letting1']

        letting_url = reverse(
            'lettings:letting',
            kwargs={'letting_id': letting_to_test.id}
        )

        response = self.client.get(letting_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        back_link_found = False
        url_back = ''
        home_link_found = False
        url_home = ''
        profiles_link_found = False
        url_profiles = ''

        if soup.find('div'):
            for div in soup.find_all('div'):
                if div.find('a', href=True):
                    if div.a.string == 'Home':
                        home_link_found = True
                        url_home = div.a['href']
                    elif div.a.string == 'Profiles':
                        profiles_link_found = True
                        url_profiles = div.a['href']
                    elif div.a.string == 'Back':
                        back_link_found = True
                        url_back = div.a['href']

        assert back_link_found
        assert url_back == reverse('lettings:index')
        assert home_link_found
        assert url_home == reverse('index')
        assert profiles_link_found
        assert url_profiles == reverse('profiles:index')
