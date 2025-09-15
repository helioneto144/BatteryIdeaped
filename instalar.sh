#!/bin/bash

# Script de instalação do Battery Conservation Toggle
# Para Fedora Gnome com laptops Lenovo IdeaPad

echo "=== Instalador do Battery Conservation Toggle ==="
echo

# Verificar se está executando como root
if [[ $EUID -eq 0 ]]; then
   echo "ERRO: Não execute este script como root!"
   echo "Execute como usuário normal. O script pedirá senha quando necessário."
   exit 1
fi

# Verificar se o módulo ideapad_laptop está carregado
echo "Verificando compatibilidade do sistema..."
if ! grep -q ideapad_laptop /proc/modules; then
    echo "ERRO: Módulo ideapad_laptop não encontrado!"
    echo "Este programa é compatível apenas com laptops Lenovo IdeaPad."
    exit 1
fi

# Verificar se o arquivo de controle existe
CONSERVATION_PATH="/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
if [[ ! -f "$CONSERVATION_PATH" ]]; then
    echo "ERRO: Arquivo de controle não encontrado: $CONSERVATION_PATH"
    echo "Seu laptop pode não suportar o modo de conservação da bateria."
    exit 1
fi

echo "✓ Sistema compatível detectado!"
echo

# Verificar dependências
echo "Verificando dependências..."

# Verificar Python3
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python3 não encontrado!"
    echo "Instale com: sudo dnf install python3"
    exit 1
fi

# Verificar PyGObject
if ! python3 -c "import gi" &> /dev/null; then
    echo "ERRO: PyGObject não encontrado!"
    echo "Instale com: sudo dnf install python3-gobject gtk3-devel"
    exit 1
fi

# Verificar pkexec
if ! command -v pkexec &> /dev/null; then
    echo "ERRO: pkexec não encontrado!"
    echo "Instale com: sudo dnf install polkit"
    exit 1
fi

echo "✓ Todas as dependências encontradas!"
echo

# Copiar arquivos
echo "Instalando arquivos..."

# Copiar script principal
sudo cp battery_conservation_toggle.py /usr/local/bin/
sudo chmod +x /usr/local/bin/battery_conservation_toggle.py

# Copiar arquivo .desktop
sudo cp battery_conservation.desktop /usr/share/applications/

# Atualizar cache de aplicações
if command -v update-desktop-database &> /dev/null; then
    sudo update-desktop-database /usr/share/applications/
fi

echo "✓ Instalação concluída!"
echo

# Testar instalação
echo "Testando instalação..."
if /usr/local/bin/battery_conservation_toggle.py --toggle; then
    echo "✓ Teste realizado com sucesso!"
else
    echo "⚠ Teste falhou, mas a instalação foi concluída."
fi

echo
echo "=== INSTALAÇÃO CONCLUÍDA ==="
echo
echo "Como usar:"
echo "1. Procure por 'Battery Conservation' no menu de aplicações"
echo "2. Ou execute: battery_conservation_toggle.py"
echo "3. Para alternar rapidamente: battery_conservation_toggle.py --toggle"
echo
echo "O aplicativo aparecerá no menu de aplicações do Gnome."
echo "Você pode adicionar um atalho de teclado nas configurações do sistema."
echo
