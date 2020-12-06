public class Squashing1 {

  public static void main(String[] args) {
    String s = new String("hello world");
    System.out.println(s);
  }

  @Override
  public boolean equals(Object obj) {
    return super.equals(obj);
  }

}
