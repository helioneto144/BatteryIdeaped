#!/usr/bin/env python3
"""
Battery Conservation Mode Toggle for Fedora Gnome
Controla o modo de conservação da bateria em laptops Lenovo IdeaPad
"""

import os
import sys
import subprocess
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, Notify, GLib

class BatteryConservationToggle:
    def __init__(self):
        self.conservation_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
        
        # Inicializar notificações
        Notify.init("Battery Conservation")
        
        # Verificar se o sistema é compatível
        if not self.check_compatibility():
            self.show_error("Sistema não compatível ou módulo ideapad_acpi não carregado")
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
    
    def toggle_conservation_mode(self):
        """Alterna o modo de conservação"""
        current_status = self.get_current_status()

        if current_status == -1:
            self.show_error("Erro ao ler status atual")
            return False

        # Alternar: se está ligado (1), desligar (0), se está desligado (0), ligar (1)
        new_status = 0 if current_status == 1 else 1

        try:
            # Tentar usar pkexec primeiro
            cmd = f"echo {new_status} | tee {self.conservation_path}"

            # Verificar se pkexec existe
            pkexec_paths = ['/usr/bin/pkexec', '/bin/pkexec', '/usr/local/bin/pkexec']
            pkexec_path = None
            for path in pkexec_paths:
                if os.path.exists(path):
                    pkexec_path = path
                    break

            if pkexec_path:
                result = subprocess.run([pkexec_path, 'bash', '-c', cmd],
                                      capture_output=True, text=True)
            else:
                # Fallback para sudo se pkexec não estiver disponível
                result = subprocess.run(['sudo', 'bash', '-c', cmd],
                                      capture_output=True, text=True)

            if result.returncode == 0:
                status_text = "LIGADO" if new_status == 1 else "DESLIGADO"
                self.show_notification(f"Modo de conservação: {status_text}")
                return True
            else:
                self.show_error("Erro ao alterar modo de conservação")
                return False
        except Exception as e:
            self.show_error(f"Erro: {str(e)}")
            return False
    
    def show_notification(self, message):
        """Mostra notificação no sistema"""
        try:
            notification = Notify.Notification.new("Battery Conservation", message, "battery")
            notification.show()
        except:
            print(message)
    
    def show_error(self, message):
        """Mostra erro"""
        try:
            notification = Notify.Notification.new("Battery Conservation - Erro", message, "dialog-error")
            notification.show()
        except:
            print(f"ERRO: {message}")
    
    def show_status_dialog(self):
        """Mostra diálogo com status atual e opção de alternar"""
        current_status = self.get_current_status()
        
        if current_status == -1:
            self.show_error("Erro ao ler status atual")
            return
        
        status_text = "LIGADO" if current_status == 1 else "DESLIGADO"
        action_text = "Desligar" if current_status == 1 else "Ligar"
        
        dialog = Gtk.MessageDialog(
            transient_for=None,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.YES_NO,
            text=f"Modo de Conservação da Bateria"
        )
        
        dialog.format_secondary_text(
            f"Status atual: {status_text}\n\n"
            f"Deseja {action_text.lower()} o modo de conservação?"
        )
        
        dialog.set_title("Battery Conservation")
        
        response = dialog.run()
        dialog.destroy()
        
        if response == Gtk.ResponseType.YES:
            self.toggle_conservation_mode()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--toggle":
        # Modo silencioso - apenas alterna
        app = BatteryConservationToggle()
        app.toggle_conservation_mode()
    else:
        # Modo interativo - mostra diálogo
        app = BatteryConservationToggle()
        app.show_status_dialog()

if __name__ == "__main__":
    main()
