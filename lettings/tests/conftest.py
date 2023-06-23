import pytest
from django.contrib.auth.models import User

from lettings.models.letting import Letting
from lettings.models.address import Address

from profiles.models.profile import Profile


@pytest.fixture
def get_datas():

    user1 = User.objects.create_user(
        username='user1',
        password='P@s$4TestAp1',
        email='user1@test.net',
        first_name='user',
        last_name='1'
    )

    user2 = User.objects.create_user(
        username='user2',
        password='P@s$4TestAp1',
        email='user2@test.net',
        first_name='user',
        last_name='2'
    )

    user3 = User.objects.create_user(
        username='user3',
        password='P@s$4TestAp1',
        email='user3@test.net',
        first_name='user',
        last_name='3'
    )

    adresse1 = Address.objects.create(
        number=3,
        street='rue du fou',
        city='Dinguetown',
        state='PI',
        zip_code=69390,
        country_iso_code='FR'
    )

    adresse2 = Address.objects.create(
        number=356,
        street='Avenue des ombres',
        city='Sombrelune',
        state='IG',
        zip_code=87542,
        country_iso_code='DK'
    )

    adresse3 = Address.objects.create(
        number=27,
        street='Downtown street',
        city='FreeTown',
        state='BD',
        zip_code=89140,
        country_iso_code='IR'
    )

    adresse4 = Address.objects.create(
        number=5656,
        street='Vampire State Building road',
        city='Paris',
        state='PA',
        zip_code=75009,
        country_iso_code='FR'
    )

    adresse5 = Address.objects.create(
        number=666,
        street='Devil Street',
        city='Inferno',
        state='EN',
        zip_code=66666,
        country_iso_code='EN'
    )

    letting1 = Letting.objects.create(
        title='DingueTown Abbey',
        address=adresse1
    )

    letting2 = Letting.objects.create(
        title='Darkmoon journey',
        address=adresse2
    )

    letting3 = Letting.objects.create(
        title='Free your Mind',
        address=adresse3
    )

    letting4 = Letting.objects.create(
        title='French Dracula Castle',
        address=adresse4
    )

    letting5 = Letting.objects.create(
        title='Die Hard',
        address=adresse5
    )

    profile1 = Profile.objects.create(
        user=user1,
        favorite_city='Paris'
    )

    profile2 = Profile.objects.create(
        user=user2,
        favorite_city='New York'
    )

    profile3 = Profile.objects.create(
        user=user3,
        favorite_city='Dublin'
    )

    return locals()
