package pcse002_assignment_solo;
import javax.swing.JOptionPane;

public class Calculator {
    public static void main(String [] args) {
         Object[] operation = { "Addition", "Substraction", "Multiplication", "Division", "Remainder" };
         var selectedOperator = JOptionPane.showOptionDialog(null, "Select an operation", "Calculator", 
                 JOptionPane.YES_NO_CANCEL_OPTION, 3, null, operation, operation[0]);
         
         String value1Selection = JOptionPane.showInputDialog("Enter the first value.");
         String value2Selection = JOptionPane.showInputDialog("Enter the second value.");
         
         double value1 = Double.parseDouble(value1Selection);
         double value2 = Double.parseDouble(value2Selection);
         double answer = 0;
         
         if (value2 == 0 && selectedOperator == 3 || selectedOperator == 4) {
             JOptionPane.showMessageDialog(null, "Arithmetic error, 2nd value can not be 0 for this operation.");
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
         System.out.println(value1 + " " + value2 + " " + selectedOperator);
         }}
