#!/usr/bin/env python3
"""
Teste simples para verificar funcionalidade do modo de conservação
"""

import subprocess
import sys
from pathlib import Path

def test_conservation_mode():
    conservation_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
    
    print("=== Teste do Modo de Conservação da Bateria ===")
    print()
    
    # Verificar se o arquivo existe
    if not Path(conservation_path).exists():
        print("❌ ERRO: Arquivo de controle não encontrado")
        print(f"   Caminho: {conservation_path}")
        return False
    
    print("✅ Arquivo de controle encontrado")
    
    # Ler status atual
    try:
        with open(conservation_path, 'r') as f:
            current_status = f.read().strip()
        
        print(f"📊 Status atual: {current_status}")
        
        if current_status == "1":
            print("   → Modo conservação LIGADO (bateria limitada a ~60%)")
        elif current_status == "0":
            print("   → Modo conservação DESLIGADO (carga normal até 100%)")
        else:
            print(f"   → Status desconhecido: {current_status}")
        
    except Exception as e:
        print(f"❌ ERRO ao ler status: {e}")
        return False
    
    # Verificar se pkexec está disponível
    try:
        result = subprocess.run(['which', 'pkexec'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ pkexec disponível para elevação de privilégios")
        else:
            print("⚠️  pkexec não encontrado - será necessário para alterar o modo")
    except Exception:
        print("⚠️  Não foi possível verificar pkexec")
    
    print()
    print("=== Teste Concluído ===")
    print()
    print("Para usar o programa:")
    print("1. Execute: python3 battery_conservation.py")
    print("2. Ou instale com: ./install.sh")
    print()
    
    return True

if __name__ == "__main__":
    test_conservation_mode()
