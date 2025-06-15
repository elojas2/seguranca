# FTP

## O que usar

Instalar um servidor FTP:

```bash
    sudo apt install vsftpd
```

Configure no /etc/vsftpd.conf:

```ini
    write_enable=YES
    local_enable=YES
```

Crie um usuário

```bash
    sudo adduser ftptest
    sudo passwd ftptest
```

Inicie:

```bash
    sudo systemctl start vsftpd
```

Usando o hydra para atacar:

```bash
    hydra -l ftptest -P /usr/share/wordlists/rockyou.txt ftp://127.0.0.1
```
