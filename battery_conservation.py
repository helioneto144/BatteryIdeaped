#!/usr/bin/env python3
"""
Battery Conservation Mode Toggle for Fedora Gnome
Programa para alternar o modo de conservação da bateria em laptops Lenovo IdeaPad
"""

import gi
import subprocess
import sys
import os
from pathlib import Path

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, GLib, AppIndicator3

class BatteryConservationApp:
    def __init__(self):
        self.conservation_path = "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
        
        # Verificar se o sistema suporta modo de conservação
        if not self.check_system_support():
            self.show_error_dialog("Sistema não suportado", 
                                 "Este sistema não suporta modo de conservação da bateria ou o módulo ideapad_laptop não está carregado.")
            sys.exit(1)
        
        self.setup_ui()
        self.update_status()
    
    def check_system_support(self):
        """Verifica se o sistema suporta modo de conservação"""
        try:
            # Verificar se o módulo ideapad_laptop está carregado
            result = subprocess.run(['lsmod'], capture_output=True, text=True)
            if 'ideapad_laptop' not in result.stdout:
                return False
            
            # Verificar se o arquivo de controle existe
            return Path(self.conservation_path).exists()
        except Exception:
            return False
    
    def setup_ui(self):
        """Configura a interface do usuário"""
        self.window = Gtk.Window()
        self.window.set_title("Modo Conservação da Bateria")
        self.window.set_default_size(400, 200)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect("destroy", Gtk.main_quit)
        
        # Container principal
        vbox = Gtk.VBox(spacing=20)
        vbox.set_margin_left(20)
        vbox.set_margin_right(20)
        vbox.set_margin_top(20)
        vbox.set_margin_bottom(20)
        
        # Título
        title_label = Gtk.Label()
        title_label.set_markup("<b><big>Modo Conservação da Bateria</big></b>")
        vbox.pack_start(title_label, False, False, 0)
        
        # Status atual
        self.status_label = Gtk.Label()
        vbox.pack_start(self.status_label, False, False, 0)
        
        # Botão para alternar
        self.toggle_button = Gtk.Button()
        self.toggle_button.connect("clicked", self.toggle_conservation_mode)
        vbox.pack_start(self.toggle_button, False, False, 0)
        
        # Botão para atualizar status
        refresh_button = Gtk.Button(label="Atualizar Status")
        refresh_button.connect("clicked", self.on_refresh_clicked)
        vbox.pack_start(refresh_button, False, False, 0)
        
        # Informações
        info_label = Gtk.Label()
        info_label.set_markup("<small><i>Modo conservação: limita a carga da bateria a 60%\npara prolongar sua vida útil</i></small>")
        info_label.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(info_label, False, False, 0)
        
        self.window.add(vbox)
    
    def get_conservation_status(self):
        """Obtém o status atual do modo de conservação"""
        try:
            with open(self.conservation_path, 'r') as f:
                status = f.read().strip()
                return int(status)
        except Exception as e:
            print(f"Erro ao ler status: {e}")
            return None
    
    def set_conservation_mode(self, enable):
        """Define o modo de conservação (1 para habilitar, 0 para desabilitar)"""
        try:
            value = "1" if enable else "0"
            cmd = f"echo {value} | sudo tee {self.conservation_path}"
            
            # Executar comando com sudo
            process = subprocess.Popen(['pkexec', 'sh', '-c', cmd], 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                return True
            else:
                print(f"Erro ao definir modo de conservação: {stderr.decode()}")
                return False
        except Exception as e:
            print(f"Erro ao executar comando: {e}")
            return False
    
    def update_status(self):
        """Atualiza o status na interface"""
        status = self.get_conservation_status()
        
        if status is None:
            self.status_label.set_markup("<span color='red'>Erro ao ler status</span>")
            self.toggle_button.set_label("Erro")
            self.toggle_button.set_sensitive(False)
        elif status == 1:
            self.status_label.set_markup("<span color='green'><b>Modo Conservação: LIGADO</b></span>")
            self.toggle_button.set_label("Desligar Modo Conservação")
            self.toggle_button.set_sensitive(True)
        else:
            self.status_label.set_markup("<span color='orange'><b>Modo Conservação: DESLIGADO</b></span>")
            self.toggle_button.set_label("Ligar Modo Conservação")
            self.toggle_button.set_sensitive(True)
    
    def toggle_conservation_mode(self, button):
        """Alterna o modo de conservação"""
        current_status = self.get_conservation_status()
        
        if current_status is None:
            self.show_error_dialog("Erro", "Não foi possível ler o status atual")
            return
        
        # Alternar: se está ligado (1), desligar (0), e vice-versa
        new_status = 0 if current_status == 1 else 1
        
        if self.set_conservation_mode(new_status == 1):
            self.update_status()
            action = "ligado" if new_status == 1 else "desligado"
            self.show_info_dialog("Sucesso", f"Modo conservação {action} com sucesso!")
        else:
            self.show_error_dialog("Erro", "Falha ao alterar modo de conservação.\nVerifique se você tem permissões administrativas.")
    
    def on_refresh_clicked(self, button):
        """Atualiza o status quando o botão refresh é clicado"""
        self.update_status()
    
    def show_error_dialog(self, title, message):
        """Mostra diálogo de erro"""
        dialog = Gtk.MessageDialog(
            transient_for=self.window,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=title
        )
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()
    
    def show_info_dialog(self, title, message):
        """Mostra diálogo de informação"""
        dialog = Gtk.MessageDialog(
            transient_for=self.window,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=title
        )
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()
    
    def run(self):
        """Executa a aplicação"""
        self.window.show_all()
        Gtk.main()

def main():
    app = BatteryConservationApp()
    app.run()

if __name__ == "__main__":
    main()
