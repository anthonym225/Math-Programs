import java.util.Scanner;
public class RadiusSolver{

  public static void findRadius(double x, double h, double y, double k){
    double radius;

    radius = Math.sqrt(Math.pow((x-h),2) + Math.pow((y-k),2));
    System.out.println("The radius of the circle is: " + radius);

  }


  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);

    System.out.println("Enter X value: ");
    double x = scan.nextDouble();

    System.out.println("Enter H value: ");
    double h = scan.nextDouble();

    System.out.println("Enter Y value: ");
    double y = scan.nextDouble();

    System.out.println("Enter K value: ");
    double k = scan.nextDouble();

    scan.close();

    findRadius(x,h,y,k);
  }
}
