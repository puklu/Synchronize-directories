import argparse
import sys
from pathlib import Path
import logging
import schedule
import time

from synchronize import synchronize
from helper import remove_extension


def main():
    parser = argparse.ArgumentParser(description='Tool to synchronize two folders')
    parser.add_argument('-src', help="Path to the source folder")
    parser.add_argument('-rep', help="Path to the replica folder", default="../replica_dir")
    parser.add_argument('-sync', help="Sync interval in minutes", default=30)
    parser.add_argument('-logf', help="Path to log file", default="../logfile")
    args = parser.parse_args()

    src_path = Path(args.src)
    if not src_path.is_dir():
        print("Source directory doesn't exist, please provide a valid path to the source directory!")
        return

    replica_path = Path(args.rep)

    logfile_path = Path(args.logf)
    logfile_path = remove_extension(logfile_path) # logfile will be saved with extension ".log" always

    try:
        logging.basicConfig(filename=f"{logfile_path}.log", level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        sync_interval = float(args.sync)

        # synchronize(src_path, replica_path)
        schedule.every(sync_interval).minutes.do(synchronize, src_path, replica_path)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Invalid interval value!!")
        return

    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Exiting...")
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)

    except PermissionError as e:
        print(f"Permission error occurred, please change the parameters accordingly: {e}")

    except Exception as e:
        print("An unknown error occurred:", e)


if __name__ == '__main__':
    print("\n\n\n")
    print("  ***  Welcome to the Synchronize Directories tool  ***  ")
    print(" # The program will run until interrupted by the user (eg using ctrl+c) # ")
    print("\n")
    main()


