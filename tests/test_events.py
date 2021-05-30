import pytest
from model_bakery import baker

from events.models import Event


class TestEventsList:
    endpoint = '/api/v1/events/'

    @pytest.mark.django_db(transaction=True)
    def test_unauthorized_client(self, city, events, client):
        baker.make_recipe(
            'tests.fixtures.event',
            _quantity=5,
            city=city
        )
        response = client.get(self.endpoint)
        test_data = response.json()
        assert response.status_code != 404, (
            f'Адрес {self.endpoint} не существует'
        )
        assert response.status_code == 200, (
            f'Адрес {self.endpoint} для неавторизованного пользователя должен вернуть 200'
        )
        assert len(test_data) == 0, (
            f'Запрос к {self.endpoint} без GET параметра не должен возвращать объекты'
        )
        response = client.get(self.endpoint + f'?city={city.id}')
        test_data = response.json()
        assert response.status_code == 200, (
            f'Запрос к {self.endpoint} с GET параметром city должен вернуть 200'
        )
        assert len(test_data) == 5, (
            f'Запрос к {self.endpoint} GET параметром city должен вернуть только мероприятия в городе {city}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_authorized_client(self, events, admin, admin_client, moderator_client):
        admin_city = admin.city.all()[0]
        baker.make_recipe(
            'tests.fixtures.event',
            _quantity=5,
            city=admin_city
        )
        response = admin_client.get(self.endpoint)
        test_data = response.json()
        assert response.status_code != 404, (
            f'Адрес {self.endpoint} для запроса с токеном не существует'
        )
        assert response.status_code == 200, (
            f'Запрос к {self.endpoint} с токеном авторизации должен возвращать 200'
        )
        assert len(test_data) == Event.objects.filter(city=admin_city).count(), (
            f'Запрос к {self.endpoint} с токеном авторизации должен возвращать все события в городе пользователя'
        )
        assert len(test_data) < Event.objects.count(), (
            f'{self.endpoint} с токеном не должен возвращать события в других городах'
        )
        test_event = test_data[0]
        assert 'address' in test_event, (
            'address нет в списке полей сериализатора модели Event '
        )
        assert 'contact' in test_event, (
            'contact нет в списке полей сериализатора модели Event '
        )
        assert 'title' in test_event, (
            'title нет в списке полей сериализатора модели Event '
        )
        assert 'description' in test_event, (
            'description нет в списке полей сериализатора модели Event '
        )
        assert 'start_at' in test_event, (
            'start_at нет в списке полей сериализатора модели Event '
        )
        assert 'end_at' in test_event, (
            'end_at нет в списке полей сериализатора модели Event '
        )
        assert 'seats' in test_event, (
            'seats нет в списке полей сериализатора модели Event '
        )
        assert 'taken_seats' in test_event, (
            'taken_seats нет в списке полей сериализатора модели Event '
        )
        assert 'city' in test_event, (
            'taken_seats нет в списке полей сериализатора модели Event '
        )
        assert 'booked' in test_event, (
            'booked нет в списке полей сериализатора модели Event '
        )
        response = moderator_client.get(self.endpoint)
        test_data = response.json()
        assert response.status_code == 200, (
            f'Адрес {self.endpoint} доступен для авторизованного пользователя с пустым полем города'
        )
        assert len(test_data) == 0, (
            f'Запрос к {self.endpoint} от пользователя с пустым полем города возвращает пустой ответ'
        )
