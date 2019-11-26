import math

# ProcessData class to process the raw data received from the robot
class ProcessData():

    # Takes in the data received from the robot in string form and returns a nice and organized dictionary
    @staticmethod
    def parseData(data):
        try:
            parsed = data.split(',')
            parsedData = {}
            for x in parsed:
                parsedData[str(x.split(':')[0]).replace("b\'", "")] = float(x.split(':')[1].replace('\\n\'', ''))
            return parsedData
        except:
            return {'leftEncoderValue':math.nan, 'rightEncoderValue':math.nan, 'leftEncoderVelocity':math.nan, 'rightEncoderVelocity':math.nan, 'leftEncoderAcceleration':math.nan, 'rightEncoderAcceleration':math.nan}
