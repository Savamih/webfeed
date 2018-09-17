from time import sleep


def main():
    while True:
        print "Ping"
        sleep(2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
