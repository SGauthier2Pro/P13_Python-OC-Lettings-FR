from django.urls import reverse
from django.test import Client


class TestOCLettingsSiteViews:

    client = Client()

    def test_index_view(self):

        uri = reverse('index')
        response = self.client.get(uri)

        assert response.status_code == 200
        assert '<title>Holiday Homes</title>' in str(response.content)
