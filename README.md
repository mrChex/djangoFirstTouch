djangoFirstTouch
================

Этот проект создан для того что бы пощупать github, django, backbonejs и coffescript.

Перед развертыванием нужно постановить virtualenv на ваш компьютер, в случае с ubuntu это:
```
$ sudo apt-get install python-virtualenv
```

потом необходимо собрать окружение и все зависимости:
```
$ ./build_end.sh
```

и после чего войти в созданное окружение:
```
$ source ./env/bin/activate
```

строка приглашения станет выглядить так:
```
<DFT> user:djangoFirstTouch$
```

Для запуска проекта достаточно выполнить:
```
./run_dev.sh
```