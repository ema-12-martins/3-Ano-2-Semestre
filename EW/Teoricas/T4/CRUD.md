# CRUD
### R-Retrive
Retrive-Recuperacao de informcacao. Os pedidos tipicos ao o listar os registos de uma colecao ou consultar apenas 1 registo.

Listar os pedidos de um colecao:
1. Recebo pedido de listar.
2. Pedir a API de dados a lisatgem dos registos.
3. Colocar o envelepe html HTLM: povoar um template com os dados.
4. Enviar a pagina HTML correspondente.

Consultar 1 registo de uma coleção:
1. Recebo pedido de consulta.
2. Extrair o id do registo do pedido.
3. Pedir à API de dados o registo.
4. Colocar o envelepe html HTLM: povoar um template com os dados.
5. Enviar a pagina HTML correspondente.

---

### C-Create
Pretendemos inserir 1 registo numa coleção:
1. Recebo pedido de consulta.
2. Extrair os dados do pedido que chegou.
3. Pedir à API a insercao do registo.
4. Colocar o envelepe html HTLM: povoar um template com os dados.
5. Enviar a pagina HTML correspondente.

---

### U-Update
O json server faz isto de maneira destrutiva enquanto o mongo bd faz incrementalmente, ou seja, o primeiro apaga e insere de novo enquanto o segundo altera o campo pretendido.

Alteração de um registo de uma coleção:
1. Recebo pedido de consulta.
2. Extrair o id do registo e os dados a altera do pedido.
3. Pedir à API a atualização do registo.
4. Colocar o envelepe html HTLM: povoar um template com os dados.
5. Enviar a pagina HTML correspondente.

---

### D-Delete
Pretende-se eliminar um registo de uma colecao:
1. Recebo pedido de eliminacao.
2. Extrair o id do registo pedido.
3. Pedir à API que elimine o registo.
4. Colocar o envelepe html HTLM: povoar um template com os dados.
5. Enviar a pagina HTML correspondente.


# Formulários WEB (HTML Forms)
Recolhe informação do lado do utilizador para a usar do lado do servidor. Pega no input e cria um script.

Podem ocnter campos de texto, check boxes, radio-buttons, submit buttons, select list...

~~~
<form>
    //Codigo do formulario
</form>
~~~

O form tem que ter um **name**,**action**(script que responde ao formulario), **method**(GET (tudo na query string) ou POST(vai a informacao no body)),**target**(pagina para mostrar resultado) e **enctype**(que tipo de informacao o formulario web manda). Este ultimo parametro pode ser application/x-www-form-urlencoded(default) ou multipart/form-data. O primeiro manda texto e o segundo permite mandar ficheiros.

---

### Type

**Input:** Para meter texto numa caixa.

**Password:** Campo de texto mas cifrado.

**Radio:** Deixa apenas selecionar uma das opcoes.

**Submit:** Para submeter o formulario.

Nota: **fieldset** mete uma caisa á volta dos componente que engolba.

# Recuros estaticos
- CSS
- JS
- Imagens

# Estrutura aplicacional
Pasta do serviço:
- Public: Imagens, JavaScript e CSS.

# TPC4

dataset compositores musicais.
colocar o dayaset no json-server
Rotas importantes:

/compositores

/compositores/{id}

/compositores?perido={periodo}

/periodos

/peiodos/{id}

Implementar as operacaes crud sobre compositores e sobre periodos.