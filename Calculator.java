import javax.swing.JOptionPane;
public class Calculator {
	public static void main(String [] args) {
		double value1 = 0, value2 = 0, answer = 0;	
		 Object[] operations = { "Addition", "Subtraction", "Multiplication", "Division", "Remainder" };
		 int selectedOperator = JOptionPane.showOptionDialog(null, "Select an operation", "Calculator", 
				 JOptionPane.YES_NO_CANCEL_OPTION, JOptionPane.QUESTION_MESSAGE, null, operations, null);

		 String value1Selection = JOptionPane.showInputDialog("Enter the first value.");
		 String value2Selection = JOptionPane.showInputDialog("Enter the second value.");
		 
		 value1 = Double.parseDouble(value1Selection);
		 value2 = Double.parseDouble(value2Selection);
		 
		 if (value2 == 0 && selectedOperator >= 3) {
			 JOptionPane.showMessageDialog(null, "Arithmetic error, 2nd value can not be 0 for this operation.");
		 return;
		 }
		 else if (selectedOperator == -1) {
			 JOptionPane.showMessageDialog(null, "Error, no operation was chosen.");
			 return;
		 }
		 
		 switch (selectedOperator) {
		 case 0:
			 answer = value1 + value2;
			 JOptionPane.showMessageDialog(null, value1 + " + " + value2 + " = " + answer);
		 break;
		 case 1:
			 answer = value1 - value2;
			 JOptionPane.showMessageDialog(null, value1 + " - " + value2 + " = " + answer);
		 break;
		 case 2:
			 answer = value1 * value2;
			 JOptionPane.showMessageDialog(null, value1 + " × " + value2 + " = " + answer);
		 break;
		 case 3:
			 answer = value1 / value2;
			 JOptionPane.showMessageDialog(null, value1 + " ÷ " + value2 + " = " + answer);
		 break;
		 case 4:
			 answer = value1 % value2;
			 JOptionPane.showMessageDialog(null, value1 + " % " + value2 + " = " + answer);
		 break;
		 }
		 }
	}

/*
https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JOptionPane.html
from line 8 to 10 in this code
this code declares an array of "objects" with the object type being "string"
this array stores the "strings" in an index starting from the value "0"
the array name is "operations" and will store the strings listed above
with respect to its positional value as the index value.
This code uses JOptionPane to display an options dialog using
showOptionDialog. This displays the user a set of choices in a dialog box.
It is more preferable as it prevents the user from typing invalid inputs.
The 4th argument's optionType is replaced by the specified "operations" array
The 7th argument specifies the array to be used
The 8th argument specifies the default selected value, null means there will be no
default value.
selectedOperator will store the index value of the selected option as an
integer value from 0 till 4.
If the dialogue box is closed by the user, the integer value will be "-1".
*/
