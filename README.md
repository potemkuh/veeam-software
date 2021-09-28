# veeam-software тестовое задание
Написать программу, которая будет синхронизировать два каталога: каталог-источник и каталог-реплику. Задача программы – приводить содержимое каталога-реплики в соответствие содержимому каталога-источника.
Требования:
Сихронизация должна быть односторонней: после завершения процесса синхронизации содержимое каталога-реплики должно в точности соответствовать содержимому каталогу-источника;
Синхронизация должна производиться периодически;
Операции создания/копирования/удаления объектов должны логироваться в файле и выводиться в консоль;
Пути к каталогам, интервал синхронизации и путь к файлу логирования должны задаваться параметрами командной строки при запуске программы.
