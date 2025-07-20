import socket
import threading
import os

def handle_client(client_socket, client_address):
    """Обработка связи с одним клиентом"""
    try:
        print(f"[NEW CONNECTION] {client_address} подключено.")

        while True:
            ## Получение данных от клиента
            try:
                data = client_socket.recv(1024)
                if not data:
                    break  ## Клиент отключился

                message = data.decode()
                print(f"[new] [{client_address}] {message}")

                ## Отправка ответа
                response = f"Сообщение '{message}' получено успешно"
                client_socket.send(response.encode())
                client_socket.send(message.encode())

            except ConnectionResetError:
                print(f"[{client_address}] Соединение сброшено клиентом")
                break

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        ## Очистка при отключении клиента
        client_socket.close()
        print(f"[DISCONNECTED] {client_address} отключено")

def start_server():
    """Запуск сервера и прослушивание соединений"""
    ## Конфигурация сервера
    host = '127.0.0.1'
    port = 12345

    ## Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## Установка опции сокета для повторного использования адреса
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        ## Привязка к хосту и порту
        server_socket.bind((host, port))

        ## Прослушивание соединений
        server_socket.listen(5)
        print(f"[STARTING] Сервер прослушивает {host}:{port}")

        while True:
            ## Принятие клиентского соединения
            client_socket, client_address = server_socket.accept()

            ## Создание нового потока для обработки клиента
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True  ## Поток закроется при выходе из основной программы
            client_thread.start()

            ## Отображение активных соединений
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    except KeyboardInterrupt:
        print("\n[SHUTTING DOWN] Сервер завершает работу...")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        server_socket.close()
        print("[CLOSED] Сокет сервера закрыт")
if __name__ == "__main__":
    start_server()