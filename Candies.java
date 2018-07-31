import java.util.TreeSet;

public class Candies {
    public int MostK(int[] array, int k){
        int sum = 0, max = Integer.MIN_VALUE;
        TreeSet<Integer> set = new TreeSet<>();
        set.add(0);
        for (int i = 0; i < array.length; i++){
            sum += array[i];
            Integer min = set.ceiling(sum - k);
            if(min != null)
                max = Math.max(max, sum - min);
            set.add(sum);
        }
        return max;
    }

    public  int candies(int[] array, int k, int o){
        int max = Integer.MIN_VALUE, odd_num = 0, left = 1;
        TreeSet<Integer> set = new TreeSet<>();
        set.add(0);
        Integer[] sum = new Integer[array.length + 1];
        sum[0] = 0;
        for(int i = 1;i < array.length + 1;i ++){
            sum[i] = sum[i - 1] + array[i - 1];
        }
        for (int i = 1; i < array.length + 1; i++){
            set.add(sum[i - 1]);
            odd_num += array[i - 1] & 1;
            while (odd_num > o){
                set.remove(sum[left - 1]);
                odd_num -= array[i - 1] & 1;
                left ++;
            }
            Integer min = set.ceiling(sum[i] - k - sum[left - 1]);
            if(min != null)
                max = Math.max(max, sum[i] - sum[left - 1] - min);

        }
        return max;
    }


    public static void main(String[] args) {
        System.out.println("hello");

        int[] array = {-2, 1, 5};
        int k = 4;
        Candies candies = new Candies();
        int res = candies.MostK(array, k);
        System.out.println(res);

        int o = 1;
        int res1 = candies.candies(array, k, o);
        System.out.println(res1);
    }
}

