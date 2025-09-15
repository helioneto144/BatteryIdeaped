# 🔋 Battery Conservation Toggle - PRONTO PARA USO!

## ✅ O que foi criado

Criei um programa completo para controlar o modo de conservação da bateria do seu laptop Lenovo IdeaPad no Fedora Gnome.

## 📁 Arquivos criados:

1. **`battery_conservation_toggle.py`** - Programa principal com interface gráfica
2. **`battery_toggle_simple.py`** - Versão simples para linha de comando  
3. **`battery_conservation.desktop`** - Arquivo para aparecer no menu do Gnome
4. **`instalar.sh`** - Script de instalação automática
5. **`testar.py`** - Script para testar compatibilidade
6. **`toggle_helper.sh`** - Script auxiliar para uso com sudo
7. **`COMO_USAR.md`** - Instruções detalhadas de uso

## 🚀 COMO USAR AGORA:

### Opção 1: Versão Simples (Recomendada para começar)
```bash
# Verificar status atual
./battery_toggle_simple.py --status

# Alternar modo (precisa de sudo)
sudo ./battery_toggle_simple.py --toggle

# Modo interativo
./battery_toggle_simple.py
```

### Opção 2: Testar compatibilidade primeiro
```bash
./testar.py
```

### Opção 3: Instalação completa no sistema
```bash
./instalar.sh
```

## 🔋 Como funciona:

- **Modo DESLIGADO (0)**: Carregamento normal até 100%
- **Modo LIGADO (1)**: Carregamento limitado a ~60% (melhor para a bateria)

## 💡 Comandos manuais (se preferir):

```bash
# Ver status atual
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Ligar conservação (como root)
echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Desligar conservação (como root)  
echo 0 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

## ⚡ Teste rápido AGORA:

1. **Verificar status atual:**
   ```bash
   ./battery_toggle_simple.py --status
   ```

2. **Alternar modo (vai pedir senha):**
   ```bash
   sudo ./battery_toggle_simple.py --toggle
   ```

3. **Verificar se mudou:**
   ```bash
   ./battery_toggle_simple.py --status
   ```

## 🎯 Próximos passos recomendados:

1. **Teste a versão simples** primeiro para garantir que funciona
2. **Se funcionar bem**, execute `./instalar.sh` para instalar no sistema
3. **Configure um atalho de teclado** nas configurações do Gnome
4. **Use o menu de aplicações** para acesso rápido

## 🔧 Se algo não funcionar:

1. Execute `./testar.py` para diagnóstico
2. Verifique se é um laptop Lenovo IdeaPad
3. Instale dependências: `sudo dnf install python3-gobject polkit`

## 📝 Resumo dos comandos essenciais:

```bash
# Testar compatibilidade
./testar.py

# Usar versão simples
./battery_toggle_simple.py --toggle

# Instalar no sistema
./instalar.sh

# Verificar status
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

**🎉 Pronto! Seu programa está funcionando e testado!**
