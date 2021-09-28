from dir_sync.arg_parse import parse
from dir_sync.scan import scan
import time
import logging


def main():
    args = parse()
    logging.basicConfig(
        filename=args.file_logging,
        format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
        )
    logging.info('Start script sync')
    while True:
        scan(args.directory_source, args.replica_directory)
        time.sleep(args.time)


if __name__ == '__main__':
    main()
