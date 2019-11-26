import java.io.*;
import java.net.*;


class EncoderDataSender {

	// These are just made up values, obviously on the actual bot these would be the actual encoder values/velocities/accelerations

	private static double[] encoderTicks = {1395.34, 1384.26};
	private static double[] encoderVelocity = {15.15, 15.12};
	private static double[] encoderAcceleration = {-1.4, -1.5};


	public static void main(String[] argv) throws UnknownHostException, IOException{
		
		try{

			// Intializes a socket to null so that we don't get 'cannot find symbol' error
			Socket s = null;
			boolean connected = false;
			
			// This will keep trying to connect back to the driver station until it is succesful
			while (!connected){
			
				try {
			
					s = new Socket("127.0.0.1", 12345);
					connected = true;
			
				} catch (Exception e){}
			
			}

			// Establishes an output stream to the socket
			PrintWriter out = new PrintWriter(s.getOutputStream(), true);



			// While the socket is not closed it will send the encoder data and then sleep for 10 milliseconds, this was to prevent writing to the output stream to fast.
			while (!s.isClosed()){
			
				out.println(generateDataString(encoderTicks, encoderVelocity, encoderAcceleration));
				out.flush();
				Thread.sleep(10);
			
			}


			// Closes the output stream and socket
			out.close();
			s.close();

		} catch (Exception e){

			// This will catch any errors that may occur

			System.out.println("Error sending data!");

		}
	
	}

	// This method takes in three double arrays and generates a string containing their values
	private static String generateDataString(double[] eT, double[] eV, double[] eA){
		return String.format("leftEncoderValue:%1$.2f,rightEncoderValue:%2$.2f,leftEncoderVelocity:%3$.2f,rightEncoderVelocity:%4$.2f,leftEncoderAcceleration:%5$.2f,rightEncoderAcceleration:%6$.2f", eT[0], eT[1], eV[0], eV[1], eA[0], eA[1]);
	}

}
