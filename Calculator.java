import javax.swing.JOptionPane;

public class Calculator {
    public static void main(String[] args) {
        double value1 = 0, value2 = 0, answer = 0;
        
        Object[] operations = {"Addition", "Subtraction", "Multiplication", "Division", "Remainder"};
        int selectedOperator = JOptionPane.showOptionDialog(null, "Select an operation", "Calculator", JOptionPane.YES_NO_CANCEL_OPTION, JOptionPane.QUESTION_MESSAGE, null, operations, null);

        String value1Selection = JOptionPane.showInputDialog("Enter the first value.");
        String value2Selection = JOptionPane.showInputDialog("Enter the second value.");

        value1 = Double.parseDouble(value1Selection);
        value2 = Double.parseDouble(value2Selection);

        if (value2 == 0 && selectedOperator >= 3) { // for operators division and remainder
            JOptionPane.showMessageDialog(null, "Arithmetic error, 2nd value can not be 0 for this operation.");
            return;
        }

        switch (selectedOperator) {
            case 0: // addition
                answer = value1 + value2;
                JOptionPane.showMessageDialog(null, value1 + " + " + value2 + " = " + answer);
                break;
            case 1: // subtraction
                answer = value1 - value2;
                JOptionPane.showMessageDialog(null, value1 + " - " + value2 + " = " + answer);
                break;
            case 2: // multiplication
                answer = value1 * value2;
                JOptionPane.showMessageDialog(null, value1 + " × " + value2 + " = " + answer);
                break;
            case 3: // division
                answer = value1 / value2;
                JOptionPane.showMessageDialog(null, value1 + " ÷ " + value2 + " = " + answer);
                break;
            case 4: // remainder
                answer = value1 % value2;
                JOptionPane.showMessageDialog(null, value1 + " % " + value2 + " = " + answer);
                break;
            default: // if the operator menu is closed via the X button
                JOptionPane.showMessageDialog(null, "Error, no operation was chosen.");
                break;
        }
    }
}
