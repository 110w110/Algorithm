import threading

def startTimer():
    timer = threading.Timer(5, startTimer)
    timer.start()

    print("Timer")
