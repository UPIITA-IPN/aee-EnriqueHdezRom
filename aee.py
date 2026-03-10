def egcd_force_a_gt_b(a: int, b: int):
    """
    Algoritmo extendido de Euclides (robusto).
    Fuerza |a| >= |b| intercambiando si hace falta.
    Retorna (g, x, y) tal que a*x + b*y = g = gcd(a,b), con g >= 0.
    """

    if a == 0 and b == 0:
        raise ValueError("gcd(0,0) no está definido.")

    # Guardar originales (con signo) para verificar al final
    a0, b0 = a, b

    # Para forzar a > b según magnitud
    swapped = False
    if abs(a) < abs(b):
        a, b = b, a
        swapped = True

    # Extended Euclid estándar
    old_r, r = a, b
    old_x, x = 1, 0   # coef de 'a'
    old_y, y = 0, 1   # coef de 'b'

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y

    g = old_r
    xa, yb = old_x, old_y  # coeficientes para los (a,b) ya ordenados

    # Si intercambiamos a y b al inicio, también intercambiamos coeficientes
    if swapped:
        xa, yb = yb, xa

    # Normalizar gcd a positivo
    if g < 0:
        g = -g
        xa = -xa
        yb = -yb

    # Verificación con los originales del usuario
    assert a0 * xa + b0 * yb == g, "No se cumplió a*x + b*y = gcd(a,b)"

    return g, xa, yb


def imprimir_tabla_eea(a: int, b: int):
    """
    Imprime la tabla paso a paso del Algoritmo Extendido de Euclides,
    manteniendo la misma lógica de 'forzar |a| >= |b|' para ser consistente.
    """
    if a == 0 and b == 0:
        print("gcd(0,0) no está definido.")
        return

    a0, b0 = a, b

    swapped = False
    if abs(a) < abs(b):
        a, b = b, a
        swapped = True

    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1

    # Encabezado tipo tabla
    #print("\nTabla (paso a paso):")
    #print(f"{'i':>2} | {'q':>6} | {'old_r':>12} | {'r':>12} | {'old_x':>12} | {'x':>12} | {'old_y':>12} | {'y':>12}")
    #print("-" * 102)

    i = 0
    # Estado inicial (sin q)
    #print(f"{i:>2} | {'-':>6} | {old_r:>12} | {r:>12} | {old_x:>12} | {x:>12} | {old_y:>12} | {y:>12}")

    while r != 0:
        i += 1
        q = old_r // r

        new_r = old_r - q * r
        new_x = old_x - q * x
        new_y = old_y - q * y

        old_r, r = r, new_r
        old_x, x = x, new_x
        old_y, y = y, new_y

        #print(f"{i:>2} | {q:>6} | {old_r:>12} | {r:>12} | {old_x:>12} | {x:>12} | {old_y:>12} | {y:>12}")

    g = old_r
    xa, yb = old_x, old_y

    if swapped:
        xa, yb = yb, xa

    if g < 0:
        g = -g
        xa = -xa
        yb = -yb

    #print("\nResultado del EEA:")
    #print(f"gcd({a0}, {b0}) = {g}")
    #print(f"x = {xa}, y = {yb}")
    #print(f"Verificación: {a0}*({xa}) + {b0}*({yb}) = {a0*xa + b0*yb}")


def pedir_entero(msg: str) -> int:
    while True:
        s = input(msg).strip()
        try:
            return int(s)
        except ValueError:
            print("Entrada inválida.")


def main():
    print(" Algoritmo Extendido de Euclides")
    a = pedir_entero("Ingresa a: ")
    b = pedir_entero("Ingresa b: ")

    # Caso especial: módulo 0 no existe
    if b == 0:
        imprimir_tabla_eea(a, b)
        print("\nNo hay inverso multiplicativo modular.")
        return

    g, x, y = egcd_force_a_gt_b(a, b)

    print("\nResultado:")
    print(f"gcd({a}, {b}) = {g}")

    if g == 1:
        m = abs(b)  # módulo positivo
        inv = x % m  # x es el inverso de a (mod b) cuando gcd=1
        print("\nEl inverso multiplicativo modular:")
        print(f"{a}^(-1) mod {m} = {inv}")
        #print(f"Verificación: ({a} * {inv}) mod {m} = {(a * inv) % m}")
    else:
        # Si no hay inverso, imprime la tabla paso a paso + mensaje pedido
        imprimir_tabla_eea(a, b)
        print("\nNo hay inverso multiplicativo modular.")


if __name__ == "__main__":
    main()