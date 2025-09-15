#!/usr/bin/env python3
"""
Script de teste para verificar se o sistema suporta modo de conservação da bateria
"""

import os
import subprocess

def verificar_sistema():
    print("=== Teste de Compatibilidade ===")
    print()
    
    # Verificar módulo ideapad_laptop
    print("1. Verificando módulo ideapad_laptop...")
    try:
        with open('/proc/modules', 'r') as f:
            modules = f.read()

        if 'ideapad_laptop' in modules:
            print("✓ Módulo ideapad_laptop encontrado")
        else:
            print("✗ Módulo ideapad_laptop NÃO encontrado")
            print("   Este programa é compatível apenas com laptops Lenovo IdeaPad")
            return False
    except Exception as e:
        print(f"✗ Erro ao verificar módulos: {e}")
        return False
    
    # Verificar arquivo de controle
    print("2. Verificando arquivo de controle...")
    conservation_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
    if os.path.exists(conservation_path):
        print(f"✓ Arquivo encontrado: {conservation_path}")
    else:
        print(f"✗ Arquivo NÃO encontrado: {conservation_path}")
        return False
    
    # Verificar status atual
    print("3. Verificando status atual...")
    try:
        with open(conservation_path, 'r') as f:
            status = f.read().strip()
            status_text = "LIGADO" if status == "1" else "DESLIGADO"
            print(f"✓ Status atual: {status_text} ({status})")
    except:
        print("✗ Erro ao ler status atual")
        return False
    
    # Verificar dependências Python
    print("4. Verificando dependências Python...")
    try:
        import gi
        gi.require_version('Gtk', '3.0')
        gi.require_version('Notify', '0.7')
        from gi.repository import Gtk, Notify
        print("✓ PyGObject e dependências encontradas")
    except:
        print("✗ PyGObject ou dependências NÃO encontradas")
        print("   Instale com: sudo dnf install python3-gobject gtk3-devel")
        return False
    
    # Verificar pkexec
    print("5. Verificando pkexec...")
    pkexec_found = False
    for path in ['/usr/bin/pkexec', '/bin/pkexec', '/usr/local/bin/pkexec']:
        if os.path.exists(path):
            pkexec_found = True
            break

    if pkexec_found:
        print("✓ pkexec encontrado")
    else:
        print("⚠ pkexec NÃO encontrado")
        print("   Instale com: sudo dnf install polkit")
        print("   O programa ainda pode funcionar, mas precisará de sudo manual")
    
    print()
    if pkexec_found:
        print("✓ SISTEMA TOTALMENTE COMPATÍVEL!")
    else:
        print("✓ SISTEMA COMPATÍVEL (com limitações)!")
        print("  Instale o polkit para melhor experiência: sudo dnf install polkit")
    print("Você pode prosseguir com a instalação.")
    return True

if __name__ == "__main__":
    if verificar_sistema():
        print("\nPara instalar, execute: chmod +x instalar.sh && ./instalar.sh")
    else:
        print("\n✗ Sistema não compatível ou dependências faltando.")
