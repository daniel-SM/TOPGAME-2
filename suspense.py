from time import sleep


def make_suspense(suspense_time):
    for _ in range(3):
        print(".")
        sleep(suspense_time)
