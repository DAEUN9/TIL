public class test {
    public static void main(String[] args) {
        Mom mom = new Mom();
        Mom son = new Mom();

        if (son instanceof Mom) {
            System.out.println("mom");
        }
        if(son instanceof Son) {
            System.out.println("son");
        }
    }

    public static class Mom {
        public void say() {
            System.out.println("hi");
        }
    }
    public static class Son extends Mom {
        public void say() {
            System.out.println("hi");
        }
    }

}
