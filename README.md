# projeto-integrador-grupo31
Esse é o repositório do projeto integrador do grupo 31 do Senac

## Tema:
Saúde Mental e o Mundo Digital

## Integrantes
- Juliana Lins
- Vitória Ferreira
- Erick Bicalho
- Lucas Rossatto
- Gabriel Andrade
- Amália Pratte

## Base de dados:
- Nome: Mental Health & Technology Usage Dataset | Kaggle
- Link: https://www.kaggle.com/datasets/waqi786/mental-health-and-technology-usage-dataset

## Contexto
Vivemos em uma era de hiperconectividade, onde a integração entre a vida cotidiana e os dispositivos digitais é praticamente absoluta. A tecnologia facilitou o acesso à informação e à comunicação, assim como o uso intensivo de telas e redes sociais tem levantado preocupações crescentes sobre o bem-estar psicológico.

Estudos recentes sugerem que a exposição prolongada ao ambiente digital pode estar associada à privação de sono, ao aumento dos níveis de cortisol (hormônio do estresse) e ao desenvolvimento de sintomas de ansiedade e depressão. Diante desse cenário, torna-se essencial investigar, por meio de dados, como o comportamento digital impacta diretamente indicadores biológicos e emocionais, como o sono e o estresse.

## Objetivo
Este projeto tem como objetivo principal analisar e visualizar as correlações entre os hábitos de uso tecnológico e a saúde mental dos usuários. Através do processamento de dados com Python, buscamos responder a perguntas fundamentais:

Impacto no Descanso: De que forma o tempo excessivo de tela compromete a quantidade e qualidade das horas de sono?

Bem-estar Emocional: Existe uma correlação estatística entre o tempo gasto em redes sociais e o aumento do nível de estresse percebido?

Demografia Digital: Quais faixas etárias apresentam os comportamentos de risco mais acentuados no ambiente virtual?

Identificação de Padrões: Fornecer um panorama claro (através de um Dashboard) que ajude a identificar se o uso da tecnologia é o fator determinante para uma saúde mental classificada como "boa" ou "ruim".

A finalidade última é transformar dados complexos em insights compreensíveis, promovendo uma reflexão sobre a necessidade de um equilíbrio saudável entre a vida analógica e a digital.

---

## Planejamento 
Tarefa de Todos: Escolher a base de dados 

Tarefa Juliana Lins: Sugestão de base de dados e definir as tarefas de cada integrante

Tarefa Vitória Ferreira: Sugestão de base de dados e criar um cronograma 

Tarefa Erick Bicalho: Sugestão de base de dados, criação do Repositório, organização estrutural do projeto, indicar visualizações e métricas vamos apresentar no dashboard

Tarefa Lucas Rossatto: Descrever a ideia inicial do Dashboard

Tarefa Gabriel Andrade: Revisar o readme.md completo

Tarefa Amália Pratte: Descrever brevemente o contexto e objetivo da análise 

---

<h2>Cronograma - Projeto Integrador</h2>

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Etapa</th>
      <th>Atividade</th>
      <th>Responsável</th>
      <th>Data de entrega</th>
      <th>Andamento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 - Planejamento Inicial</td>
      <td>Criação do repositório, adição dos integrantes e organização das pastas.</td>
      <td>Erick</td>
      <td>10/03/2026</td>
      <td>Concluído</td>
    </tr>
    <tr>
      <td>1 - Planejamento Inicial</td>
      <td>Definição das tarefas de cada integrante no README.</td>
      <td>Juliana</td>
      <td>20/03/2026</td>
      <td>Concluído</td>
    </tr>
    <tr>
      <td>1 - Planejamento Inicial</td>
      <td>Elaboração do cronograma do projeto no README.md</td>
      <td>Vitória</td>
      <td>21/03/2026</td>
      <td>Concluído</td>
    </tr>
    <tr>
      <td>2 - Contextualização</td>
      <td>Escrita do contexto e objetivo da análise sobre Saúde Mental e Tecnologia.</td>
      <td>Amália</td>
      <td>23/03/2026</td>
      <td>Concluído</td>
    </tr>
    <tr>
      <td>3 - Processo de ETL</td>
      <td>Planejamento e descrição das etapas de Extração, Transformação (Pandas) e Carga.</td>
      <td>Integrantes</td>
      <td>10/03/2026</td>
      <td>Concluído</td>
    </tr>
    <tr>
      <td>4 - Dashboard (Ideia Inicial)</td>
      <td>Descrição da ideia inicial do dashboard e seu propósito.</td>
      <td>Lucas</td>
      <td>23/03/2026</td>
      <td>Concluído</td>
    </tr>
    <tr>
      <td>4 - Dashboard (Métricas)</td>
      <td>Indicação das visualizações e métricas que serão apresentadas no dashboard.</td>
      <td>Erick</td>
      <td>19/03/2026</td>
      <td>Concluído</td>
    </tr>
    <tr>
      <td>5 - Revisão Final</td>
      <td>Apoio na ideação do dashboard e revisão completa do README.md.</td>
      <td>Gabriel</td>
      <td>23/03/2026</td>
      <td>Concluído</td>
    </tr>
  </tbody>
</table>

## Transformação de dados (ETL)

### Para garantir a qualidade dessa análise, pretendemos realizar:

- Limpeza: Identificar e tratar valores nulos ou duplicados.
- Padronização: Converter tipos de dados (ex: Garantir que valores númericos sejam de fato do tipo número, para que não tenha erro na hora de calcular)
- Categorizar: Agrupar idades em faixas etárias para facilitar comparação.


## Métricas e visualizações que vamos mostrar na análise:
 
- Média de horas de sono
- Média de tempo de tela
- Nível médio de estresse
- Horas médias de redes sociais
- Porcentagem de pessoas com a saúde mental boa ou ruim
- Qual faixa etária tem mais tempo de tela

---

- Gráficos de dispersão para análisar relações (ex: tempo de tela X estresse)
- Gráficos de barra para comparação
- Gráfico mapa de calor (heatmap) para correlação de variáveis
- Histograma para identificar padrões 

Além das métricas, serão realizadas análises relacionais entre variáveis, com o objetivo de indentificar padrões e possíveis correlações relevantes.

---

# Dashboard: Saúde Mental & Tecnologia
 
## Descrição da Ideia Inicial
 
Este dashboard tem como objetivo analisar o impacto do uso de tecnologia, especialmente tempo de tela e redes sociais, na saúde mental das pessoas. A proposta é transformar dados brutos em visualizações claras e objetivas, permitindo identificar padrões, correlações e tendências entre hábitos digitais, qualidade do sono, níveis de estresse e bem-estar geral.  