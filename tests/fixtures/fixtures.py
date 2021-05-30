from model_bakery.recipe import Recipe
from model_bakery import baker
from events.models import Event
import pytest


@pytest.fixture
def city():
    return baker.make_recipe('tests.fixtures.city')


@pytest.fixture
def another_city():
    return baker.make_recipe('tests.fixtures.city')


# Events in the same city
@pytest.fixture
def event(city):
    return baker.make_recipe('tests.fixtures.event',city=city,seats=1)

@pytest.fixture
def event_another(city):
    return baker.make_recipe('tests.fixtures.event',city=city)


# Events batch in new,created city
@pytest.fixture
def events():
    return baker.make_recipe('tests.fixtures.event', _quantity=3)

# Admin participates in several events
@pytest.fixture
def admin_participant(admin,event):
    return baker.make_recipe('tests.fixtures.event_participant',user=admin,event=event)

@pytest.fixture
def admin_participant_another(admin,event_another):
    return baker.make_recipe('tests.fixtures.event_participant',user=admin,event=event_another)

