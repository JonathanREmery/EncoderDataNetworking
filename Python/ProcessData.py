import math

# ProcessData class to process the raw data received from the robot
class ProcessData():

    # Takes in the data received from the robot in string form and returns a nice and organized dictionary
    @staticmethod
    def parseData(data):
        try:
            data = str(data).replace('b\'','').replace('\'','')
            parsed = data.split(',')
            parsedData = {}
            for x in parsed:
                parsedData[x.split(':')[0]] = float(x.split(':')[1])
            return parsedData
        except:
            return {'leftEncoderValue':math.nan, 'rightEncoderValue':math.nan, 'leftEncoderVelocity':math.nan, 'rightEncoderVelocity':math.nan, 'leftEncoderAcceleration':math.nan, 'rightEncoderAcceleration':math.nan}
