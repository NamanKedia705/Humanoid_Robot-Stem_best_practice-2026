import threading
import os
import time

def start_voice():
    os.system("python3 voice_runner.py")

def start_app():
    os.system("python3 app_server.py")

def start_screen():
    os.system("python3 touchscreen_ui.py")

if __name__ == "__main__":
    print("Starting robot system...")

    threading.Thread(target=start_voice, daemon=True).start()
    threading.Thread(target=start_app, daemon=True).start()
    threading.Thread(target=start_screen, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down system")
