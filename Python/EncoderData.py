import math


# EncoderData class to store the values received from the robot
class EncoderData():

    # Intialize all of the values with NaN
    leftEncoderValue = math.nan
    rightEncoderValue = math.nan
    leftEncoderVelocity = math.nan
    rightEncoderVelocity = math.nan
    leftEncoderAcceleration = math.nan
    rightEncoderAcceleration = math.nan

    # EncoderData constructor
    def __init__(self, encoderDataStruct=None):
        # If encoder values are provided when the object is created use those if not then they will just be NaN by default
        if encoderDataStruct != None:
            self.leftEncoderValue = encoderDataStruct['leftEncoderValue']
            self.rightEncoderValue = encoderDataStruct['rightEncoderValue']
            self.leftEncoderVelocity = encoderDataStruct['leftEncoderVelocity']
            self.rightEncoderVelocity = encoderDataStruct['rightEncoderVelocity']
            self.leftEncoderAcceleration = encoderDataStruct['leftEncoderAcceleration']
            self.rightEncoderAcceleration = encoderDataStruct['rightEncoderAcceleration']

    # Set the EncoderData object's values equal to the values provided
    def setEncoderData(self, encoderDataStruct):
        self.leftEncoderValue = encoderDataStruct['leftEncoderValue']
        self.rightEncoderValue = encoderDataStruct['rightEncoderValue']
        self.leftEncoderVelocity = encoderDataStruct['leftEncoderVelocity']
        self.rightEncoderVelocity = encoderDataStruct['rightEncoderVelocity']
        self.leftEncoderAcceleration = encoderDataStruct['leftEncoderAcceleration']
        self.rightEncoderAcceleration = encoderDataStruct['rightEncoderAcceleration']

    # Get the EncoderData object's values as a dictionary
    def getEncoderData(self):
        return {'leftEncoderValue':self.leftEncoderValue, 'rightEncoderValue':self.rightEncoderValue, 'leftEncoderVelocity':self.leftEncoderVelocity, 'rightEncoderVelocity':self.rightEncoderVelocity, 'leftEncoderAcceleration':self.leftEncoderAcceleration, 'rightEncoderAcceleration':self.rightEncoderAcceleration}

    # Get The EncoderData object's leftEncoderValue and rightEncoderValue in a tuple
    def getEncoderValues(self):
        return (self.leftEncoderValue, self.rightEncoderValue)

    # Get The EncoderData object's leftEncoderVelocity and rightEncoderVelocity in a tuple
    def getEncoderVelocities(self):
        return (self.leftEncoderVelocity, self.rightEncoderVelocity)

    # Get The EncoderData object's leftEncoderAcceleration and rightEncoderAcceleration in a tuple
    def getEncoderAccelerations(self):
        return (self.leftEncoderAcceleration, self.rightEncoderAcceleration)