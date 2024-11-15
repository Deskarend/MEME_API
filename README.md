# Test_MEME_API
## Автотесты для API, хранящей мемы
### Реализованные сценарии

Созданы API-тесты, покрывающие функционал `Авторизация пользователя`, `Проверка токена авторизации`, `Получение списка всех мемов`, 
`Получение одного мема`,`Добавление нового мема`, `Изменение существующего мема`, `Удаление мема`

### Структура проекта

- `endpoints` - пакет, содержащий проект(фреймворк)
- `tests` - пакет, содержащий тесты, разделенные по классам

### Запуск автотестов
**Установка зависимостей**
> `$ pip install -r requirements.txt`  

**Запуск автотестов и генерирование Allure-отчета**
>  `$ pytest tests --alluredir=allure-results`

**Формирование отчёта в формате веб-страницы**
> `$ allure serve allure_results`

**Генерирование отчёта в формате веб-страницы в одном файле**
> `$ allure generate --single-file allure-results`

### Failed tests:
>**TestAuthorize:**    
> 
>`test_authorize_with_empty_name`  
**Регистрация с именем в виде пустой строки ""**
>
>`test_authorize_without_payload`  
**500 ошибка при авторизации без тела**   

>**TestAddNewMem:**    
> 
>`test_add_a_new_meme_without_payload`  
**500 ошибка при добавлении мема без тела**
> 
> `test_add_a_new_meme_with_empty_text_field`  
 **Добавление мема с пустым текстом ''**
> 
> `test_add_a_new_meme_with_empty_url_field`  
 **Добавление мема с пустым url'ом ''**
> 
> `test_add_a_new_meme_with_empty_tags_field`  
 **Добавление мема с пустым tags [ ]**
> 
> `test_add_a_new_meme_with_empty_info_field`  
 **Добавление мема с пустым info {}**
 
>**TestEditMeme:**    
> 
>`test_edit_the_meme_without_payload`  
**500 ошибка при изменении мема без тела**
> 
> `test_edit_the_meme_with_empty_info_field`  
 **Изменение мема с пустым info {}**

