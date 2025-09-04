from argparse import ArgumentParser


def parse_arguments():
    '''Parse arguments needed for the program's logic'''
    parser = ArgumentParser(description='Broadcast server that allow clients to send messages to all connected clients')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s',
                       '--start',
                       action='store_true',
                       help='start the server')
    group.add_argument('-c',
                       '--connect',
                       action='store_true',
                       help='connect the client to the server')

    return parser.parse_args()
  
