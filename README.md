# Comment API
Commentig Backend Service

What can this app do?
- Creating comments
- Altering comments
- View with pagination(by default 10 objects)
- Listing comments for provided essence


## Requirements

- docker-compose

Make sure that you've installed it properly from https://docs.docker.com/compose/install.



## Usage

Clone it!

```
$ git clone https://github.com/rruss/Comments-API
```


Build containers:



```
$ docker-compose build
```


Run the builded containers:

```
$ docker-compose up
```

Примечание: Для решения использовалось GenericForeignKey, который является сущностью, которая позволяет модели быть связанной с любыми другими моделями. Таким образом у нас будет одна моделька на нескольких типов. Но при использовании GenericForeignKey схема базы данных будет неидеальна, так как усложняет написание и объединение запросов и они становятся некрасивым, потому что само имя таблицы становится значением, которое требуется вычислять. Этот процесс является более сложным и затратным по сравнению с использованием обычных внешних ключей. Он также неудобен в плане оптимизации, особенно при работе с большим количеством объектов. Для Базы Данных использовал SQLite, который прост в использовании, но не рекомендуется для масштабных проектов так как позволяет единовременное исполнение лишь одной операции записи.



Для понимания работы API и тестирования имеется Postman collections.

