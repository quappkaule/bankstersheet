import javax.swing.*;

class Panel{
    public static void main(String args[]){
        JFrame frame = new JFrame("Bankstersheet");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);

        JPanel panel = new JPanel(true);
        frame.getContentPane().add(panel);

        frame.setVisible(true);
    }
}