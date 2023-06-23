from django.urls import reverse
from django.test import Client
from bs4 import BeautifulSoup
import pytest


class TestprofilesIndexView:

    client = Client()
    index_url = reverse('profiles:index')

    @pytest.mark.django_db
    def test_profiles_index_views_with_empty_db(self):

        response = self.client.get(self.index_url)

        assert response.status_code == 200
        assert '<title>Profiles</title>' in str(response.content)
        assert '<p>No profiles are available.</p>' in str(response.content)

    @pytest.mark.django_db
    def test_lettings_index_views_with_filed_db(self, get_datas):

        response = self.client.get(self.index_url)

        assert response.status_code == 200
        assert '<title>Profiles</title>' in str(response.content)

        soup = BeautifulSoup(response.content, 'html.parser')

        profiles_count = 0

        for li in soup.find_all('li'):
            profiles_count += 1
            assert li.find('a', href=True)
            assert li.a['href'] == reverse(
                'profiles:profile',
                kwargs={'username': get_datas['profile' + str(profiles_count)].user.username}
                                           )

        for i in range(1, profiles_count+1):
            assert get_datas['profile' + str(i)].user.username in str(response.content)

    @pytest.mark.django_db
    def test_nav_links_present_in_profiles_index_view(self):

        response = self.client.get(self.index_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        home_link_found = False
        url_home = ''
        lettings_link_found = False
        url_lettings = ''

        if soup.find('div'):
            for div in soup.find_all('div'):
                if div.find('a', href=True):
                    if div.a.string == 'Home':
                        home_link_found = True
                        url_home = div.a['href']
                    elif div.a.string == 'Lettings':
                        lettings_link_found = True
                        url_lettings = div.a['href']

        assert home_link_found
        assert url_home == reverse('index')
        assert lettings_link_found
        assert url_lettings == reverse('lettings:index')


class TestProfilesProfileView:

    client = Client()

    @pytest.mark.django_db
    def test_lettings_letting_view_with_existing_id(self, get_datas):

        profile_to_test = get_datas['profile1']

        profile_url = reverse(
                'profiles:profile',
                kwargs={'username': profile_to_test.user.username}
                                           )

        response = self.client.get(profile_url)

        assert response.status_code == 200
        assert '<title>' + profile_to_test.user.username + '</title>' in str(response.content)
        assert '<p>First name: ' + profile_to_test.user.first_name + '</p>' in str(
            response.content)
        assert '<p>Last name: ' + profile_to_test.user.last_name + '</p>' in str(
            response.content)
        assert '<p>Email: ' + profile_to_test.user.email + '</p>' in str(
            response.content)
        assert '<p>Favorite city: ' + profile_to_test.favorite_city + '</p>' in str(
            response.content)

    @pytest.mark.django_db
    def test_nav_links_present_in_profiles_profile_view(self, get_datas):
        profile_to_test = get_datas['profile1']

        profile_url = reverse(
            'profiles:profile',
            kwargs={'username': profile_to_test.user.username}
        )

        response = self.client.get(profile_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        back_link_found = False
        url_back = ''
        home_link_found = False
        url_home = ''
        lettings_link_found = False
        url_lettings = ''

        if soup.find('div'):
            for div in soup.find_all('div'):
                if div.find('a', href=True):
                    if div.a.string == 'Home':
                        home_link_found = True
                        url_home = div.a['href']
                    elif div.a.string == 'Lettings':
                        lettings_link_found = True
                        url_lettings = div.a['href']
                    elif div.a.string == 'Back':
                        back_link_found = True
                        url_back = div.a['href']

        assert back_link_found
        assert url_back == reverse('profiles:index')
        assert home_link_found
        assert url_home == reverse('index')
        assert lettings_link_found
        assert url_lettings == reverse('lettings:index')

    @pytest.mark.django_db
    def test_profiles_profile_view_with_non_existing_id(self, get_datas):

        profile_url = reverse(
            'profiles:profile',
            kwargs={'username': 'unknown'}
        )

        response = self.client.get(profile_url)

        assert response.status_code == 404

