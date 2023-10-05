# Data Project Starter Kit

## Sobre o Projeto

Este repositório é uma parte integrante do workshop "Como estruturar um projeto de dados do Zero". O intuito aqui é fornecer uma base e uma estrutura padronizada para iniciar projetos de engenharia, ciência e análise de dados. O foco principal é em boas práticas, automação, testes e documentação.

### Objetivos do Workshop:

* **Entender a estrutura padrão de projetos**: Isso inclui a organização de diretórios, como o código-fonte, testes, documentação, entre outros.

* **Estruturas padrões em projetos de dados**: Vamos refatorar o projeto utilizando classes, módulos e boas práticas em uma ETL.

* **Familiarizar-se com ferramentas de desenvolvimento**: Abordaremos o uso de ambientes virtuais e discutiremos ferramentas como PIP, CONDA e POETRY.

* **Testes com Pytest**: Garanta que seu código funcione como esperado, criando testes unitários e de integração.

* **Versionamento com Git e GitHub**: Aprenda a versionar seu projeto e a usar o GitHub para colaboração e publicação.

* **Documentação com MKDocs**: Você vai aprender a documentar seu projeto com MKDocs e a publicar sua documentação no [GitHub Pages](https://lvgalvao.github.io/DataProjectStarterKit/)

* **Automatização e CI/CD**: Configurar rotinas de integração e entrega contínua para manter a qualidade do projeto.


## Começando

### Pré-requisitos

Você deve ter o Python instalado em sua máquina. Este projeto foi desenvolvido utilizando Python 3.11, mas é compatível com versões desde a 3.11 até a 3.13.

### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/lvgalvao/dataprojectstarterkit.git
cd dataprojectstarterkit
```

2. Instale as dependências do projeto usando [Poetry](https://python-poetry.org/docs/):

```bash
poetry install
```

3. Ative o ambiente virtual:

```bash
poetry shell
```

4. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
make test
```

1. Execute o comando para ver a documentação do projeto:

```bash
make docs
```

6. Execute o comando de execucão da pipeline:

```bash
make run
```

7. Verifique na pasta data/output se o arquivo foi gerado corretamente.

## Contato

Para dúvidas, sugestões ou feedbacks:

* **Luciano Filho** - [lvgalvaofilho@gmail.com](mailto:lvgalvaofilho@gmail.com)
