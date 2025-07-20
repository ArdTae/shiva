import socket
import sys
import time
import os
import math
import time
def start_menu():
    os.system('cls')
    print("S-H-I-V-A")
    print("[*] Выберите режим работы: ")
    print("[1] Абсолютная анонимность \n[2] Частичное P2P")
    menu = input("[*] Введите: ")
    if menu == "1":
        print("пыов")
    if menu == "2":
        start_client()
def start_client():
    host = '127.0.0.1'
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
    pl_ip = input("")
    pl_port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_pl:
        try:
            socket_pl.connect((pl_ip, pl_port))
            print("[!] Успешное подключение. Введите сообщение")
            message_pl = input("")
            socket_pl.send(message_pl.encode())
            print("Введеное сообщение: ", message_pl, "Закодированная версия: ", message_pl.encode)
        except Exception as e:
            print("[*] Ошибка.", e, "\n")
def connect_list():
    list_port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_lis:
        socket_lis.bind(("0.0.0.0", list_port))
        socket_lis.listen()
        print("[!] Клиент запущен как слушатель.Ожидается подключение...")
        while True:
            print("[!] Найдено подключение.")
            conn, addr = socket_lis.accept()
            data = conn.recv(1024)
            print("Получено сообщение: ", data.decode)
            conn.send(b"ask")


        

                                
if __name__ == "__main__":
    start_menu()
