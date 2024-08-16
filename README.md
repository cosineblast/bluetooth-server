
## Comofaz

Primeiro, crie um venv na pasta para instalar as dependências, se não tiver um:

``` 
python3 -m venv env
```

Depois, inicialize o env no seu shell (normalmente bash):

```
. ./env/bin/activate
```

Depois, use pip para instalar as dependências

```
pip install $(cat requirements.txt)
```

Para executar o servidor, utilize

``` 
python3 main.py
``` 

