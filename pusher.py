def main():
    while True:
        print "This is it!"
    sleep(2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
