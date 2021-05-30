from model_bakery import baker
import pytest


@pytest.fixture
def admin(city):
    admin = baker.make_recipe('tests.fixtures.admin')
    admin.city.set([city])
    return admin


@pytest.fixture
def moderator():
    return baker.make_recipe('tests.fixtures.moderator')


@pytest.fixture
def token_for_admin(admin):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(admin)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def admin_client(token_for_admin):
    from rest_framework.test import APIClient
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_for_admin["access"]}')
    return client


@pytest.fixture
def token_for_moderator(moderator):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(moderator)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def moderator_client(token_for_moderator):
    from rest_framework.test import APIClient
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_for_moderator["access"]}')
    return client
