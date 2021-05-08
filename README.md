## Авторизация - получение токена
###запрос
`curl --location --request POST 'http://127.0.0.1:8000/api/v1/token/' 
--header 'Content-Type: application/json' 
--data-raw '{  "username": "admin",  "password": "admin"}'`
###ответ
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDU4NTM1NSwianRpIjoiNGY5YTc5ZmZmNDEzNDM5NmJlNjhlZTVhNjk4MWNjMDgiLCJ1c2VyX2lkIjoxfQ.9pi-sEjkVsU7yxnP26Xvf-E98CVp9HgRvE_sHI7Mi_E",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwNDk5MjU1LCJqdGkiOiI3N2Q1MWNmNWM1ZGU0YzBmYjE3MDVlMDgzYjU4YjYyMSIsInVzZXJfaWQiOjF9.jPP3p030SSA4H72m1JpElYh-R-bF20CBcLwnxI7Lxjs"
}
```
##Получение списка городов
`curl --location --request GET 'http://127.0.0.1:8000/api/v1/cities/' 
--header 'Content-Type: application/json'`

```json
[
  {
    "id": 1,
    "name": "Москва",
    "is_primary": true
  },
  {
    "id": 2,
    "name": "Воронеж",
    "is_primary": false
  }
]
```

##
###запрос
``
###ответ
```
```

##
###запрос
``
###ответ
```
```