# Core

Esse repositório faz parte do projeto de análise de sentimentos de formulários em um ambiente educacional e é destinado à API em Python responsável pela análise.

## Configure o seu ambiente

Baixe o Python em https://www.python.org/downloads/ e instale em sua máquina. O download a partir do site vem com o pip (gerenciador de pacotes do Python) por padrão.

Com o Python e o pip instalados, crie uma pasta reservada com o nome desse repositório (core). Dentro dessa pasta, crie um ambiente virtual (virtual environment) do Python com o comando `python -m venv .venv` a partir da raiz do repositório.

*O Python já possui um módulo de criação de venv (como visto acima), mas existem outros módulos criados pela comunidade com suas vantanges e desvantagens.*

Após o venv ser criado, será necessário ativalo com o comando `source .venv/bin/activate` se você estiver no Linux ou no Mac, ou `.\.venv\Scripts\activate` se estiver no Windows. Deve aparecer uma marcação no seu terminal indicando que o venv está ativo. Para desativá-lo, basta executar o comando `deactivate`.

*O procedimento de ativação deve ser feito sempre que o venv do projeto não estiver ativado e ele deve permanecer ativo enquanto você estiver rodando ou alterando o projeto.*

Para instalar as dependências do projeto rode o comando `pip install -r requirements.txt` com o venv ativo.

## Rodando a API

Execute o comando `uvicorn main:app --reload`.
