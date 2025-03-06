import javax.swing.JOptionPane;
public class ExamEligibility {
	public static void main(String[] args) {
		double classNum = 0, classesAttended = 0;
		String eligibilityMessage;
		
		String classSum = JOptionPane.showInputDialog(null,
	             "How many classes are there in total?", "Class total input.",
	             JOptionPane.QUESTION_MESSAGE);
		classNum = Integer.parseInt(classSum);
		
		String classAttendance = JOptionPane.showInputDialog(null,
	             "How many classes did you attend?", "Class attendance input.",
	             JOptionPane.QUESTION_MESSAGE);
		classesAttended = Integer.parseInt(classAttendance);
		if (classNum < classesAttended) {
			JOptionPane.showMessageDialog(null, "Error, number of classes attended cannot be higher than number of classes total.");
			return;
			}

		String assignment1 = JOptionPane.showInputDialog(null,
	             "Score for assignment 1? (out of 100%)", "Assignment 1 score input.",
	             JOptionPane.QUESTION_MESSAGE);
		int asmt1 = Integer.parseInt(assignment1);
		
		String assignment2 = JOptionPane.showInputDialog(null,
	             "Score for assignment 2? (out of 100%)", "Assignment 2 score input.",
	             JOptionPane.QUESTION_MESSAGE);
		int asmt2 = Integer.parseInt(assignment2);
		
		String assignment3 = JOptionPane.showInputDialog(null,
	             "Score for assignment 3? (out of 100%)", "Assignment 3 score input.",
	             JOptionPane.QUESTION_MESSAGE);
		int asmt3 = Integer.parseInt(assignment3);
		
		if (asmt1 > 100 || asmt2 > 100 || asmt3 > 100) {
			JOptionPane.showMessageDialog(null, "Error, assignment score cannot be higher than 100.");
			return;
			}
		else if (asmt1 < 0 || asmt2 < 0 || asmt3 < 0) {
			JOptionPane.showMessageDialog(null, "Error, assignment score cannot be lower than 0.");
			return;
		}
		
		int assignmentTotal = (asmt1 + asmt2 + asmt3);
		int attendanceTotal = (int)((classesAttended / classNum) * 100); // using type-casting so there are no decimals
				
		if (asmt1 + asmt2 + asmt3 >= 150 || attendanceTotal >= 50)
			eligibilityMessage = "Congratulations, you are";
		else
			eligibilityMessage = "Unfortunately, you are not";
		JOptionPane.showMessageDialog(null, eligibilityMessage + " eligible for the exam.\nAttendance: " + attendanceTotal + "%\nAssignment total: " + assignmentTotal + "%\nMinimum attendance: " + "75%\nMinimum assignment total: " + "150%");
		}
	}
