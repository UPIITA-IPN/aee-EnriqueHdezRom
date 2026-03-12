#!/bin/bash

# Script para ejecutar el algoritmo extendido de Euclides (aee.py)

# Si no hay argumentos, leemos desde la entrada estándar (stdin)
if [ $# -eq 0 ]; then
    input=$(cat)
    set -- $input
fi

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 no está instalado."
    exit 1
fi

# Verificar que se tengan exactamente 2 argumentos
if [ $# -ne 2 ]; then
    echo "Uso incorrecto."
    echo "Ejemplo de uso: ./aee.sh a b"
    exit 1
fi

# Validar que los argumentos sean números enteros
if ! [[ $1 =~ ^-?[0-9]+$ ]] || ! [[ $2 =~ ^-?[0-9]+$ ]]; then
    echo "Error: Los parámetros deben ser números enteros."
    exit 1
fi

# Nombre del archivo Python (asume que está en el mismo directorio)
PYTHON_SCRIPT="aee.py"

# Verificar si el archivo Python existe
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: No se encuentra el archivo $PYTHON_SCRIPT"
    exit 1
fi

# Ejecutar el script Python con los argumentos
python3 "$PYTHON_SCRIPT" "$1" "$2"