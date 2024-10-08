# Acesso automatizado ao Github

O programa tem o objetivo de enviar convites automatizados para um repositório específico do Github, com base em uma planilha de Excel que vai obter o user e o tipo de acesso adequado ao user.

## Arquitetura
![image](assets/send-invite-github.png)

## Pré-requisitos
* Python 3.10

## Como utilizar a automação?
Clone o repositório
```
git clone https://github.com/wlcamargo/access_github_automated
```

Entre na pasta
```
cd access_github_automated
```

Crie o ambiente virtual
```
python3 -m venv venv
```

Entre no ambiente virutal (Linux)
```
source venv/bin/activate
```

Instale as dependências
```
pip install -r requirements.txt
```

Atualize o arquivo com os valores das variáveis corretas no arquivo ```.env_sample``` e altere o nome dele para ```.env```

## Concede acesso com base em planilha do Excel
Execute o programa ```python3 github-access-excel.py```

## Concede acesso com base em Google Sheets
Execute o programa ```python3 github-access-google.py```

## Warning
Para capturar dados de uma planilha do Google Sheets, será necessário exportar a chave json que concede acesso. 

## Como gerar a chave json?
1 - Procure no Google por ``` google console ```

![image](assets/google-console.png)

2 - No portal, clique em ``` apis & services```

![image](assets/api-and-services.png)

3 - Crie e exporte a credencial no formato ```.json```

![image](assets/credentials.png)

## Referências

https://docs.github.com/en/rest?apiVersion=2022-11-28


## Developer
| Desenvolvedor      | LinkedIn                                   | Email                        | Portfólio                              |
|--------------------|--------------------------------------------|------------------------------|----------------------------------------|
| Wallace Camargo    | [LinkedIn](https://www.linkedin.com/in/wallace-camargo-35b615171/) | wallacecpdg@gmail.com        | [Portfólio](https://wlcamargo.github.io/)   |



