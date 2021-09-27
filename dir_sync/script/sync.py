from dir_sync.arg_parse import parse
from dir_sync.scan import scan
import time


def main():
    args = parse()
    #print(args.file_logging)
    while True:
        scan(args.directory_source, args.replica_directory)
        time.sleep(args.time)


#scan('/home/grins/veeam-software/111', '/home/grins/veeam-software/112')
if __name__ == '__main__':
    main()
