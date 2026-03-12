import sys

def egcd_force_a_gt_b(a: int, b: int):
    # (Mantén el código de tu función exactamente igual)
    if a == 0 and b == 0:
        raise ValueError("gcd(0,0) no está definido.")

    a0, b0 = a, b
    swapped = False
    if abs(a) < abs(b):
        a, b = b, a
        swapped = True

    old_r, r = a, b
    old_x, x = 1, 0   
    old_y, y = 0, 1   

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y

    g = old_r
    xa, yb = old_x, old_y  

    if swapped:
        xa, yb = yb, xa

    if g < 0:
        g = -g
        xa = -xa
        yb = -yb

    assert a0 * xa + b0 * yb == g, "No se cumplió a*x + b*y = gcd(a,b)"
    return g, xa, yb


def imprimir_tabla_eea(a: int, b: int):
    # (Mantén el código de tu función exactamente igual)
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
    i = 0

    while r != 0:
        i += 1
        q = old_r // r
        new_r = old_r - q * r
        new_x = old_x - q * x
        new_y = old_y - q * y
        old_r, r = r, new_r
        old_x, x = x, new_x
        old_y, y = y, new_y

    g = old_r
    xa, yb = old_x, old_y

    if swapped:
        xa, yb = yb, xa

    if g < 0:
        g = -g
        xa = -xa
        yb = -yb


def main():
    # Obtener argumentos (omitiendo el nombre del script)
    args = sys.argv[1:]
    
    # Si no hay argumentos en consola, leer desde la entrada estándar
    if len(args) == 0:
        entrada = sys.stdin.read().split()
        args = entrada

    # Validar que tengamos exactamente 2 argumentos
    if len(args) != 2:
        print("Uso incorrecto.")
        print("Ejemplo de uso: python aee.py a b")
        sys.exit(1)

    # Intentar convertir los argumentos a enteros
    try:
        a = int(args[0])
        b = int(args[1])
    except ValueError:
        print("Error: Los parámetros deben ser números enteros.")
        sys.exit(1)

    # Caso especial: módulo 0 no existe
    if b == 0:
        imprimir_tabla_eea(a, b)
        print("No hay inverso multiplicativo modular.")
        return

    g, x, y = egcd_force_a_gt_b(a, b)

    if g == 1:
        m = abs(b)  # módulo positivo
        inv = x % m  # x es el inverso de a (mod b)
        print(inv)
    else:
        imprimir_tabla_eea(a, b)
        print("No hay inverso multiplicativo modular.")


if __name__ == "__main__":
    main()