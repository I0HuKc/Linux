import psutil
import os
import time

from termcolor import colored

def get_proc():

    get_proc_name = []

    def scan():
        while True:
            try:
                i = 0
                os.system('clear')
                print('\x1b[6;30;42mPID\t\tPPID\t\tName\x1b[0m')
                for proc in psutil.process_iter():
                    i +=1
                    print(f' {proc.pid}\t\t {proc.ppid()}\t\t{proc.name()}')
                time.sleep(int(1))
            except Exception as e:
                print(colored(" ERROR:", 'red'), (str(e)))

    scan()
    print(f'Всего процессов запущенно [ \x1b[1;32m{i}\x1b[0m ]')


if __name__ == '__main__':
        try:
            get_proc()
        except Exception as e:
            print(colored(" ERROR:", 'red'), (str(e)))
        except KeyboardInterrupt:
            print('\nПринудительное завершение')
