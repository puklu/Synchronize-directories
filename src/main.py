import argparse
from pathlib import Path
import logging
import schedule
import time

from synchronize import synchronize


def main():
    parser = argparse.ArgumentParser(description='Tool to synchronize two folders')
    parser.add_argument('-src', help="Path to the source folder")
    parser.add_argument('-rep', help="Path to the replica folder")
    parser.add_argument('-sync', help="Sync interval in minutes")
    parser.add_argument('-logf', help="Path to log file")
    args = parser.parse_args()

    src_path = Path(args.src)
    replica_path = Path(args.rep)
    sync_interval = float(args.sync)
    logfile_path = Path(args.logf)

    logging.basicConfig(filename=f"{logfile_path}.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    if not src_path.is_dir():
        src_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"{src_path} created!")
        print(f"{src_path} created!")

    synchronize(src_path, replica_path)

    # schedule.every(sync_interval).minutes.do(synchronize, src_path, replica_path)

    # while True:
    #     schedule.run_pending()
        # time.sleep(1)


if __name__ == '__main__':
    main()


