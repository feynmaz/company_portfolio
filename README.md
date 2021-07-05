# company_portfolio

Работает на [Heroku](https://company-potfolio.herokuapp.com/).


## Пользователи

1. Пользователи в системе могут быть авторизованными и неавторизованными. Авторизованные пользователи могут быть администраторами или пользователями без прав администратора.
2. Неавторизованный пользователь может только просматривать профили компаний.
3. Авторизованный пользователь без прав администратора может просматривать и редактировать профили компаний. Редактировать он может только те профили, к которым привязан. Привязку пользователей к профилям компаний осуществляет администратор через панель администрирования (по адресу /admin/users/usercompanyrelationship/). Регистрация пользователя без прав администратора осуществляется через форму на сайте (по адресу /users/register/). 
4. Авторизованный пользователь с правами администратора имеет доступ и к сайту, и к панели администрирования. На сайте он может просматривать профили и редактировать профиль любой компании. На панели администрирования он может добавлять, обновлять, удалять профили компаний, пользователей и связи пользователь-компания. Также администратор может выдать права администрирования любому пользователю (при редактировании поставив чек-бокс Staff status).


## О разработке

1. В системе уже зарегистрированы один администратор и один пользователь без прав администратора.
2. **Запрещено**:
    1. Создавать пользователей через панель администрирования.
    2. Удалять пользователей "admin" и "djangotestuser".
    3. Удалять профили компаний, если их осталось 6.
3. Все остальное желающим ознакомиться с разработкой разрешено.

Данные для входа:

* admin: J4R5LpHYH - администратор
* djangotestuser: ZDTD4xbkD - обычный пользователь

### API

Доступные api url:
* GET: /api/v1/companies/
* GET и PUT для авторизованных: /api/v1/companies/<int:pk>/
