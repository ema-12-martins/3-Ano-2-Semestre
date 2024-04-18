# ChaCha20
Esta é uma cifra **sequêncial** que cifra bit a bit.

1. Para a inicialização, o ChaCha20 precisa de uma chave criptográfica e um nonce(número usado uma única vez).
2. A partir da chave e do nonce, o ChaCha20 gera um stream de chaves que é uma sequencia de bits pseudo-aleatórios. Isto é feito com rotações de bits...
3. Com a stream de chaves gerada, faz-se um XOR desse strem com os dados que se deseja cifrar.

4. Após cada bloco de dados processado, o ChaCha20 gera uma nova strem de chaves. Isto é feito alterando o nonce ou o contador interno do algoritmo.
5. Depois de todos os cados serem cifrados, o processo fica concluído.

O ChaCha20 tem a vantagem de ser rápido e eficiente. É usado em protocolos como TLS, SSH e outros.

# Exemplo ChaCha20
Vamos supor que queremos cifrar a mensagem "Hello, world!" Usando ChaCha20 com uma chave de 256bits e um nonce de 64bits.

1. Escolher uma chave de 256bits(b2 bytes) e um nonce de 64bits(8bytes). Podemos ter, por exemplo a chave=0x0102030405060708091011121314151617181920212223242526272829303132 e o Nonce=0x000000000000004a.

2. Esta etapa tem vários passos:
- Preparação dos dados: A chave de criptografia e o nonce são combinados com constantes fixas para formar o bloco de entrada inicial do algoritmo.
- Iterações: O algoritmo executa várias iterações de uma função de mistura. Cada iteração produz uma parte do stream de chaves.
- Função de Mistura: A função de mistura envolve várias operações matemáticas, incluindo adições modulares, rotações de bits e operações XOR. Essa função embaralha os dados de entrada de forma a produzir um novo conjunto de dados, que é então usado na próxima iteração.
- Gerando o Stream de Chaves: Após um número específico de iterações, o resultado final é extraído como parte do stream de chaves.

3. Para cifrar vamos usar o XOR:
- Mensagem original: "Hello, world!"
- Mensagem em hexadecimal: 0x48656c6c6f2c20776f726c6421
- Stream de chaves (primeiros 16 bytes): 0x5a79c4c3dc5ea5bb1d83edcfb217e9f7
- Mensagem cifrada (resultado do XOR): 0x12869a877a3384cc0c5cafb5b9639e6e