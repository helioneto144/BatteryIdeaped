# Como Usar o Battery Conservation Mode Toggle

## Instalação Rápida

1. **Baixe ou clone este repositório**
2. **Abra um terminal no diretório do projeto**
3. **Execute o instalador:**
   ```bash
   ./install.sh
   ```

## Verificação do Sistema

Antes de instalar, você pode testar se seu sistema é compatível:

```bash
python3 test_battery.py
```

Este comando irá verificar:
- Se o arquivo de controle existe
- O status atual do modo de conservação
- Se as dependências estão disponíveis

## Formas de Usar

### 1. Via Menu do Gnome (Recomendado)

Após a instalação:
1. Pressione a tecla **Super** (Windows)
2. Digite "**Battery**" ou "**Conservação**"
3. Clique em "**Battery Conservation Mode**"
4. Use a interface gráfica para alternar o modo

### 2. Via Linha de Comando

```bash
# Executar o programa com interface gráfica
python3 battery_conservation.py

# Ou se instalado:
python3 /usr/local/bin/battery_conservation.py
```

### 3. Comandos Manuais (Para Usuários Avançados)

```bash
# Verificar status atual
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Ligar modo conservação (requer sudo)
echo 1 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

# Desligar modo conservação (requer sudo)
echo 0 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

## O que Cada Modo Faz

### Modo Conservação LIGADO (1)
- ✅ Bateria carrega apenas até ~60%
- ✅ Prolonga a vida útil da bateria
- ✅ Ideal para uso principalmente conectado à energia
- ⚠️ Menor autonomia quando desconectado

### Modo Conservação DESLIGADO (0)
- ✅ Bateria carrega até 100%
- ✅ Máxima autonomia
- ✅ Ideal para uso móvel frequente
- ⚠️ Pode reduzir vida útil da bateria a longo prazo

## Quando Usar Cada Modo

### Use Modo Conservação LIGADO quando:
- Laptop fica conectado à energia a maior parte do tempo
- Trabalha principalmente em casa/escritório
- Quer maximizar a vida útil da bateria
- Não precisa de autonomia máxima

### Use Modo Conservação DESLIGADO quando:
- Usa o laptop frequentemente sem energia
- Precisa de máxima autonomia
- Viaja frequentemente
- Precisa de carga completa para trabalho móvel

## Solução de Problemas

### "Sistema não suportado"
- Verifique se tem um laptop Lenovo IdeaPad
- Execute: `python3 test_battery.py` para diagnóstico

### "Falha ao alterar modo"
- Certifique-se de ter permissões administrativas
- Verifique se o PolicyKit está instalado
- Tente executar como administrador

### Interface não abre
- Verifique se o GTK está instalado:
  ```bash
  sudo dnf install python3-gobject gtk3-devel
  ```

## Desinstalação

Para remover o programa:

```bash
./uninstall.sh
```

## Status do Sistema

Você pode sempre verificar o status atual com:

```bash
python3 test_battery.py
```

Ou diretamente:

```bash
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

- **0** = Desligado (carga até 100%)
- **1** = Ligado (carga até ~60%)

## Dicas

1. **Para uso diário:** Deixe o modo conservação ligado se usa principalmente conectado
2. **Para viagens:** Desligue o modo conservação para ter autonomia máxima
3. **Monitoramento:** Use o programa para verificar o status facilmente
4. **Automação:** Você pode criar scripts para alternar automaticamente baseado em condições

## Segurança

- O programa usa `pkexec` para elevação segura de privilégios
- Não armazena senhas ou credenciais
- Apenas modifica o arquivo de controle do kernel
- Todas as operações são reversíveis
