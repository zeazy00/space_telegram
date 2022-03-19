# Скачивание и отправка фото в telegram

Скачивание картинок раз в сутки с сайтов NASA и SpeceX и отправка фото в telegram

### Как установить

Для работы кода необходимо создать файл .env и поместить туда ключ API NASA, ключ API TELEGRAM, и чат ID TELEGRAM.
```
NASA_API_KEY=bfSjLfaaGlBDOjzUgGUdFgbTCXvNa4bOehyGTfkl
TELEGRAM_TOKEN=2121456781:AAH7f5-Emgli7FfN5Ls-78kKKxua70xMLvo
CHAT_ID=@soxvezdie
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

### Пример работы

```
INFO:root:no spasex links
INFO:root:images from Astronomy Picture of the Day: 28
WARNING:root:errors: 2
INFO:root:images from EPIC: 13
{'id': 2121656931, 'username': 'kdcsozvezdie_bot', 'first_name': '\u200eКГБОУ КДЦ "Созвездие"'}
ok
```
