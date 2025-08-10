public class t {
    public static void main(String[] args) {
        final int SIZE = 16;
        int[] arr = new int[SIZE];
        long sum = 0;

        long start = System.currentTimeMillis();

        for (int i = 0; i < 1000000000; i++) {
            sum += i;
            arr[(int)(i % SIZE)] = (arr[(int)(i % SIZE)] + (int)(sum & 0xFF)) % 100;
        }

        long end = System.currentTimeMillis();

        int arrSum = 0;
        for (int v : arr) {
            arrSum += v;
        }

        System.out.println("Sum: " + sum);
        System.out.println("Array checksum: " + arrSum);
        System.out.println("Time: " + ((end - start) / 1000.0) + " seconds");
    }
}
