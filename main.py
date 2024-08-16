
import bluetooth
import json

def main():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(('', bluetooth.PORT_ANY))

    server_socket.listen(1)
    name = server_socket.getsockname()[1]
    uuid = "043f618d-73ab-4878-9264-e34803bd0cd7"

    # bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
    #                        service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
    #                        profiles=[bluetooth.SERIAL_PORT_PROFILE],
    #                        # protocols=[bluetooth.OBEX_UUID]
    #                        )


    print('server on name', name)
    print('...')
    socket, info = server_socket.accept()

    print('OMG???', info)

    while True:
        length_bytes = socket.recv(4) # TODO: check if this is guaranteed to return 4 bytes

        print('got message')

        length = int.from_bytes(length_bytes, byteorder='big')

        print('length is {}', length)

        message_bytes = socket.recv(length)

        message_json = str(message_bytes, 'utf-8')

        message = json.loads(message_json)

        # TODO: do whatever you want with the message
        print(message)

    socket.close()

if __name__ == '__main__':
    main()
