import javax.swing.*;
import java.awt.*;

public class FitnessLoginPage extends JFrame {

    public FitnessLoginPage() {
        setTitle("21Fitness Login");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel mainPanel = new JPanel(new GridLayout(0, 1, 5, 15));

        JLabel welcomeLabel = new JLabel("Welcome to 21Fitness!");
        welcomeLabel.setFont(new Font("SansSerif", Font.BOLD, 24));
        welcomeLabel.setHorizontalAlignment(SwingConstants.CENTER);

        
        JPanel inputPanel = new JPanel(new GridLayout(2, 2, -100, 8));

        JLabel emailLabel = new JLabel("     Email     ");
        JTextField emailField = new JTextField("aliabu@gmail.com", 15);
        emailField.setHorizontalAlignment(SwingConstants.LEFT);
        emailField.setForeground(Color.GRAY);

        JLabel passwordLabel = new JLabel("     Password     ");
        JTextField passwordField = new JTextField("Must contain 8 letters", 15);
        passwordField.setForeground(Color.GRAY);

        
        inputPanel.add(emailLabel);
        inputPanel.add(emailField);
        inputPanel.add(passwordLabel);
        inputPanel.add(passwordField);

        
        JPanel checkPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JCheckBox rememberCheckBox = new JCheckBox("Always Sign Me In");
        rememberCheckBox.setForeground(Color.BLUE);
        checkPanel.add(rememberCheckBox);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton loginButton = new JButton("Log In");
        buttonPanel.add(loginButton);

        JPanel forgotPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton forgotPasswordLabel = new JButton("Forgot Password");
        forgotPasswordLabel.setForeground(Color.BLUE);
        forgotPanel.add(forgotPasswordLabel);

        
        JSeparator separator = new JSeparator();

        
        JPanel bottomLinksPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 0));
        JButton noAccountButton = new JButton("Don't Have An Account?");
        noAccountButton.setForeground(Color.BLUE);
        
        JButton continueButton = new JButton("Continue Without Signing In");
        continueButton.setForeground(Color.BLUE);
        
        bottomLinksPanel.add(noAccountButton);
        bottomLinksPanel.add(continueButton);

        mainPanel.add(welcomeLabel);
        mainPanel.add(inputPanel);
        mainPanel.add(checkPanel);
        mainPanel.add(buttonPanel);
        mainPanel.add(forgotPanel);
        mainPanel.add(separator);
        mainPanel.add(bottomLinksPanel);

        add(mainPanel, BorderLayout.NORTH);
    }

    public static void main(String[] args) {
            FitnessLoginPage frame = new FitnessLoginPage();
            frame.setSize(380, 700);
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
    }
}
