import zmq
from ProcessData import ProcessData
from EncoderData import EncoderData

# Create an EncoderData object which will be storing our values
encoderData = EncoderData()

# Main function of the python code
def main():

    # Create a ZMQ Context
    zContext = zmq.Context()
    # Create a ZMQ SUB Socket
    receiver = zContext.socket(zmq.SUB)
    # Bind the ZMQ SUB Socket to port 12345
    receiver.bind("tcp://0.0.0.0:12345")
    # Subscribe to all topics
    receiver.setsockopt(zmq.SUBSCRIBE, b'')

    while True:

        try:

            # Receive data from the ZMQ SUB Socket
            dataReceived = receiver.recv()

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

main()
