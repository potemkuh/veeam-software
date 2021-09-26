import arg_parse

def main():
    args = arg_parse.parse()
    print(args.directory_source)
    print(args.replica_directory)
    print(args.time)
    print(args.file_logging)

if __name__ == '__main__':
    main()