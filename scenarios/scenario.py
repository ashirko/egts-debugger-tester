import socket, argparse

def port_type(x):
    x = int(x)
    if x < 1024 or x > 65535:
        raise argparse.ArgumentTypeError("Port number must be between 1024 and 65535")
    return x

def start_scenario():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=9090, type=port_type, help="listening port")
    parser.add_argument("--hostname", default='', help="hostname")
    args = parser.parse_args()

    sock = socket.socket()
    sock.connect((args.hostname, args.port))
    return sock