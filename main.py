import mouse
import random
import time


def main():
    while True:
        mouse.move(random.randint(0, 1920), random.randint(0, 1080))
        time.sleep(5)   # put your preferable to move the mouse in seconds


if __name__ == '__main__':
    main()