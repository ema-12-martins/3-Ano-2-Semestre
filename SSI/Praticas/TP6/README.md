# Q1
Para verificar se as chaves fornecidas nos arquivos MSG_SERVER.key e MSG_SERVER.crt constituem de fato um par de chaves RSA válido, priemiro temos de verificar se o formato dos arquivos é correto. Depois, temos de validar a chave pública presente no certificado. Por último, é necessário testar o emparelhamento das chaves, criptografando ou assinando dados com a chave privada e verificando a correspondência utilizando a chave pública.

# Q2
Os campos que tem de ser verificados são a data, os atributos do campo subject e a validação das extensões do certificado.