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


def send_unit(index, shared_progress):
    last_progress = -1
    report = ""
    for i in range(int(AMOUNT / THREADS)):
        bee = Bee()
        report += bee.explore()
        progress = round(i / (AMOUNT/THREADS) * 100, PRECISION)
        if progress > last_progress:
            shared_progress[index] = last_progress = progress
            progress_bar(min(shared_progress))
            with open(output_path, "a") as f:
                f.write(report)
            report = ""
    with open(output_path, "a") as f:
        f.write(report)
    print(f"Process-{index} Completed")


if __name__ == '__main__':
    try:
        with open(output_path, "r") as f:
            instances = f.read().count(":")
            AMOUNT -= instances
    except: pass

    if AMOUNT > 0:
        print(f"Running {AMOUNT} simulations...")
        processes = []
        progress = multiprocessing.Array('d', range(THREADS))
        for i in range(THREADS):
            p = multiprocessing.Process(target=send_unit, args=(i,progress))
            processes.append(p)
            p.start()
        for process in processes:
            process.join()
        print("Done")
    
    else:
        print("Not running more simulations")
        print(f"{instances} >= {AMOUNT+instances}")
        









