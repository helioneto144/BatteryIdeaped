# 🔋 Como Usar o Battery Conservation Toggle

## 🚀 Instalação Rápida

### 1. Primeiro, teste se seu sistema é compatível:
```bash
./testar.py
```

### 2. Se o teste passou, instale:
```bash
./instalar.sh
```

## 📱 Formas de Usar

### ✨ Método 1: Menu do Gnome (Recomendado)
1. Pressione a tecla **Super** (Windows)
2. Digite "**battery**" ou "**conserv**"
3. Clique em "**Battery Conservation Toggle**"
4. Escolha **Sim** para alternar o modo

### ⚡ Método 2: Atalho de Teclado (Mais Rápido)
1. Vá em **Configurações** → **Teclado** → **Atalhos de Teclado**
2. Role até o final e clique em **"+"**
3. Configure:
   - **Nome**: Battery Conservation
   - **Comando**: `battery_conservation_toggle.py --toggle`
   - **Atalho**: Pressione **Ctrl+Alt+B** (ou sua preferência)
4. Agora use **Ctrl+Alt+B** para alternar rapidamente!

### 💻 Método 3: Terminal
```bash
# Modo interativo (mostra diálogo)
battery_conservation_toggle.py

# Modo silencioso (apenas alterna)
battery_conservation_toggle.py --toggle

# Verificar status manualmente
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

## 🔋 Entendendo o Modo de Conservação

- **0 (DESLIGADO)**: Carregamento normal até 100%
  - Use quando precisar de máxima autonomia
  - Para viagens ou uso móvel

- **1 (LIGADO)**: Carregamento limitado a ~60%
  - Use quando trabalhar sempre conectado à energia
  - Prolonga a vida útil da bateria
  - Ideal para uso como desktop

## 🔔 Notificações

O programa mostra notificações quando você alterna o modo:
- "Modo de conservação: LIGADO" 
- "Modo de conservação: DESLIGADO"

## ⚠️ Problemas Comuns

### "Sistema não compatível"
- Verifique se é um laptop Lenovo IdeaPad
- Execute: `lsmod | grep ideapad_laptop`

### "Erro ao alterar modo"
- Verifique se o pkexec está instalado
- Tente executar o instalador novamente

### Aplicativo não aparece no menu
- Execute: `sudo update-desktop-database /usr/share/applications/`
- Reinicie o Gnome: **Alt+F2** → digite **r** → **Enter**

## 🗑️ Desinstalar

```bash
sudo rm /usr/local/bin/battery_conservation_toggle.py
sudo rm /usr/share/applications/battery_conservation.desktop
sudo update-desktop-database /usr/share/applications/
```

## 💡 Dicas

1. **Configure um atalho de teclado** para acesso mais rápido
2. **Use o modo conservação** quando trabalhar sempre conectado
3. **Desative antes de viagens** para ter 100% de bateria
4. O programa **lembra sua escolha** até você alternar novamente
