# 🔋 Battery Conservation Mode Toggle para Lenovo IdeaPad

<div align="center">

![Battery Conservation](https://img.shields.io/badge/Battery-Conservation-green)
![Lenovo IdeaPad](https://img.shields.io/badge/Lenovo-IdeaPad-blue)
![Fedora](https://img.shields.io/badge/Fedora-Linux-blue)
![Gnome](https://img.shields.io/badge/Desktop-Gnome-orange)

**Controle fácil do modo de conservação da bateria para laptops Lenovo IdeaPad no Fedora Linux**

</div>

## 🎯 Para Usuários de Lenovo IdeaPad

Se você tem um **Lenovo IdeaPad** e usa **Fedora Linux**, este programa é para você!

### 🤔 Por que usar o Modo de Conservação?

Seu laptop IdeaPad tem uma funcionalidade especial que pode **dobrar a vida útil da sua bateria**:

- 🔋 **Sem conservação**: Bateria carrega até 100% → Degrada mais rápido
- ✅ **Com conservação**: Bateria carrega só até 60% → Dura muito mais tempo

### 📊 Quando usar cada modo:

| Situação | Modo Recomendado | Por quê? |
|----------|------------------|----------|
| 🏠 Trabalho em casa/escritório | **LIGADO** | Laptop sempre na tomada, preserva bateria |
| ✈️ Viagens e uso móvel | **DESLIGADO** | Precisa de autonomia máxima |
| 🎮 Gaming conectado na energia | **LIGADO** | Protege bateria do calor e carga constante |
| 📚 Estudos na biblioteca | **DESLIGADO** | Precisa de toda autonomia disponível |

## ✅ Compatibilidade - Seu IdeaPad Funciona?

Este programa funciona na maioria dos IdeaPads modernos:

### ✅ **Modelos Testados e Compatíveis:**
- IdeaPad Gaming 3
- IdeaPad 5 (14" e 15")
- IdeaPad Flex 5
- IdeaPad S340, S540
- IdeaPad L340, L3
- IdeaPad 320, 330
- E muitos outros modelos recentes

### 🔍 **Como verificar se seu IdeaPad é compatível:**
```bash
# Execute este comando no terminal:
ls /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Se aparecer o caminho do arquivo = ✅ Compatível
# Se der erro "arquivo não encontrado" = ❌ Não compatível
```

### 💻 **Sistemas Suportados:**
- ✅ Fedora Linux (todas as versões recentes)
- ✅ Desktop Gnome
- ✅ Módulo `ideapad_laptop` carregado (automático na maioria dos casos)

## 🚀 Instalação Super Fácil (3 passos)

### 📋 **Pré-requisitos (já vem no Fedora):**
- ✅ Python 3 (já instalado)
- ✅ GTK 3 (já instalado no Gnome)
- ✅ PolicyKit (já instalado)

### 📥 **Passo 1: Baixar o programa**

**Opção A - Git (recomendado):**
```bash
git clone https://github.com/helioneto144/BatteryIdeaped.git
cd BatteryIdeaped
```

**Opção B - Download direto:**
1. Clique em "Code" → "Download ZIP" nesta página
2. Extraia o arquivo
3. Abra terminal na pasta extraída

### ⚙️ **Passo 2: Instalar**
```bash
chmod +x install.sh
./install.sh
```

### 🎉 **Passo 3: Usar**
1. Pressione a tecla **Super** (Windows)
2. Digite "**Battery**"
3. Clique em "**Battery Conservation Mode**"

## 🔧 **O que a instalação faz:**
- ✅ Verifica se seu IdeaPad é compatível
- ✅ Instala o programa no sistema
- ✅ Cria ícone no menu do Gnome
- ✅ Configura permissões necessárias
- ✅ Testa se tudo está funcionando

### Instalação Manual

Se preferir instalar manualmente:

```bash
# Copiar script principal
sudo cp battery_conservation.py /usr/local/bin/
sudo chmod +x /usr/local/bin/battery_conservation.py

# Instalar entrada do menu
sudo cp battery-conservation.desktop /usr/share/applications/
sudo chmod 644 /usr/share/applications/battery-conservation.desktop

# Atualizar cache do desktop
sudo update-desktop-database /usr/share/applications/
```

## 🎮 Como Usar Seu Novo Controle de Bateria

### 🖱️ **Método 1: Interface Gráfica (Mais Fácil)**

1. **Abrir o programa:**
   - Pressione `Super` (tecla Windows)
   - Digite "**Battery**" ou "**Conservação**"
   - Clique em "**Battery Conservation Mode**"

2. **Usar a interface:**
   - 📊 **Status atual**: Mostra se está ligado/desligado
   - 🔄 **Botão principal**: Clique para alternar o modo
   - 🔄 **Atualizar**: Verifica o status atual
   - ℹ️ **Informações**: Explica o que cada modo faz

### ⌨️ **Método 2: Linha de Comando**

```bash
# Abrir interface gráfica
python3 /usr/local/bin/battery_conservation.py

# Verificar status atual
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

### 📱 **Exemplo de Uso Diário:**

**🌅 Manhã (indo trabalhar):**
- Modo: **DESLIGADO**
- Motivo: Preciso de autonomia máxima

**🏠 Chegando em casa:**
- Modo: **LIGADO**
- Motivo: Vou usar conectado na energia

**✈️ Viagem:**
- Modo: **DESLIGADO**
- Motivo: Preciso de toda bateria disponível

### Comandos Manuais (avançado)

```bash
# Verificar status atual
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Ligar modo conservação (requer sudo)
echo 1 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Desligar modo conservação (requer sudo)
echo 0 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

## Desinstalação

Para remover o programa:

```bash
chmod +x uninstall.sh
./uninstall.sh
```

Ou manualmente:

```bash
sudo rm -f /usr/local/bin/battery_conservation.py
sudo rm -f /usr/share/applications/battery-conservation.desktop
sudo update-desktop-database /usr/share/applications/
```

## 🔧 Solução de Problemas para IdeaPads

### ❌ **"Sistema não suportado"**

**Seu IdeaPad não é compatível? Vamos verificar:**

```bash
# 1. Verificar se é um IdeaPad Lenovo
sudo dmidecode -s system-product-name

# 2. Verificar se o módulo está carregado
lsmod | grep ideapad

# 3. Verificar se o arquivo de controle existe
ls -la /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

**Soluções:**
- ✅ Se o arquivo existe: Seu IdeaPad é compatível!
- ❌ Se não existe: Modelo pode não ter suporte ou precisa atualizar BIOS
- 🔄 Tente reiniciar e verificar novamente

### ⚠️ **"Falha ao alterar modo de conservação"**

**Problema de permissão? Vamos resolver:**

```bash
# Verificar se pkexec está instalado
which pkexec

# Se não estiver, instalar:
sudo dnf install polkit
```

**Outras soluções:**
- 🔐 Certifique-se de que sua conta tem privilégios sudo
- 🔄 Tente fechar e abrir o programa novamente
- 💻 Teste manual: `echo 1 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode`

### 🖥️ **Interface não abre**

**Problema com GTK? Instalar dependências:**

```bash
# Instalar tudo que precisa
sudo dnf install python3 python3-gobject gtk3-devel polkit

# Se ainda não funcionar
sudo dnf install gobject-introspection-devel
```

### 🆘 **Meu IdeaPad específico não funciona**

**Modelos mais antigos ou específicos:**

1. **Verificar variações do caminho:**
   ```bash
   find /sys -name "*conservation*" 2>/dev/null
   find /sys -name "*ideapad*" 2>/dev/null
   ```

2. **Verificar BIOS:**
   - Alguns IdeaPads precisam habilitar "Battery Conservation" na BIOS
   - Procure em: Advanced → Power Management

3. **Atualizar sistema:**
   ```bash
   sudo dnf update
   ```

### 📞 **Ainda não funciona?**

Abra uma [issue no GitHub](https://github.com/helioneto144/BatteryIdeaped/issues) com:
- 🏷️ Modelo exato do seu IdeaPad
- 💻 Versão do Fedora
- 📋 Saída do comando: `sudo dmidecode -s system-product-name`
- 📋 Saída do comando: `find /sys -name "*conservation*" 2>/dev/null`

## Estrutura do Projeto

```
BatteryFedora/
├── battery_conservation.py    # Script principal
├── battery-conservation.desktop # Entrada do menu
├── install.sh                # Script de instalação
├── uninstall.sh              # Script de desinstalação
└── README.md                 # Este arquivo
```

## 🤝 Contribuições da Comunidade IdeaPad

**Ajude outros usuários de IdeaPad!**

### 🐛 **Encontrou um problema?**
- Abra uma [issue](https://github.com/helioneto144/BatteryIdeaped/issues)
- Inclua modelo do seu IdeaPad e versão do Fedora

### ✨ **Quer melhorar o programa?**
- Faça um fork do projeto
- Implemente sua melhoria
- Envie um pull request

### 📝 **Testou em um novo modelo de IdeaPad?**
- Compartilhe nos issues se funcionou
- Ajude a expandir a lista de compatibilidade

### 🌟 **Gostou do projeto?**
- Dê uma ⭐ no GitHub
- Compartilhe com outros usuários de IdeaPad
- Escreva um review

## 📊 Status do Projeto

- ✅ **Funcional**: Testado em múltiplos modelos de IdeaPad
- 🔄 **Ativo**: Mantido regularmente
- 🆓 **Gratuito**: Sempre será livre e open source
- 🛡️ **Seguro**: Usa métodos oficiais do kernel Linux

## 📜 Licença

Este projeto é **domínio público**. Use livremente em qualquer IdeaPad!

## 🙏 Agradecimentos

- **Lenovo** por implementar o modo de conservação nos IdeaPads
- **Comunidade Linux** por manter os drivers ideapad_laptop
- **Usuários** que testaram e reportaram compatibilidade

---

<div align="center">

**💡 Dica:** Marque este repositório com ⭐ para ajudar outros usuários de IdeaPad a encontrarem!

**🔋 Sua bateria agradece!**

</div>
