# Русский язык

## Что это?
Это бот телеграмм для пепередачи файлов между людьми (анонимно) с помощью бота используя сгенерированный токен

## Установка
+ Скачайте файлы бота
+ Скачайте кастомное логирование по этой ссылке
    + https://github.com/AsQqqq/python_log_system
+ Положите custom_logging в папку с проектом

## Перед началом
+ Зайдите в папку setting
    + Создайте в ней файл config.py
        + Создайте в этом файле переменную API и укажите там API от своего бота
        + Так же укажите путь до вашей базы данных. Пример:
            + ```database_path = f'database/database_folder/database.db'```
+ Создайте папку database_folder в папке database
+ Создайте виртуальное окружение для вашего бота и импортируйте 2 библеотеки
    + ```pip install aiogram```
    + ```pip install colorama```
+ Настройте файл custom_logging.py
    + Внутри файла есть конфиги

# English

## What is it?
This is a telegram bot for transferring files between people (anonymously) using a bot using a generated token

## Installation
+ Download the bot files
+ Download custom logging from this link
    + https://github.com/AsQqqq/python_log_system
+ Put custom_logging in the project folder

## Before starting
+ Go to the setting folder
    + Create a file in it config.py
        + Create an API variable in this file and specify the API from your bot there
        + Also specify the path to your database. Example:
            + ```database_path = f'database/database_folder/database.db'```
+ Create a virtual environment for your bot and import 2 bible libraries
    + ```pip install aiogram```
    + ```pip install colorama```
+ Configure the file custom_logging.py
+ There are configs inside the file

------

## Этапы

+ Сделать бота телеграмм(запуск) ✔️
+ Сделать ответ на команду /start ✔️
+ Сделать ответ на все сообщения ✔️
+ Создать базу данных ✔️
+ Создать внос пользователя внутрь ✔️
+ Сделать проверку на изменения каких либо данных у пользователя ✔️
+ Сделать тестовую кнопку ✔️
+ Сделать меню ✔️
+ Сделать систему состояний ✔️
+ Сделать систему сообщений ✔️
+ Сделать бэкенд кнопок ❌
+ Сделать загрузку данных через кнопку в базу данных ❌
+ Сделать генерацию токенов для данных ❌
+ Сделать оформление хранимых данных (возможно называть файлы например) ❌
+ Сделать удаление данных пользователем ❌
+ Сделать загрузку данных по токену другим пользователем ❌
+ Сделать временную жизнь файлам (24 часа) ❌
+ Сделать генерации ссылки на файл ❌

## Stages

+ Make a telegram bot (launch) ✔️
+ Make a response to the /start command ✔️
+ Make a reply to all messages ✔️
+ Create a database ✔️
+ Create a user entry inside ✔️
+ Make a check for changes to any data from the user ✔️
+ Make a test button ✔️
+ Make a menu ✔️
+ Make a system of states ✔️
+ Make a message system ✔️
+ Make a backend of buttons ❌
+ Upload data via the button to the database ❌
+ Generate tokens for data ❌
+ Make the design of the stored data (it is possible to name files for example) ❌
+ Make data deletion by the user ❌
+ Make the token data upload by another user ❌
+ Make temporary files live (24 hours) ❌
+ Make a file link generation ❌