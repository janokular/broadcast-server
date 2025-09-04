#!/bin/env python3


from utils.parser import parse_arguments
from src.server import start_server
from src.client import connect_client


def main():
    args = parse_arguments()

    if args.start:
        start_server()
    elif args.connect:
        connect_client()
    else:
        print('error: Something went wrong')

if __name__ == '__main__':
    main()
