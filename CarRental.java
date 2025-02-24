package pcse002_assignment_solo;
import javax.swing.JOptionPane;

public class CarRental {
	public static void main(String[] args) {
		double car = 0, rental = 0, priceDaily, priceWeekly, priceMonthly;
		String carName = "Null";
		
		int carChoice = 0;
			String carType = JOptionPane.showInputDialog(null,
			             "Choose a car type.\n1. Compact, $30.50 per day\n2. Sedan, $50.00 per day\n3. SUV, $80.96 per day\nPlease input the number only.", "Car type selection",
			             JOptionPane.QUESTION_MESSAGE);
			carChoice = Integer.parseInt(carType);
			if (carChoice <= 0 || carChoice >= 4) {
				JOptionPane.showMessageDialog(null, "Error, invalid car type.");
				return;
			}
		
		
		int rentalChoice = 0;
			String rentalLength = JOptionPane.showInputDialog(null,
			             "Choose rental duration.\n1. Daily, no discount\n2. Weekly, 15% discount\n3. Monthly, 30% discount", "rental duration selection.",
			             JOptionPane.QUESTION_MESSAGE);
			rentalChoice = Integer.parseInt(rentalLength);
			if (rentalChoice <= 0 || rentalChoice >= 4) {
				JOptionPane.showMessageDialog(null, "Error, invalid duration length.");
				return;
			}
			
		switch (carChoice) {
		case 1:
		car = 30.50;
		carName = "Compact";
		break;
		case 2:
		car = 50.00;
		carName = "Sedan";
		break;
		case 3:
		car = 80.96;
		carName = "SUV";
		break;
		}
		
		switch (rentalChoice) {
		case 1:
		rental = 1.0;
		break;
		case 2:
		rental = 0.85;
		break;
		case 3:
		rental = 0.70;
		break;}
		
		priceDaily = Math.round(car * rental * 100.0) / 100.0;
		int display = (int)(rental * 100); // "switch" does not support double variables
		
		switch (display) {
		case 100:  // if the user chose daily
				JOptionPane.showMessageDialog(null, "Price for " + carName + " type car is $" + priceDaily + " per day.");
		break;
		
		case 85: // if the user chose weekly
				priceWeekly = Math.round(car * rental * 7 * 100.0) / 100.0;
				JOptionPane.showMessageDialog(null, "Price for " + carName + " type car is $" + priceDaily + " per day or $" + priceWeekly + " per week.");
		break;
		
		case 70: // if the user chose monthly
				priceMonthly = Math.round(car * rental * 30 * 100.0) / 100.0;
				JOptionPane.showMessageDialog(null, "Price for " + carName + " type car is $" + priceDaily + " per day or $" + priceMonthly + " per month.");
		break;
		
		}
	}
}
