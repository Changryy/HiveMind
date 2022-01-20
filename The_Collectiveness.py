import multiprocessing
from Hive import Bee, output_path

AMOUNT = 10**9
PRECISION = 3


try:
    with open(output_path, "r") as f:
        AMOUNT -= f.read().count(":")
except: pass


def progress_bar(percent, total, bar_length = 20):
    arrow   = '-' * int(percent/100 * bar_length - 1) + '>'
    spaces  = ' ' * (bar_length - len(arrow))

    print(f"Progress: [{arrow}{spaces}] {percent:.3f} %", end='\r')


def send_unit(from_f, to_f, index):
    last_progress = -1
    for i in range(int(AMOUNT*from_f), int(AMOUNT*to_f)):
        Bee()
        if index != 0: continue
        progress = round((i / AMOUNT - from_f) / (to_f - from_f) * 100, PRECISION)
        if progress > last_progress:
            last_progress = progress
            progress_bar(progress, 100)


if __name__ == '__main__':
    threads = 16

    processes = []
    for i in range(threads):
        p = multiprocessing.Process(target=send_unit, args=(i/threads,(i+1)/threads,i))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()









