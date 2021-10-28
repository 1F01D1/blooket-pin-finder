# glizzz_y

import random
import requests
import threading

thread_amount = int(input("Number of Threads: "))


def main():
    for _ in range(10000):
        random_numbers = str(random.randint(100000, 999999))

        response = requests.get(
            f"https://api.blooket.com/api/firebase/id?id={random_numbers}")
        data = response.json()

        if data["success"] == True:
            print('Valid Game Pin: ' + random_numbers)
        else:
            print('Invalid Game Pin: ' + random_numbers)


if __name__ == "__main__":
    threads = list()

    for index in range(thread_amount):
        _ = threading.Thread(target=main())

        threads.append(_)

        _.start()

    for index, thread in enumerate(threads):
        thread.join()
