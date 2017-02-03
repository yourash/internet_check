import sh
from os import path
from time import sleep, gmtime, strftime


def logwriter(log):
    log = str(log)
    if path.exists('internet_logs/logs.txt'):
        with open('internet_logs/logs.txt', "a") as logfile:
            logfile.write(log + '\n')
    else:
        with open('internet_logs/logs.txt', "w") as logfile:
            logfile.write(log + '\n')


def ping():
    stdout = None
    current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    try:
        stdout = sh.ping("-c 4", "ex.ua")
    except Exception:
        log = current_time + " : ERROR NO INTERNET CONNECTION"
    finally:
        if stdout is not None:
            if "0% packet loss" in str(stdout):
                log = current_time + " : OK"
            else:
                log = current_time + " : unstable internet connection"
        logwriter(log)
        print(log)


def main():
    while True:
        ping()
        sleep(300)

if __name__ == '__main__':
    main()
