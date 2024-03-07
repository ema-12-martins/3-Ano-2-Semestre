# MAC
No contexto deste código, MAC (Message Authentication Code) é um código usado para verificar a autenticidade e integridade de uma mensagem. É uma forma de garantir que a mensagem não tenha sido alterada ou adulterada após ter sido criada.

O HMAC (Hash-based Message Authentication Code) é uma construção específica de MAC que utiliza uma função de hash criptográfica, como SHA-256 neste caso, para gerar o código de autenticação a partir da chave secreta e dos dados da mensagem. Isso proporciona uma camada adicional de segurança, tornando o código mais resistente a ataques de falsificação de mensagem e de força bruta.

- h = hmac.HMAC(key, hashes.SHA256()): Aqui, estamos inicializando um objeto HMAC com a chave secreta key e o algoritmo de hash SHA-256. Isso cria um objeto HMAC que será usado para gerar o código de autenticação.

- h.update(b"message to hash"): Este comando atualiza o estado do objeto HMAC com a mensagem que queremos autenticar. Neste caso, estamos passando a mensagem "message to hash" como bytes para serem hash.

- h_copy = h.copy(): Esta linha cria uma cópia do objeto HMAC h. Isso pode ser útil se você precisar verificar o mesmo código de autenticação em diferentes momentos sem perder o estado do objeto original.

- h.verify(signature): Aqui, estamos verificando se o código de autenticação signature corresponde ao código gerado pelo objeto HMAC h para a mensagem fornecida. Se os códigos corresponderem, isso indica que a mensagem não foi alterada e que a autenticação foi bem-sucedida. Caso contrário, uma exceção será levantada indicando que a verificação falhou.