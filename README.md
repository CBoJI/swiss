
===============================================================================

Внимание! Изменен алгоритм работы: теперь клиент не получает STUN-данные.

===============================================================================

Напишите на Python простой клиентский и серверный скрипт для передачи
текстового сообщения от клиента к серверу через интернет.

Считаем что клиент и сервер подключены к интернет. Сервер и клиент
находятся за Full Cone NAT. Иными словами и сервер и клиент не имеют прямых IP
адресов, а находятся в разных городах с типом соединения Full Cone NAT. Для
координации передачи можно использовать любой STUN сервер в т.ч. и бесплатный и
любой сигнальный сервер в т.ч. и бесплатный. Передача должна происходить peer 2
peer, без прохождения сообщения через промежуточный сервер. Можно использовать
только STUN и сигнальный сервер для того чтобы пиры нашли друг друга.

===============================================================================

Реализовано на Python2.7
Для работы необходима библиотека pystun

pip install -r requirements.txt

Перед началом работы отредактируйте настройки config.py:

SIGNAL_SERVER_IP = '188.166.1.106'  # расположен на "белом" IP, можно не изменять

==========================================================

запуск:

1) python signal_server.py  (если не изменяли SIGNAL_SERVER_IP, то не выполняйте 1 пункт)

2) python server.py

3) python client.py

