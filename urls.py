class BaseURL:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

class URL:
    HOME_PAGE_URL = BaseURL.BASE_URL # Домашняя страница
    LOGIN_PAGE_URL = f'{BaseURL.BASE_URL}login' # Страница авторизации
    PROFILE_PAGE_URL = f'{BaseURL.BASE_URL}account/profile' # Страница "Профиль пользователя"
