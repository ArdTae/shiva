import socket
import sys
import time
import os
import math
import time
import infsh
from colorama import Fore
def start_menu():
    os.system('cls')
    print(Fore.GREEN + infsh.shiva_baner)
    print(infsh.baner)
    print("[*] Выберите режим работы: ")
    print(infsh.baner)
    print("[1] Абсолютная анонимность \n[2] Частичное P2P\n[3] I2P\n[4] Settings")
    print(infsh.baner)
    menu = input("[*] Введите: ")
    if menu == "1":
        start_anon()
    elif menu == "2":
        start_client()
    elif menu == "3":
        start_i2p()
    elif menu == "4":
        start_sett()
    else:
        print("[!] Вы выбрали неверную комманду. Введите порядковое число комады(например 1, для клиента слушателя)")
        time.sleep(5)
        start_menu
def start_client():
    host = "127.0.0.1"
    port = 12345

    ## Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## Установка таймаута для попыток подключения (5 секунд)
    client_socket.settimeout(5)

    try:
        ## Подключение к серверу
        print(f"[CONNECTING] Подключение к серверу по адресу {host}:{port}...")
        client_socket.connect((host, port))

        ## Сброс таймаута на none для обычной связи
        client_socket.settimeout(None)

        print("[CONNECTED] Подключено к серверу")
    
        while True:

            ## Получение списка пользователей
            print("Список подключений:")
            print("[1] name: apskd\n[2] name: osd\n[3] name: opefw\n[4] Ввести name вручную.")
            data_adres = client_socket.recv(1024)
            if not data_adres:
                print("[!] В данным момент подключений нет. Найдите пользователя сами.")
            print(data_adres.decode)
            message = input("\nВведите сообщение (или 'quit' для выхода): ")

            if message.lower() == 'quit':
                print("[CLOSING] Закрытие соединения по запросу...")
                break
            elif message.lower() == "4":
                print("[!] Вы выбрали режим подключения вручную: ")
                print("[*] Выберите вы будете являться: [1] Клиентом слушателем\n[2] Клиентом инициатором")
                menu_4 = input("")
                if menu_4 == "1":
                    print("[!] Вы выбрали режим слушателя")
                    print("[!] В данном режиме вы являетесь слушателем, вы принимаете подключение от инициатора, вам нужно будет передать данные для подключения инициатору.")
                    connect_list()
                elif menu_4 == "2":
                    print("[!] Вы выбрали режим инициатора")
                    print("[!] В данном режиме вы являетесь инициатором, вам нужно подключиться к клиенту-слушателю.")
                    print("[!] Укажите ip клиента-слушателя: ")
                    connect_to_pl()
                else:
                    print("[!] Вы выбрали неверную комманду. Введите порядковое число комады(например 1, для клиента слушателя)")
                    time.sleep(5)
    except socket.timeout:
        print("[TIMEOUT] Попытка подключения истекла. Запущен ли сервер?(server_error_1)")
        print("[!] Восстановление работы клиента...")
        time.sleep(10)
        start_menu()
    except ConnectionRefusedError:
        print("[REFUSED] Соединение отклонено. Убедитесь, что сервер запущен.(server_error_2)")
        start_menu()
    except KeyboardInterrupt:
        print("\n[INTERRUPT] Клиент завершает работу...")
    except Exception as e:
        print(f"[ERROR1] {e}")
    """Запуск клиента, который подключается к серверу"""
    ## Информация о сервере
        ## Цикл связи
def connect_to_pl():
    print("[!] Вы выбрали режим клиента-инициатора.")
    print("[!] Введите прослушиваемый хост: ")
    pl_ip = input("Введите: ")
    print("[!] Введите прослушиваемый порт: ")
    pl_port = input("Введите: ")
    print("[!] Выполняется попытка подключения... ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_pl:
        try:
            while socket_pl.connect((pl_ip, int(pl_port))):
                try:
                    pl_data = socket_pl.recv(1024)
                    while not pl_data:
                        try:
                            print("[!] Сообщений нет")
                        except:
                            print("Новое сообщение: ", pl_data.decode)
                    print("[!] Успешное подключение. Введите сообщение")
                    message_pl = input("")
                    socket_pl.send(message_pl.encode())
                    print("Введеное сообщение: ", message_pl, "Закодированная версия: ", message_pl.encode)
                except:
                    print("[*] Ошибка подключения.")
        except Exception as e:
            print("[*] Ошибка.", e, "\n")
def connect_list():
    print("[!] Вы выбрали режим клиента-слушателя")
    print("[!] Введите пролушиваемый хост: ")
    list_host = input("[!] Введите: ")
    print("[!] Введите прослушиваемый порт.")
    list_port = input("Введите: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_lis:
        socket_lis.bind((list_host, int(list_port)))
        socket_lis.listen()
        print("[!] Клиент запущен как слушатель.Ожидается подключение...")
        while True:
            print("[!] Найдено подключение.")
            conn, addr = socket_lis.accept()
            list_data = socket_lis.recv(1024)
            while not list_data:
                try:
                    print("[!] Нет сообщений")
                except:
                    print("[!] Новое сообщение:", list_data.decode())
            data = conn.recv(1024)
            print("Получено сообщение: ", data.decode)
            conn.send(b"ask")
# start i2p

def start_i2p():
    print("[!] Перед началом работы, стоит отметить что работа с сетью i2p неподготовленному пользовтелю может показаться сложной, перед началом работы прочитайте на странице git как им пользоваться.")
    print("[!] Вы выбрали режим i2p.")
    
# start anon
def start_anon():
    print("[!] Вы выбрали режим абсолютной анонимномсти")
    print("Выберите каким клиентом вы являетесь: \n[1] Клиент-слушатель \n[2] Клиент-инициатор.")
    anon_menu = input("")
    if anon_menu == "1":
        connect_list()
    elif anon_menu == "2":
        connect_to_pl()
    else:
        print("[!] Вы выбрали неверную комманду. Введите порядковое число комады(например 1, для клиента слушателя)")
        time.sleep(5)
        start_anon()
def start_sett():
    print("-----Settings.-----")
    print(infsh.baner)
    print("[1] Language")
        
                              
if __name__ == "__main__":
    start_menu()
