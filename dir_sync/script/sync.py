from dir_sync.arg_parse import parse
from dir_sync.scan import scan
import time
import logging


def main():
    args = parse()
    file_log = logging.FileHandler(args.file_logging)
    console_out = logging.StreamHandler()

    logging.basicConfig(handlers=(
        file_log, console_out),
        format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
        )
    logging.info('Start script sync')
    while True:
        scan(args.directory_source, args.replica_directory)
        time.sleep(args.time)


if __name__ == '__main__':
    main()
