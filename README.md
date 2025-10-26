O trabalho inclui desde o pré-processamento e limpeza dos dados até o treinamento, avaliação e comparação de resultados entre os modelos.

Estrutura do Projeto

Pasta scripts_limpeza
Contém os códigos responsáveis pela limpeza dos datasets originais, onde foram removidos ruídos, transformadas as labels em formato binário e convertidos os arquivos para CSV, facilitando a manipulação.
O dataset Boatos BR foi balanceado nesse processo.
Todos os códigos foram desenvolvidos em Python, no ambiente Visual Studio.

Pasta datasets
Reúne os datasets originais utilizados, FakeRecogna e Boatos BR, antes da limpeza e tratamento.
Também contém os datasets finais pós-tratamento, sendo:

Um dataset de teste, com 20% das notícias;

Um dataset de treinamento, com 80% das notícias;

E o dataset completo final, antes da separação em treino e teste.

Arquivo BERTimbau.ipynb
Contém o treinamento do modelo BERTimbau, desenvolvido em Python no ambiente Google Colab.

Arquivo GPT.ipynb
Executa o teste de previsões com o modelo GPT-4, avaliando o desempenho da LLM sobre o conjunto de teste.
Desenvolvido em Python no ambiente Colab.

Arquivo predicoes_BERT.ipynb
Responsável por aplicar o modelo BERTimbau sobre o dataset de teste, gerando as previsões e métricas de avaliação.
Desenvolvido em Python no ambiente Colab.

Pasta resultados_previsoes
Armazena os arquivos de saída e previsões gerados pelos testes do modelo GPT-4 e do BERTimbau.
