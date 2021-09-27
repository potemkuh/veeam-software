import argparse


def parse():
    parser = argparse.ArgumentParser(description='Sync')
    parser.add_argument('directory_source', type=str)
    parser.add_argument('replica_directory', type=str)
    parser.add_argument('time', type=int)
    parser.add_argument('file_logging', type=str)

    return parser.parse_args()
