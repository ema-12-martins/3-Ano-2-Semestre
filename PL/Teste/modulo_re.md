# Expressões Regulares
Alguns conceitos de expressões regulares:
- **a** corresponde ao caracter a
- **a?** corresponde a 0 ou mais ocorrencias do caracter a
- **a+** corresponde a 1 ou mais ocorrencias do caracter a
- **[abc]** corresponde a uma ocorrencia dos caracteres a b ou c
- **[a-z]** corresponde aos caracteres de a a z
- **^** corresponde ao inicio de uma string
- **$** corresponde ao fim de uma string
- **[^abc]** corresponde a qualquer ocorrencia desde que não seja a, b ou c
- **b{3}** temos 3 ocorrenacias de b
- **(a)** para formar grupos de captura
- **(?i:teste)** para apanhar casos sem ter em conta de é maiuscula ou minuscula

# Modulo RE
O método **match** procura um padrão no início de uma string.
~~~ python
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "123abc456"
match = re.match(pattern, text)

if match:
    print("Match encontrado:", match.group())  # Saída: 123
else:
    print("Nenhum match encontrado.")
~~~

O método **search** procura pelo padrão em qualquer posição da string.
~~~ python
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456"
search = re.search(pattern, text)

if search:
    print("Search encontrado:", search.group())  # Saída: 123
else:
    print("Nenhum search encontrado.")
~~~

O método **compile** compila um padrão regex em um objeto regex, que pode ser reutilizado.
~~~ python
import re

pattern = re.compile(r"\d+")  # Compila o padrão para encontrar um ou mais dígitos
text = "abc123def456"
search = pattern.search(text)

if search:
    print("Search encontrado:", search.group())  # Saída: 123
else:
    print("Nenhum search encontrado.")
~~~

O método **findall** retorna todas as ocorrências não sobrepostas do padrão em uma string.
~~~ python 
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456ghi789"
all_matches = re.findall(pattern, text)
print("Findall encontrado:", all_matches)  # Saída: ['123', '456', '789']
~~~

O método split divide uma string pelo padrão especificado.
~~~python 
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456ghi789"
split_text = re.split(pattern, text)
print("Split resultado:", split_text)  # Saída: ['abc', 'def', 'ghi', '']
~~~

O método **sub** substitui todas as ocorrências do padrão por uma string de substituição.
~~~ python
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456ghi789"
replaced_text = re.sub(pattern, "#", text)
print("Sub resultado:", replaced_text)  # Saída: abc#def#ghi#

~~~




