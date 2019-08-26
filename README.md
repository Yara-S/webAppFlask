# webAppFlask
Aplicacao web simples utilizando o framework Flask


1. Visualização web retornando o próprio html na função (edicao de html dentro de código python): run.py e first.py 
2. Visualizacao web utilizando routing: run2.py

Para rodar a aplicação containerizada com Docker:

(dentro do diretorio)

docker build -t meuapp:latest .

docker run -p 8080:8080 meuapp:latest

