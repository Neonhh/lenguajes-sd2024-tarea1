import java.util.Arrays;
import java.util.Scanner;

public class esMatrizMagica {
    public static void main(String[] args) {

        //Al llamar este programa, se pide la dimension de la matriz
        int n = Integer.parseInt(args[0]);

        if (n == 0){
            System.out.println("No se pueden evaluar los elementos de una matriz vacia.");
            return;
        }

        int[][] A = new int[n][n];
        Scanner sc = new Scanner(System.in);

        //leemos la matriz
        for(int i = 0; i < n; i++){
            System.out.println("Inserte los elementos de la fila " + (i+1) + ".");
            for (int j = 0; j < n; j++){
                System.out.print("Elemento " + (j+1) + ": ");
                A[i][j] = sc.nextInt();
            }
            System.out.println();
        }
        sc.close();
        System.out.println("Matriz ingresada:");
        imprimirMatriz(A);

        if (esMatrizMagica(A)) {
            System.out.println("\nLa matriz es magica!!\n");
        } else {
            System.out.println("\nLa matriz no es magica...\n");
        }
 
    }

    public static void imprimirMatriz(int[][] A){
        for (int[] fila : A){
            System.out.println(Arrays.toString(fila));
        }
    }

    /*
     * Dada una matriz cuadrada A, decidir si A corresponde a una matriz magica
     */
    public static boolean esMatrizMagica(int[][] A){
        //sera muy ingenuo pensar que la suma sera un entero?
        //bueno, esto almacena en suma el resultado de sumar los elementos de la primera fila.
        int suma = Arrays.stream(A[0]).sum();
        int n = A.length;

        //evaluar el resto de sumas correspondientes en A

        //empezamos a sumar las diagonales
        int sumadiag1 = A[0][0], sumadiag2 = A[0][n-1];
        if (sumadiag1 > suma || sumadiag2 > suma) return false;

        //evaluamos la suma de la primera columna para hacer el resto dentro del loop
        //probablemente esto convenga meterlo en una funcion
        int sumacolumna = 0;
        for (int[] fila : A) {
            sumacolumna += fila[0];
            if (sumacolumna > suma) return false;
        }
        if (sumacolumna != suma) return false;
        
        //loop para evaluar las sumas

        for (int i = 1; i < A.length; i++) {
            int sumafila = 0;
            sumacolumna = 0;
            //evaluamos suma en las diagonales
            sumadiag1 += A[i][i];
            sumadiag2 += A[i][n-1-i];
            if (sumadiag1 > suma || sumadiag2 > suma) return false;

            //evaluamos en la i-esima fila
            for (int elemento : A[i]){
                sumafila += elemento;
                if (sumafila > suma) return false;
            }
            if (sumafila != suma) return false;
            
            //evaluamos en la i-esima columna
            for (int[] fila : A) {
                sumacolumna += fila[i];
                if (sumacolumna > suma) return false;
            }
            if (sumacolumna != suma) return false;

        }

        //falta ver si las sumas de las diagonales llegaron al valor deseado
        return ((sumadiag1 == sumadiag2) && (sumadiag1 == suma));
    }

}
