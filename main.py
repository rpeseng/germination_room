import subprocess

def main():
    try:
        lcd =  LCDController()
        # İlk Python kodunu başlat
        process1 = subprocess.Popen(['python3', '/home/germinationroom/Documents/germination_room/app/update_data.py'])
        # İkinci Python kodunu başlat
        process2 = subprocess.Popen(['python3', '/home/germinationroom/Documents/germination_room/app/rplcdtogpioz.py'])

        process1.wait()
        process2.wait()

    except KeyboardInterrupt:
        # Ctrl+C algılandığında süreçleri öldür
        process1.terminate()
        process2.terminate()
        print("Programdan çıkış yapıldı.")
    except Exception as error:
        print(f"Main python Directory : {error}")

    finally:
        print("Program Komple kapandı.")

if __name__ == "__main__":
    main()