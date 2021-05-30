from model_bakery.recipe import Recipe, seq, foreign_key, related
from events.models import Event, EventParticipant
from user.models import City, User

city = Recipe(
    City,
    name=seq('City')
)

admin = Recipe(
    User,
    username=seq('user'),
    password=seq('PassWord'),
    email=seq('admin', suffix='@gmail.com'),
    role='admin',
    #city=related('city')
)

#admin_with_city = admin.extend(city=related(city,))

moderator = Recipe(
    User,
    password=seq('PassWord'),
    email=seq('moderator', suffix='@gmail.com'),
    role='moderator'
)



event = Recipe(
    Event,
    title = seq('ул Тест'),
    city=foreign_key(city),
    seats=2,
)

event_participant = Recipe(
   EventParticipant,
    user=foreign_key(admin),
    event=foreign_key(event)
)