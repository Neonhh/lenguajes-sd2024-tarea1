public class potenciacionModulada {
    public static void main(String[] args) {
        
        //procesando input del usuario, deben ser 3 enteros (asumo que esto se cumple)
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);

        System.out.println("El valor de " + args[0] + "^" + args[1] + " mod " + args[2] + " es: " + potenciacionModulada(a, b, c));
       
    }

    /* 
    dados tres enteros no-negativos a, b, y c, devuelve el valor de a^b mod c
    utilizando la formula recursiva obtenida por propiedades del modulo a la
    potencia
    */
    public static long potenciacionModulada(int a, int b, int c) {
        //caso base
        if (b == 0) {
            return 1;
        } 
        
        //caso recursivo
        return ((a % c) * (potenciacionModulada(a, b - 1, c) % c)) % c;
        
    }
}
