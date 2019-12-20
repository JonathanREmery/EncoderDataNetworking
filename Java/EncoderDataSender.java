import java.io.*;
import org.zeromq.SocketType;
import org.zeromq.ZMQ;
import org.zeromq.ZContext;

class EncoderDataSender {

	// These are just made up values, obviously on the actual bot these would be the actual encoder values/velocities/accelerations

	private static double[] encoderTicks = {1395.34, 1384.26};
	private static double[] encoderVelocity = {15.15, 15.12};
	private static double[] encoderAcceleration = {-1.4, -1.5};


	public static void main(String[] argv) throws Exception {
		// Try to create a new ZContext
		try (ZContext context = new ZContext()) {
			// Create a new ZMQ PUB Socket
			ZMQ.Socket sender = context.createSocket(ZMQ.PUB);
			// Connect the ZMQ PUB Socket to localhost on port 12345
			sender.connect("tcp://localhost:12345");
			
			// Constantly publish the encoder data to the ZMQ PUB Socket
			while (true){
				sender.send(generateDataString(encoderTicks, encoderVelocity, encoderAcceleration));
			}
		}	
	}

	// This method takes in three double arrays and generates a string containing their values
	private static String generateDataString(double[] eT, double[] eV, double[] eA){
		return String.format("leftEncoderValue:%1$.2f,rightEncoderValue:%2$.2f,leftEncoderVelocity:%3$.2f,rightEncoderVelocity:%4$.2f,leftEncoderAcceleration:%5$.2f,rightEncoderAcceleration:%6$.2f", eT[0], eT[1], eV[0], eV[1], eA[0], eA[1]);
	}

}
