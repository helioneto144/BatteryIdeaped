#!/bin/bash

# Script de instalação para Battery Conservation Mode Toggle
# Para Fedora Gnome

set -e

echo "=== Instalador do Battery Conservation Mode Toggle ==="
echo

# Verificar se está executando como root
if [[ $EUID -eq 0 ]]; then
   echo "Este script não deve ser executado como root."
   echo "Execute como usuário normal. O sudo será solicitado quando necessário."
   exit 1
fi

# Verificar se o sistema suporta modo de conservação
echo "Verificando suporte do sistema..."

# Verificar módulo ideapad_laptop
if ! lsmod | grep -q ideapad_laptop; then
    echo "ERRO: Módulo ideapad_laptop não encontrado."
    echo "Este programa funciona apenas em laptops Lenovo IdeaPad compatíveis."
    exit 1
fi

# Verificar arquivo de controle
CONSERVATION_PATH="/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
if [[ ! -f "$CONSERVATION_PATH" ]]; then
    echo "ERRO: Arquivo de controle não encontrado: $CONSERVATION_PATH"
    echo "Este sistema pode não suportar modo de conservação da bateria."
    exit 1
fi

echo "✓ Sistema compatível detectado!"
echo

# Verificar dependências
echo "Verificando dependências..."

# Verificar Python 3
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python 3 não encontrado. Instale com:"
    echo "sudo dnf install python3"
    exit 1
fi

# Verificar GTK
if ! python3 -c "import gi; gi.require_version('Gtk', '3.0')" 2>/dev/null; then
    echo "ERRO: GTK 3 para Python não encontrado. Instale com:"
    echo "sudo dnf install python3-gobject gtk3-devel"
    exit 1
fi

# Verificar pkexec (PolicyKit)
if ! command -v pkexec &> /dev/null; then
    echo "ERRO: pkexec não encontrado. Instale com:"
    echo "sudo dnf install polkit"
    exit 1
fi

echo "✓ Todas as dependências encontradas!"
echo

# Instalar arquivos
echo "Instalando arquivos..."

# Copiar script principal
echo "Copiando script principal..."
sudo cp battery_conservation.py /usr/local/bin/
sudo chmod +x /usr/local/bin/battery_conservation.py

# Copiar arquivo .desktop
echo "Instalando entrada do menu..."
sudo cp battery-conservation.desktop /usr/share/applications/
sudo chmod 644 /usr/share/applications/battery-conservation.desktop

# Atualizar cache do desktop
if command -v update-desktop-database &> /dev/null; then
    sudo update-desktop-database /usr/share/applications/
fi

echo "✓ Instalação concluída!"
echo

# Testar status atual
echo "Testando funcionalidade..."
current_status=$(cat "$CONSERVATION_PATH" 2>/dev/null || echo "erro")

if [[ "$current_status" == "1" ]]; then
    echo "Status atual: Modo conservação LIGADO"
elif [[ "$current_status" == "0" ]]; then
    echo "Status atual: Modo conservação DESLIGADO"
else
    echo "AVISO: Não foi possível ler o status atual"
fi

echo
echo "=== Instalação Concluída ==="
echo
echo "O programa foi instalado com sucesso!"
echo
echo "Para usar:"
echo "1. Procure por 'Battery Conservation Mode' no menu de aplicações"
echo "2. Ou execute diretamente: python3 /usr/local/bin/battery_conservation.py"
echo
echo "O programa permite alternar entre:"
echo "- Modo conservação LIGADO: limita carga a 60% (prolonga vida da bateria)"
echo "- Modo conservação DESLIGADO: carga normal até 100%"
echo
