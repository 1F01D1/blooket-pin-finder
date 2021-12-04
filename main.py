import socket
import ssl
import random
import threading
import logging
import json

thread_amount = int(input("Number of Threads: "))


def main():
    for _ in range(10000):
        random_numbers = str(random.randint(100000, 999999))

        ssl_context = ssl.create_default_context()

        sock = socket.socket()
        sock.settimeout(5)
        sock.connect(("api.blooket.com", 443))

        sock = ssl_context.wrap_socket(sock, False, False, False, "api.blooket.com")

        sock.sendall(f"GET /api/firebase/id?id={random_numbers} HTTP/1.1\r\nHost: api.blooket.com\r\n\r\n".encode())
        data = sock.recv(1024).split(b"vegur\r\n\r\n")[1].split(b"\n")[0]

        _data = json.loads(data.decode())

        if _data["success"] != False:
            print("Valid game pin: " + random_numbers)
        else:
            print('Invalid game pin: ' + random_numbers)
        


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    threads = list()
    for index in range(thread_amount):
        logging.info("Main: created and started thread %d.", index)
        x = threading.Thread(target=main(), args=(index,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        logging.info("Main: before joining thread %d.", index)
        thread.join()
        logging.info("Main: thread %d done", index)
