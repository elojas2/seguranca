# **MSYQL**

## **Ambiente**

- Kali Linux
- Servidor MYSQL local ativo em `127.0.0.1:3306`
- Usuário alvo: `root`
- Wordlist: `/usr/share/wordlists/rockyou.txt`

---

## **Passos do lab**

### Instale o MSYQL se não tiver

```bash
    sudo apt update
    sudo apt install mysql-server
```

### Garanta que o MySQL está rodando

```bash
    sudo systemctl enable mysql
    sudo systemctl start mysql
    sudo systemctl status mysql
```

### Configure usuário e permissões só para o lab

Entre no MYSQL

```bash
    sudo mysql
```

Crie o usuário de teste

```bash
    CREATE USER 'labuser'@'localhost' IDENTIFIED BY '123456';
    GRANT ALL PRIVILEGES ON *.* TO 'labuser'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;
```

### Execute o Hydra

```bash
    hydra -V -l labuser -P /usr/share/wordlists/rockyou.txt mysql://127.0.0.1
```

### Resultado esperado

Senha encontrada:

```bash
    [3306][mysql] host: 127.0.0.1   login: labuser   password: 123456
```

Senha não encontrada:

```bash
    0 of 1 target completed, 0 valid password found
```

Apague o usuário após o lab

```bash
    sudo mysql
```

```bash
    DROP USER 'labuser'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;
```
