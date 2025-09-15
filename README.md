# 🔋 Battery Conservation Toggle para Laptops Lenovo IdeaPad

Um programa simples e eficiente para controlar o **modo de conservação da bateria** em laptops **Lenovo IdeaPad** no **Fedora Linux** com **Gnome**.

> 💡 **Para todos os usuários de IdeaPad**: Este programa foi criado para facilitar o controle do modo de conservação da bateria, prolongando a vida útil da sua bateria quando você trabalha sempre conectado à energia.

## 🎯 O que faz

- **Liga/Desliga** o modo de conservação da bateria
- **Interface gráfica** integrada ao Gnome
- **Notificações** do sistema
- **Linha de comando** para automação
- **Instalação automática** no sistema

### 🔋 Modo de Conservação:
- **DESLIGADO (0)**: Carregamento normal até 100% - ideal para uso móvel
- **LIGADO (1)**: Carregamento limitado a ~60% - ideal para uso sempre conectado

## 📋 Requisitos

- **Sistema**: Fedora Linux com Gnome
- **Hardware**: Laptop Lenovo IdeaPad compatível
- **Módulo**: `ideapad_laptop` carregado no kernel
- **Dependências**: Python3 (já vem no Fedora)

## 🚀 Instalação Rápida

### 1. Clone o repositório:
```bash
git clone https://github.com/helioneto144/BatteryIdeaped.git
cd BatteryIdeaped
```

### 2. Teste a compatibilidade:
```bash
chmod +x testar.py
./testar.py
```

### 3. Use imediatamente (versão simples):
```bash
chmod +x battery_toggle_simple.py

# Ver status atual
./battery_toggle_simple.py --status

# Alternar modo (vai pedir senha)
sudo ./battery_toggle_simple.py --toggle
```

### 4. Ou instale no sistema (versão completa):
```bash
chmod +x instalar.sh
./instalar.sh
```

## 📱 Como Usar

### ⚡ Método 1: Linha de Comando (Mais Rápido)
```bash
# Verificar status
./battery_toggle_simple.py --status

# Alternar modo
sudo ./battery_toggle_simple.py --toggle

# Modo interativo
./battery_toggle_simple.py
```

### 🖱️ Método 2: Interface Gráfica (Após instalação)
1. Abra o menu de aplicações do Gnome
2. Procure por "**Battery Conservation Toggle**"
3. Clique para alternar o modo

### ⌨️ Método 3: Atalho de Teclado
1. **Configurações** → **Teclado** → **Atalhos Personalizados**
2. Adicione:
   - **Nome**: Battery Conservation
   - **Comando**: `battery_conservation_toggle.py --toggle`
   - **Tecla**: Ctrl+Alt+B (ou sua preferência)

### 💻 Método 4: Comandos Manuais
```bash
# Ver status
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Ligar conservação (como root)
echo 1 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Desligar conservação (como root)
echo 0 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

## 📁 Arquivos do Projeto

- **`battery_toggle_simple.py`** - ⭐ Versão simples recomendada (linha de comando)
- **`battery_conservation_toggle.py`** - Versão completa com interface gráfica
- **`testar.py`** - Script para verificar compatibilidade
- **`instalar.sh`** - Instalador automático
- **`battery_conservation.desktop`** - Arquivo para menu do Gnome
- **`INSTRUCOES_FINAIS.md`** - Guia completo de uso
- **`COMO_USAR.md`** - Instruções detalhadas

## ⚠️ Solução de Problemas

### "Sistema não compatível"
- Verifique se é um laptop **Lenovo IdeaPad**
- Execute: `grep ideapad_laptop /proc/modules`

### "Arquivo de controle não encontrado"
- Seu modelo pode não suportar modo de conservação
- Verifique se existe: `/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode`

### "Permissão negada"
- Use `sudo` para alternar o modo
- Instale polkit para melhor experiência: `sudo dnf install polkit`

## 🛠️ Dependências Opcionais

Para a versão com interface gráfica:
```bash
sudo dnf install python3-gobject gtk3-devel polkit
```

## 🗑️ Desinstalação

```bash
sudo rm /usr/local/bin/battery_conservation_toggle.py
sudo rm /usr/share/applications/battery_conservation.desktop
sudo update-desktop-database /usr/share/applications/
```

## 🤝 Contribuições

- **Issues**: Reporte bugs ou sugestões
- **Pull Requests**: Melhorias são bem-vindas
- **Testes**: Teste em diferentes modelos de IdeaPad

## 📄 Licença

Este projeto é de **domínio público**. Use, modifique e distribua livremente!

## 🎉 Para Usuários de IdeaPad

Este programa foi criado especificamente para facilitar a vida de usuários de laptops Lenovo IdeaPad no Fedora. Se você:

- ✅ Trabalha sempre conectado à energia
- ✅ Quer prolongar a vida da bateria
- ✅ Precisa alternar entre uso móvel e desktop
- ✅ Quer uma interface simples e eficiente

**Este programa é para você!** 🚀

---

⭐ **Se este programa foi útil, deixe uma estrela no repositório!**