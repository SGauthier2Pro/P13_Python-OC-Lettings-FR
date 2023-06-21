from django.urls import reverse, resolve


def test_oc_lettings_site_url():

    url = reverse('index')
    assert resolve(url).view_name == 'index'
    assert resolve(url).url_name == 'index'
