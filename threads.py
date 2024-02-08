import threading
import time

class AnaThreading(threading.Thread):
    def __init__(self):
        super().__init__()
        self.alt_threading = None
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())


    def run(self):
        with self.pause_cond:
            while True:
                while self.paused:
                    self.pause_cond.wait()

                print("Ana threading çalışıyor.")
                time.sleep(2)


    def pause(self):
        self.paused = True
        self.pause_cond.acquire()


    def resume(self):
        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()

class AltThreading(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        while True:
            print(f"Alt Threading {self.num} çalışıyor.")
            time.sleep(2)

if __name__ == "__main__":
    ana_threading = AnaThreading()
    ana_threading.start()

    alt_threading1 = AltThreading(1)
    alt_threading2 = AltThreading(2)
    alt_threading3 = AltThreading(3)
    alt_threading4 = AltThreading(4)

    while True:
        input("Enter'a basın: Ana threading duracak...")
        ana_threading.pause()

        # Manuel olarak alt threading'leri çalıştır
        alt_threading1.start()
        alt_threading2.start()
        alt_threading3.start()
        alt_threading4.start()

        # Alt threading'lerin tamamlanmasını bekleyin
        alt_threading1.join()
        alt_threading2.join()
        alt_threading3.join()
        alt_threading4.join()

        ana_threading.resume()
