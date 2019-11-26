import socket
from ProcessData import ProcessData
from EncoderData import EncoderData

# Create an EncoderData object which will be storing our values
encoderData = EncoderData()

# Main function of the python code
def main():

    # Create a network socket that the robot can connect to
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Make the socket reuseable so you don't get an 'Address already in use' error
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to 0.0.0.0:12345 and start listening
    conn.bind(('0.0.0.0', 12345))
    conn.listen(1)

    # Accept the incoming connection from the robot
    client, addr = conn.accept()

    while True:

        try:

            # Receive 256 bytes of data from the robot
            dataReceived = str(client.recv(256))

            # Check if the socket is closed and if so break out of the while loop
            if dataReceived=='b\'\'':
                break

            # Set the EncoderData object's values equal to the values we received from the robot
            encoderData.setEncoderData(ProcessData.parseData(dataReceived))

            # Print out the EncoderData object's values
            print("Values: ({}, {})".format(encoderData.getEncoderValues()[0], encoderData.getEncoderValues()[1]))
            print("Velocities: ({}, {})".format(encoderData.getEncoderVelocities()[0], encoderData.getEncoderVelocities()[1]))
            print("Accelerations: ({}, {})".format(encoderData.getEncoderAccelerations()[0], encoderData.getEncoderAccelerations()[1]))
            print()

        except Exception as err:

            # Handle any errors that may occur
            print(type(err))
            break

    # Shutdown the socket
    client.close()
    conn.close()


main()
