# Data Project Starter Kit

## Sobre o Projeto

Este repositório é uma parte integrante do workshop "Como estruturar um projeto de dados do Zero". O intuito aqui é fornecer uma base e uma estrutura padronizada para iniciar projetos de engenharia, ciência e análise de dados. O foco principal é em boas práticas, automação, testes e documentação.
Tera um novo no dia 29/01
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

* **VSCode**: É o editor de código que vamos utilizar no workshop. [Instruções de instalação do VSCode aqui](https://code.visualstudio.com/download).

* **Git e GitHub**:

1. Você deve ter o Git instalado em sua máquina. [Instruções de instalação do Git aqui](https://git-scm.com/book/pt-br/v2).
2. Você também deve ter uma conta no GitHub. [Instruções de criação de conta no GitHub aqui] (https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account).
3. Se você for usuário Windows, recomendo esse vídeo: [Youtube](https://www.youtube.com/watch?v=_hZf1teRFNg).
4. Tutorial de Git e Github básico [Ebook](https://www.linkedin.com/feed/update/urn:li:activity:7093915148351864832/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7093915148351864832%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=4GUdvXH4TK%2BtZtlNHmiqJA%3D%3D).
5. Se você já é usuário Git, recomendo o vídeo do Akita: [Youtube](https://www.youtube.com/watch?v=6Czd1Yetaac).

* **Pyenv**: É usado para gerenciar versões do Python. [Instruções de instalação do Pyenv aqui](https://github.com/pyenv/pyenv#installation). Vamos usar nesse projeto o Python 3.11.3. Para usuários Windows, é recomendado assistirem esse tutorial [Youtube](https://www.youtube.com/watch?v=TkcqjLu1dgA).

* **Poetry**: Este projeto utiliza Poetry para gerenciamento de dependências. [Instruções de instalação do Poetry aqui](https://python-poetry.org/docs/#installation).Se você é usuário Windows, recomendo assistir esse vídeo: [Youtube](https://www.youtube.com/watch?v=BuepZYn1xT8). Que instala o Python, Poetry e VSCode. Mas um simples comando PIP INSTALL POETRY já resolve.

Sugestão de leituras.
[Ebook 1 - Testes](https://www.linkedin.com/feed/update/urn:li:activity:7099722252144848896/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7099722252144848896%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=hg1%2BufBeTLClrS%2BJixGEoA%3D%3D)
[Ebook 2 - Github Actions](https://www.linkedin.com/feed/update/urn:li:activity:7098264928553201665/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7098264928553201665%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=%2BFcdPRcDT62iNieFV3Yc%2Fg%3D%3D)
[Ebook 3 - Na minha máquina funciona](https://www.linkedin.com/feed/update/urn:li:activity:7095419109449814017/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7095419109449814017%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=7ShpQeNCQuCDErI%2BAzEBXw%3D%3D)

### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/lvgalvao/dataprojectstarterkit.git
cd dataprojectstarterkit
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.11.3
pyenv local 3.11.3
```

3. Instale as dependências do projeto:

```bash
poetry install
```

4. Ative o ambiente virtual:

```bash
poetry shell
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
task test
```

6. Execute o comando para ver a documentação do projeto:

```bash
task doc
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
task run
```

8. Verifique na pasta data/output se o arquivo foi gerado corretamente.

## Contato

Para dúvidas, sugestões ou feedbacks:

* **Luciano Filho** - [lvgalvaofilho@gmail.com](mailto:lvgalvaofilho@gmail.com)
