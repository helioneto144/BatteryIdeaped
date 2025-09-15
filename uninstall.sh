#!/bin/bash

# Script de desinstalação para Battery Conservation Mode Toggle

set -e

echo "=== Desinstalador do Battery Conservation Mode Toggle ==="
echo

# Verificar se está executando como root
if [[ $EUID -eq 0 ]]; then
   echo "Este script não deve ser executado como root."
   echo "Execute como usuário normal. O sudo será solicitado quando necessário."
   exit 1
fi

echo "Removendo arquivos instalados..."

# Remover script principal
if [[ -f "/usr/local/bin/battery_conservation.py" ]]; then
    echo "Removendo script principal..."
    sudo rm -f /usr/local/bin/battery_conservation.py
    echo "✓ Script principal removido"
else
    echo "Script principal não encontrado (já removido?)"
fi

# Remover arquivo .desktop
if [[ -f "/usr/share/applications/battery-conservation.desktop" ]]; then
    echo "Removendo entrada do menu..."
    sudo rm -f /usr/share/applications/battery-conservation.desktop
    echo "✓ Entrada do menu removida"
else
    echo "Entrada do menu não encontrada (já removida?)"
fi

# Atualizar cache do desktop
if command -v update-desktop-database &> /dev/null; then
    sudo update-desktop-database /usr/share/applications/
fi

echo
echo "=== Desinstalação Concluída ==="
echo "O Battery Conservation Mode Toggle foi removido do sistema."
echo
