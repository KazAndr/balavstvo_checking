import java.util.Arrays;

public class myFunc {
            static double max = 0;
                private static double array[] = { 0.22, 0.4, 0.92, 1.5, 1.99, 4.5  };

                public static void main(String[] args) {
                                findMax(array);
                                findMin(array);
                                            
                }

                public static double findMax(double[] array) {
                                Arrays.sort(array);
                                max = array[array.length - 1];
                                System.out.println(max);
                                return max;
                                                    
                }

                public static double findMin(double[] array) {
                                double min = array[0];
                                for (int i = 0; i < array.length; i++) {
                                        if (array[i] < array[0]) {
                                                      min = array[i];
                                                                            
                                        }
                                                
                                }
                                        System.out.println(min);
                                        return min;
                }
}
