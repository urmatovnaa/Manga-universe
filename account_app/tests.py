from django.test import TestCase, Client
from rest_framework.authtoken.models import Token

from account_app.models import Account


class AccountsTest(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            email='first@user.com',
            username='user1',
            password='somepass',
            confirm_password='somepass',
        )
        print('created test user:' + str(self.user))

    def test_register_user(self):
        """
        Тестируем:
        1) Создание юзера
        2) Авторизацию
        3) Сверяем токены
        """
        # ТЕСТ-1: создаем пользователя
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/social/registration/",
            data={
                "email": "email@mail.ru",
                "username": "username2",
                "password": "password24",
                "confirm_password": "password24",
            }
        )
        assert response.status_code == 201

    # ТЕСТ-2: авторизовываемся чтобы server создал токен для клиента
    def test_should_login(self):
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/social/login/",
            data={
                'email': "first@user.com",
                "password": "somepass",
                }
            )
        # после авторизации забираем ответ где хранится токен
        assert response.status_code == 200
        self.assertIn('auth_token', response.data)

        # ТЕСТ-3: получаем id последнего зарегистрированного
        # пользователя и сверяем с тем что был в response
        user = self.User.objects.latest('id')
        # # получаем его токен
        token = Token.objects.get(user=user)
        self.assertEqual(response.data['auth_token'], token.key)

    def test_should_not_login(self):
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/social/login/",
            data={
                'email': "first4@user.com",
                "password": "somepass",
                }
            )
        # после авторизации забираем ответ где хранится токен
        assert response.status_code == 400

    def test_have_not_required_fields_should_fail(self):
        # required fields - email, username, password, confirm_password
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/social/registration/",
            data={
                "email": "testuser@gmail.com",
                "username": " test user "
            }
        )
        print(response.status_code)
        assert response.status_code == 400


