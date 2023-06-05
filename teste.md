# Tarefas para refatorar o sistema de Login

## Visão Geral

* Hoje o sistema de autenticação, utilizado pelo Parquet Digital, é totalmente dependente do sistema SCA, onde são
  administrados
  os usuários.
* O sistema Parquet Digital, consome as informações cedidas pelo SCA, através da API do SCA.
* Hoje todos os usuários que utilizam o PD(Parquet Digital) são administrados por e somente pelo sistema SCA.
* O sistema é autenticado passando o usuário e sua senha para o sistema SCA, que autenticando devolve um arquivo JSON,
  com algumas informações do usuário e suas permissões(ROLES).
* Somente usuários ativos são autenticados.
* Autenticado, o sistema P.D gera uma chave JWT que é utilizada pelo PD.
* A chave JWT é um identificador único.
* O processo de Login retorna ALGUMAS das promotorias do dado promotor.
* Utilizamos duas bases de dados(Oracle e Impala) para processar as informações do Login.
* Hoje não utilizamos as ferramentas de autenticação do Django.
* Hoje passamos a chave JWT, na URl, o que não é seguro.

## Propostas

![](https://gitlab-dti.mprj.mp.br/gadg/desenvolvimento/apimpmapas/-/raw/efc04b417bff01da86b34b3b624f52f0f9c7758f/documentacao/geral/imgs/Login.jpg)
<img src="/home/welington_souza/workspace/parquet_digital_lab/documentacao/geral/imgs/Login.jpg"/>

[Miro Login](https://miro.com/app/board/uXjVMCg92Sc=/?share_link_id=755952623749)

<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVMC7kbaI=/?moveToViewport=-653,-427,1760,798&embedId=438631267808" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

Além da autenticação no sistema SCA, também utiliza o sistema de gerência nativo do Django em paralelo.
Essa estratégia nos possibilitará que mantenhamos a conformidade com o uso do SCA, mantendo inalterável para o nosso
usuário final.
Toda informação sobre o usuário continuará ser de responsabilidade do SCA, salvo algumas gerências extra, exemplo:

* Inclusão de desenvolvedores que ainda não estiverem no sistema SCA, estagiários, ou novos desenvolvedores.
* Gerências especiais em que o assessor esteja “emprestado”, a alguma promotoria.

Em resumo, a proposta de uma segunda gerência de usuário, consiste em dar suporte a codificação das atividades do
backend, adicionando possibilidades de maiores configurações e criações de novos recursos referente ao assunto.
Também a gerência de casos especiais em que o SCA ou não suporta, ou porventura, não executou.

## Problemas com o SCA

* Não podemos administrar os usuários diretamente.
  Nós disponibilizamos uma plataforma onde não controlamos os nossos usuários.
  Isso inviabiliza o DEBUG, de algum problema entre outros problemas.
* Não podemos adicionar um usuário para testes.
* Demora muito a adição/exclusão de novos usuários, principalmete para os desenvolvedores.


