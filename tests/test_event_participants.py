import pytest
from model_bakery import baker

from events.models import Event, EventParticipant
from user.models import User, City


class TestEventParticipants:
    endpoint = '/api/v1/event-participants/'

    @pytest.mark.django_db(transaction=True)
    def test_list_unauthorized(self, client):
        response = client.get(self.endpoint)
        assert response.status_code != 404, (f'Адрес {self.endpoint} не существует')
        assert response.status_code == 401, (
            f'Запрос к {self.endpoint} без токена должен возвращать 401'
        )

    @pytest.mark.django_db(transaction=True)
    def test_list_authorized(
            self, moderator, admin, admin_client,
            admin_participant, admin_participant_another
    ):
        baker.make_recipe(
            'tests.fixtures.event_participant',
            user=moderator,
            event=admin_participant.event
        )
        response = admin_client.get(self.endpoint)
        assert response.status_code == 200, (
            f'Запрос к {self.endpoint} с токеном должен возвращать 200'
        )
        test_data = response.json()
        test_event = test_data[0]
        registration_num = EventParticipant.objects.filter(user=admin).count()
        assert len(test_data) == registration_num, (
            f'{self.endpoint} должен возвращать все регистрации пользователя'
        )
        assert test_event.get('event') == admin_participant.event.id
        assert len(test_data) < EventParticipant.objects.count(), (
            f'{self.endpoint} для авторизованного пользователя не должен показывать регистрации других пользователей'
        )
        assert 'id' in test_event, (
            f'id нет в списке полей сериализатора модели EventParticipant'
        )
        assert 'event' in test_event, (
            f'event нет в списке полей сериализатора модели EventParticipant'
        )

    @pytest.mark.django_db
    def test_create_unauthorized(self, client):
        data = {}
        response = client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 401, (
            f'POST запрос к {self.endpoint} без токена должен вернуть 401'
        )

    @pytest.mark.django_db
    def test_create_authorized(
            self, admin, admin_client, moderator, moderator_client,
            event, event_another, events
    ):
        participants_count = EventParticipant.objects.count()
        data = {}
        response = admin_client.post(self.endpoint, data=data, format='json')
        assert response.status_code == 400, (
            f'POST запрос к {self.endpoint} с неправильными данными должен вернуть 400'
        )
        expected_json = {'event': event.id}
        response = admin_client.post(self.endpoint, data=expected_json, format='json')
        test_data = response.json()
        assert participants_count + 1 == EventParticipant.objects.count()
        assert response.status_code == 201, (
            f'POST запрос к {self.endpoint} с валидными данными создает новую регистрацию'
        )
        event.refresh_from_db()
        assert event.taken_seats == 1, (
            f'POST запрос к {self.endpoint} с валидными данными меняет значение'
            f' taken_seats в соответствующем событии'
        )
        assert 'id' in test_data, (
            'id нет в списке полей сериализатора модели EventParticipant'
        )
        assert 'event' in test_data, (
            'event нет в списке полей сериализатора модели EventParticipant'
        )
        response = admin_client.post(self.endpoint, data=expected_json)
        assert EventParticipant.objects.count() == 1
        assert response.status_code == 400, (
            f'Повторная регистрация на мероприятие не должна быть возможна'
        )
        participants_count = EventParticipant.objects.count()
        event_in_another_city = events[0]
        expected_json = {'event': event_in_another_city.id}
        response = admin_client.post(self.endpoint, data=expected_json, format='json')
        assert event.city != event_in_another_city.city, (
            'Ошибка теста: события должны быть в разных городах'
        )
        assert participants_count + 1 == EventParticipant.objects.count()
        assert response.status_code == 201, (
            'Регистрация на событие в другом городе должна быть возможна'
        )
        # Проверяем флаг booked
        response = admin_client.get('/api/v1/events/')
        test_data = response.json()
        assert len(test_data) == Event.objects.filter(city__in=admin.city.all()).count()
        event_booked = test_data[0]
        assert event_booked.get('booked') == True, (
            'Поле booked должно быть True если пользователь зарегестрирован'
        )
        event_not_booked = test_data[1]
        assert event_not_booked.get('booked') == False, (
            'Поле booked должно быть False если пользователь  не зарегестрирован'
        )
        expected_json = {'event': event.id}
        response = moderator_client.post(self.endpoint, data=expected_json, format='json')
        assert response.status_code == 400, (
            'При регистрации на событие без доступных мест ответ должен быть 400'
        )
        assert 'seats' in response.data, (
            'Поле seats должно содержать сообщение об ошибке'
        )

    @pytest.mark.django_db(transaction=True)
    def test_destroy(self, admin, admin_client, event, admin_participant_another):
        data = {'event': event.id}
        admin_client.post(self.endpoint, data=data, format='json')
        event.refresh_from_db()
        taken_seats_counter = event.taken_seats
        participants_count = EventParticipant.objects.filter(user=admin).count()
        data = {'event': event.id}
        response = admin_client.delete(self.endpoint,data=data, format='json')
        event.refresh_from_db()
        assert response.status_code == 204, (
            f'DELETE запрос {self.endpoint} должен вернуть 204'
        )
        assert EventParticipant.objects.count() == participants_count - 1, (
            f'DELETE запрос {self.endpoint} должен удалить объект'
        )
        assert event.taken_seats == taken_seats_counter - 1, (
            f'DELETE запрос {self.endpoint} должен изменить значение поля taken_seats у объекта Event'
        )
