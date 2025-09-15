#!/bin/bash

# Script auxiliar para alternar o modo de conservação da bateria
# Deve ser executado com privilégios de root

CONSERVATION_PATH="/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"

if [[ $EUID -ne 0 ]]; then
   echo "ERRO: Este script deve ser executado como root"
   echo "Use: sudo $0 [0|1]"
   exit 1
fi

if [[ ! -f "$CONSERVATION_PATH" ]]; then
    echo "ERRO: Arquivo de controle não encontrado: $CONSERVATION_PATH"
    exit 1
fi

# Se nenhum argumento for fornecido, alternar automaticamente
if [[ $# -eq 0 ]]; then
    current=$(cat "$CONSERVATION_PATH")
    if [[ "$current" == "1" ]]; then
        new_value="0"
    else
        new_value="1"
    fi
else
    new_value="$1"
fi

# Validar valor
if [[ "$new_value" != "0" && "$new_value" != "1" ]]; then
    echo "ERRO: Valor inválido. Use 0 (desligar) ou 1 (ligar)"
    exit 1
fi

# Alterar o modo
echo "$new_value" > "$CONSERVATION_PATH"

if [[ $? -eq 0 ]]; then
    if [[ "$new_value" == "1" ]]; then
        echo "Modo de conservação LIGADO"
    else
        echo "Modo de conservação DESLIGADO"
    fi
else
    echo "ERRO: Falha ao alterar modo de conservação"
    exit 1
fi
