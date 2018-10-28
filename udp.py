import socket


def send(ip, msg):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    # my_socket.sendto(msg.encode(), ('<broadcast>', 8988))
    try:
        my_socket.sendto(msg.encode(), (ip, 8988))
    except:
        pass

    my_socket.close()


def send_message(ip, message):
    msg = "%TEXT% : " + message
    send(ip, msg)


def send_control(ip, control):
    msg = '$' + control + '$'
    send(ip, msg)
