from threading import Thread, Lock
from time import sleep


class Knight(Thread):
    total_enemies = 100
    lock = Lock()  # Создаем lock для синхронизации.

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days_fight = 0

    def run(self):
        enemies_left = Knight.total_enemies
        with Knight.lock:
            print(f"{self.name}, на нас напали!")

        while enemies_left > 0:
            self.days_fight += 1
            enemies_left -= self.power
            if enemies_left < 0:
                enemies_left = 0

            with Knight.lock:
                print(f"{self.name}, сражается {self.days_fight} день(дня)..., осталось {enemies_left} воинов.")
            sleep(1)

        with Knight.lock:
            print(f"{self.name} одержал победу спустя {self.days_fight} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")