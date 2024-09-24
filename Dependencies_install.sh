#!/bin/bash

# Actualizar el índice de paquetes
sudo apt update

# Instalar pip si no está instalado
if ! command -v pip &> /dev/null; then
    echo "pip no está instalado. Instalando pip..."
    sudo apt install python3-pip -y
fi

# Instalar las bibliotecas matplotlib y networkx
echo "Instalando matplotlib y networkx..."
pip install matplotlib networkx

echo "Instalación completada."