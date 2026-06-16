### `scripts_limpeza`
Contém os códigos responsáveis pela limpeza inicial dos datasets originais, incluindo a remoção de ruídos, emojis, espaços em brancos, a transformação das labels em formato binário e a conversão dos arquivos para CSV. Também estão incluídos os scripts de pré-processamento textual, responsáveis pela remoção de pontuações, acentuações e stopwords. 
Todos os códigos foram desenvolvidos em **Python**. 

---

### `datasets`
Reúne os **datasets originais** utilizados —*Fake.br* , *FakeRecogna* e *FakeTrueBr* — antes da limpeza e tratamento.  

Também contém os **datasets finais pós-tratamento**, sendo:  
- Dataset **completo final**, antes da separação em treino e teste.
- Dataset de **teste**, com **20% das notícias**;
- Dataset de **validação**, com **20% das notícias**;
- Dataset de **treinamento**, com **60% das notícias**;  


