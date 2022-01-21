import multiprocessing
from Hive import Bee, output_path

AMOUNT = 10**9
PRECISION = 2
THREADS = 16


def progress_bar(progress, bar_length = 20):
    arrow   = "-" * int(progress/100 * bar_length - 1) + '>'
    spaces  = " " * (bar_length - len(arrow))
    percent = ("{:."+str(PRECISION)+"f}").format(progress)
    print(f"Progress: [{arrow}{spaces}] {percent} %", end='\r')


def send_unit(from_f, to_f, index):
    last_progress = -1
    report = ""
    for i in range(int(AMOUNT*from_f), int(AMOUNT*to_f)):
        bee = Bee()
        report += bee.explore()
        #if index != finished: continue
        progress = abs(round(
            (i / AMOUNT - from_f)
            / (to_f - from_f)
            * 100
        ,PRECISION))
        if progress > last_progress:
            last_progress = progress
            progress_bar(progress)
            with open(output_path, "a") as f:
                f.write(report)
            report = ""
    with open(output_path, "a") as f:
        f.write(report)
    print(f"Thread {index} finished")


if __name__ == '__main__':
    try:
        with open(output_path, "r") as f:
            instances = f.read().count(":")
            AMOUNT -= instances
    except: pass

    if AMOUNT > 0:
        print(f"Running {AMOUNT} simulations...")
        processes = []
        for i in range(THREADS):
            p = multiprocessing.Process(target=send_unit, args=(i/THREADS,(i+1)/THREADS,i))
            processes.append(p)
            p.start()
            
        for process in processes:
            process.join()
        print("Done")
    
    else:
        print("Not running more simulations")
        print(f"{instances} >= {AMOUNT+instances}")
        









