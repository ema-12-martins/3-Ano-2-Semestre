# Envio e receção de ficheiros
Como enviar ficheiros para uma app e como a aplicação vai lidar com eles. Temos 3 metedologias para o fazer:
1. **Envio em binário:** Tem a  desvantagem que no envio posso apenas mandar um ficheiro.
2. **Envio em multipack/form data:** Formulários.
3. **Base 64:** Pegar nos bytes e meter agrupados  para depois mandar um JSON.

# Envio em multipack
Temos de por:
~~~
enctype="multipart/form-data"
action="http..."
~~~

Comandos:
~~~
npm i
npm install --save multer
~~~

Se tivermos o campo **name** com o mesmo nome, ele agrupa numa array quando é mandado o formulário.3

# Form data
Usa o axios. Basicamente criamos o formulário à mão.