# tor_bandwidth_check

Утилита позволяет определить самые оптимальные мосты TOR с максимальным banwidth. 
Проверяет bandwidth по хэшу моста.

## Запуск 
1. Собрать список мостов в файл ```bridges.txt```.  Список мостов можно взять из https://bridges.torproject.org/options/ или Telegram каналов https://t.me/tor_bridges и 
https://t.me/GetBridgesBot
2. ``python3 -m pip install -r requirements.txt``
3. ``python3 main.py``
4. После выполнения скрипта в файле ``best_bridges.py`` будут лежать самые оптимальные мосты.
5. Добавить мосты в файл ``torrc``
6. Перезапустить тор: ``sudo systemctl restart tor``

---
Версия Python 3.10