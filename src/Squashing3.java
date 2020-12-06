public class Squashing3 {

  @Override
  public int hashCode() {
    return super.hashCode();
  }

  @Override
  public boolean equals(Object obj) {
    return super.equals(obj);
  }

  @Override
  protected void finalize() throws Throwable {
    super.finalize();
  }

  public static void main(String[] args) {

    String s1 = "Hello how are you";
    String s2 = "Ludhiana";
    String s3 = "Patiala";
    String s4 = "India";
    String s5 = "Manesar";

    System.out.println(s1);
    System.out.println(s2);
    System.out.println(s3);
    System.out.println(s1);
    System.out.println(s4);
    System.out.println(s5);


    //change 1
  }

}
