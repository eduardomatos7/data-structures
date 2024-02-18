# Projeto-grafos---Estrutura-de-Dados
Neste projeto, será criada uma base de dados composta por diferentes locais de Pernambuco, modelados como vértices de um grafo, e as distâncias entre eles representadas como arestas, com pesos correspondentes às distâncias reais.
O objetivo é construir uma base de dados real e pública, acessível a qualquer pessoa, que possa ser utilizada para diversos fins, como estudos de redes de transporte, otimização de rotas, análise de conectividade entre regiões, entre outros.
Para criar a base de dados, serão utilizadas informações disponíveis publicamente, como aquelas fornecidas por órgãos governamentais ou provedores de dados geoespaciais confiáveis.
A base de dados resultante terá mais de 90 vértices, representando uma variedade de locais em Pernambuco, e mais de 100 arestas, representando as conexões entre esses locais. Além disso, cada aresta terá um peso correspondente à distância real entre os locais que conecta.
# Base de Dados
Nesse contexto, podemos analogamente considerar as cidades como os vértices de um grafo, enquanto as distâncias entre elas seriam representadas pelas arestas. Assim, a base de dados construída com o auxílio do Google Maps se assemelha a um grafo ponderado, onde cada cidade corresponde a um vértice e a distância entre elas é a informação associada às arestas. Essa representação gráfica permite visualizar e analisar de forma mais clara as conexões entre as cidades de Pernambuco, desde a capital até o agreste, interior e sertão do estado.
# Algoritmo de Prim
O algoritmo de Prim é uma técnica amplamente utilizada para encontrar a árvore geradora mínima em um grafo ponderado e não direcionado. Uma árvore geradora mínima de um grafo é um subconjunto de arestas que conecta todos os vértices do grafo, garantindo que a soma dos pesos das arestas seja mínima.
Ao utilizar o algoritmo de Prim, é necessário fornecer como entrada o grafo ponderado em que desejamos encontrar a árvore geradora mínima, bem como o vértice a partir do qual desejamos iniciar a busca pela árvore geradora mínima. Este vértice inicial pode ser qualquer vértice válido do grafo.
O algoritmo de Prim funciona selecionando repetidamente a aresta de menor peso que conecta um vértice já incluído na árvore geradora mínima a um vértice ainda não incluído. Este processo continua até que todos os vértices do grafo tenham sido incluídos na árvore.
Universidade Federal de Pernambuco 
Centro de Informática - CIn 

# Relatório do projeto: Grupo #3.3

## Contexto do problema
O contexto do problema envolve a necessidade de calcular e visualizar a Árvore Geradora Mínima (MST) de um grafo representado por uma lista de arestas e seus pesos. Isso pode ser útil em diversas aplicações, como em sistemas de roteamento, redes de computadores, logística, entre outros.

A base de dados consiste em uma lista de arestas e pesos, representando as conexões entre vértices de um grafo. Cada aresta é definida por uma origem, um destino e um peso associado. As cidades de Pernambuco são representadas como um grafo ponderado, onde as cidades são os vértices e as estradas que as conectam são as arestas. Cada aresta possui um peso associado, que geralmente representa a distância entre as cidades ou algum outro critério relevante, como o tempo de viagem .

A base de dados contém informações sobre a distância entre cidades de Pernambuco. Cada entrada na lista mostra uma rota entre duas cidades, junto com a distância entre elas. Podemos interpretar as distâncias entre as cidades como as arestas de um grafo, enquanto as cidades seriam os vértices desse grafo. Esses dados são úteis para planejar viagens, entender como as cidades estão conectadas e calcular distâncias entre diferentes lugares do estado. Em suma, é como ter um mapa das estradas de Pernambuco, mostrando como as cidades estão interligadas.

# Implementação
Algoritmo utilizado. 
Neste projeto, utilizamos o algoritmo de Prim.

Desenvolvimento. 
Nós começamos definindo o que queríamos na nossa aplicação, que era calcular a
Árvore Geradora Mínima de cidades em Pernambuco e exibi-la graficamente. Em
Python, usamos Tkinter para a interface, NetworkX para grafos e Matplotlib para
visualização.
Criamos a interface com Tkinter, com janelas, botões e caixas de texto para
interação intuitiva. Usamos NetworkX para representar o grafo das cidades e
calcular a Árvore Geradora Mínima a partir do vértice inicial escolhido pelo usuário.
Com Matplotlib, exibimos graficamente a Árvore Geradora Mínima, facilitando a
compreensão das conexões entre as cidades. Testamos e ajustamos para garantir
funcionamento e usabilidade, resultando em uma ferramenta legal para explorar as
conexões entre as cidades pernambucanas. Juntando tudo isso, criamos uma
ferramenta que não só calcula a Árvore Geradora Mínima, mas também dá uma ideia
bem legal de como as estradas ligam as cidades de Pernambuco

## Bibliotecas utilizadas.
pandas: Para o gerenciamento mais eficaz da base de dados.

networkx: Para manipulação de grafos e cálculo da MST.

matplotlib.pyplot: Para visualização gráfica da MST.


## Conclusão
O programa oferece uma solução interativa e visualmente intuitiva para encontrar a MST de um grafo. O usuário pode selecionar o vértice inicial e, em seguida, visualizar tanto a lista de arestas da MST quanto a representação gráfica dela. Isso permite uma compreensão clara das conexões mínimas necessárias para interligar todos os vértices do grafo, com potenciais aplicações em planejamento de rotas, redes de distribuição e muito mais.

## Referências
WIKIPÉDIA. Algoritmo de Prim. Disponível em: Algoritmo de Prim – Wikipédia, a enciclopédia livre (wikipedia.org).
GOOGLE. Maps. Disponível em: https://www.google.com.br/maps.
