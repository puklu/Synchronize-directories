import argparse
from pathlib import Path
import logging
import schedule
import time

from synchronize import synchronize


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
    logging.basicConfig(filename=f"{logfile_path}.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        sync_interval = float(args.sync)
    except:
        print("Invalid interval value!!")
        return

    synchronize(src_path, replica_path)

    # schedule.every(sync_interval).minutes.do(synchronize, src_path, replica_path)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


if __name__ == '__main__':
    main()


