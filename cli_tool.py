import os
import multiprocessing
import platform
import subprocess
from Helpers.title import title


def get_thread_count():
    if platform.system() == "Windows":
        try:
            return int(subprocess.check_output("WMIC CPU Get NumberOfLogicalProcessors", shell=True).decode().split('\n')[1])
        except Exception as e:
            print(f"Error fetching thread count: {e}")
    elif platform.system() == "Linux":
        try:
            return os.cpu_count()
        except Exception as e:
            print(f"Error fetching thread count: {e}")
    else:
        print("Unsupported platform")
        return None

def main():
    print(title)
    while True:
        command = input(">> ")
        if command == "-threads":
            total_threads = get_thread_count()
            if total_threads is not None:
                print(f"Total threads: {total_threads}")
            else:
                print("Unable to determine thread count")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
