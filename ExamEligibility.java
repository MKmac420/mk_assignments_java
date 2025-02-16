package pcse002_assignment_solo;
import javax.swing.JOptionPane;

public class ExamEligibility {
	public static void main(String[] args) {
		
		String classSum = JOptionPane.showInputDialog(null,
	             "How many classes are there in total?", "",
	             JOptionPane.QUESTION_MESSAGE);
		double classNum = Integer.parseInt(classSum);
		
		String classAttendance = JOptionPane.showInputDialog(null,
	             "How many classes did you attend?", "",
	             JOptionPane.QUESTION_MESSAGE);
		double classesAttended = Integer.parseInt(classAttendance);
		
		String assignment1 = JOptionPane.showInputDialog(null,
	             "Score for assignment 1? (out of 100%)", "",
	             JOptionPane.QUESTION_MESSAGE);
		int asmt1 = Integer.parseInt(assignment1);
		
		String assignment2 = JOptionPane.showInputDialog(null,
	             "Score for assignment 2? (out of 100%)", "",
	             JOptionPane.QUESTION_MESSAGE);
		int asmt2 = Integer.parseInt(assignment2);
		
		String assignment3 = JOptionPane.showInputDialog(null,
	             "Score for assignment 3? (out of 100%)", "",
	             JOptionPane.QUESTION_MESSAGE);
		int asmt3 = Integer.parseInt(assignment3);
		
		int assignmentTotal = ((asmt1 + asmt2 + asmt3) / 3);
		int attendanceTotal = (int)((classesAttended / classNum) * 100); // using type-casting so we dont get decimals
				
		if (assignmentTotal < 50.0 || attendanceTotal < 75.0)
			JOptionPane.showMessageDialog(null, "Unfortunately, you are not eligible for the exam.\nAssignment score: " + assignmentTotal + "%\nAttendance: " + attendanceTotal + "%\nMinimum assignment score: 50%\nMinimum attendance score: 75%");
		else
			JOptionPane.showMessageDialog(null, "Congrats, you are eligible for the exam.\nAssignment score: " + assignmentTotal + "%\nAttendance: " + attendanceTotal + "%\nMinimum assignment score: 50%\nMinimum attendance score: 75%");

			
		
		
		
	}

}
