#!/usr/bin/env python3
"""
Battery Conservation Mode Toggle - Versão Simples
Para Fedora Gnome em laptops Lenovo IdeaPad
"""

import os
import sys
import subprocess

class BatteryConservationSimple:
    def __init__(self):
        self.conservation_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
        
        # Verificar se o sistema é compatível
        if not self.check_compatibility():
            print("ERRO: Sistema não compatível!")
            print("Este programa funciona apenas em laptops Lenovo IdeaPad com módulo ideapad_laptop carregado.")
            sys.exit(1)
    
    def check_compatibility(self):
        """Verifica se o sistema é compatível"""
        try:
            # Verificar se o módulo ideapad_laptop está carregado
            with open('/proc/modules', 'r') as f:
                modules = f.read()
            if 'ideapad_laptop' not in modules:
                return False
            
            # Verificar se o arquivo de controle existe
            return os.path.exists(self.conservation_path)
        except:
            return False
    
    def get_current_status(self):
        """Obtém o status atual do modo de conservação"""
        try:
            with open(self.conservation_path, 'r') as f:
                status = f.read().strip()
                return int(status)
        except:
            return -1
    
    def show_status(self):
        """Mostra o status atual"""
        current_status = self.get_current_status()
        
        if current_status == -1:
            print("ERRO: Não foi possível ler o status atual")
            return False
        
        status_text = "LIGADO" if current_status == 1 else "DESLIGADO"
        print(f"Status atual do modo de conservação: {status_text} ({current_status})")
        return True
    
    def toggle_conservation_mode(self):
        """Alterna o modo de conservação"""
        current_status = self.get_current_status()
        
        if current_status == -1:
            print("ERRO: Não foi possível ler o status atual")
            return False
        
        # Alternar: se está ligado (1), desligar (0), se está desligado (0), ligar (1)
        new_status = 0 if current_status == 1 else 1
        
        print(f"Alternando modo de conservação...")
        print(f"Status atual: {'LIGADO' if current_status == 1 else 'DESLIGADO'}")
        print(f"Novo status: {'LIGADO' if new_status == 1 else 'DESLIGADO'}")
        
        try:
            # Tentar escrever diretamente (pode funcionar se o usuário tiver permissões)
            with open(self.conservation_path, 'w') as f:
                f.write(str(new_status))
            
            # Verificar se funcionou
            if self.get_current_status() == new_status:
                status_text = "LIGADO" if new_status == 1 else "DESLIGADO"
                print(f"✓ Sucesso! Modo de conservação: {status_text}")
                return True
            else:
                print("✗ Falha ao alterar. Você precisa executar como root.")
                print(f"Tente: sudo python3 {sys.argv[0]} --toggle")
                return False
                
        except PermissionError:
            print("✗ Permissão negada. Você precisa executar como root.")
            print(f"Tente: sudo python3 {sys.argv[0]} --toggle")
            return False
        except Exception as e:
            print(f"✗ Erro: {str(e)}")
            return False

def main():
    print("=== Battery Conservation Toggle ===")
    print()
    
    app = BatteryConservationSimple()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--toggle":
            app.toggle_conservation_mode()
        elif sys.argv[1] == "--status":
            app.show_status()
        elif sys.argv[1] == "--help":
            print("Uso:")
            print(f"  {sys.argv[0]} --status   # Mostrar status atual")
            print(f"  {sys.argv[0]} --toggle   # Alternar modo")
            print(f"  {sys.argv[0]} --help     # Mostrar esta ajuda")
            print()
            print("Para alternar com privilégios:")
            print(f"  sudo {sys.argv[0]} --toggle")
        else:
            print(f"Opção inválida: {sys.argv[1]}")
            print(f"Use: {sys.argv[0]} --help")
    else:
        # Modo interativo
        app.show_status()
        print()
        resposta = input("Deseja alternar o modo de conservação? (s/N): ")
        if resposta.lower() in ['s', 'sim', 'y', 'yes']:
            app.toggle_conservation_mode()

if __name__ == "__main__":
    main()
