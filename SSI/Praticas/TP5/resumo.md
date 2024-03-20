# Diffie-Hellman

O protocolo de acordo de chaves Diffie-Hellman (DH) é um método criptográfico utilizado para que duas partes possam estabelecer uma chave secreta compartilhada sobre um canal inseguro. Esse protocolo é baseado na dificuldade do problema do logaritmo discreto em um corpo finito.

Aqui está como o protocolo funciona passo a passo, conforme sua descrição:

Alice gera um valor secreto e calcula gx:
Alice escolhe um número aleatório, vamos chamá-lo de x.Ela usa o valor público g (um gerador) e o valor público p (um número primo) para calcular gx: gx = g^x mod p. Alice envia gx para Bob.

Bob gera um valor secreto e calcula gy:
Bob escolhe um número aleatório, vamos chamá-lo de y. Ele usa o mesmo valor público g e p para calcular gy: gy = g^y mod p. Bob envia gy para Alice.

Alice e Bob calculam a chave mestra:
Alice recebe gy de Bob, enquanto Bob recebe gx de Alice.Alice calcula a chave mestra usando o valor recebido gy e seu próprio valor secreto x: Kmaster = gy^x mod p.Bob calcula a chave mestra usando o valor recebido gx e seu próprio valor secreto y: Kmaster = gx^y mod p. O resultado final é que tanto Alice quanto Bob agora têm a mesma chave mestra, que pode ser usada para comunicação segura.

O que torna o protocolo seguro é que mesmo que um atacante intercepte gx e gy, calcular a chave mestra sem conhecer x ou y é computacionalmente inviável devido à dificuldade do problema do logaritmo discreto em um corpo finito.

Essencialmente, o protocolo de Diffie-Hellman permite que duas partes concordem sobre uma chave secreta compartilhada sem nunca transmitir essa chave pela rede, garantindo assim a confidencialidade dos dados.

# KDF
Uma prática comum derivar chaves criptográficas adicionais a partir da chave mestra estabelecida usando uma Função de Derivação de Chave (KDF), como o HKDF (HMAC-based Key Derivation Function). A KDF é usada para garantir que as chaves derivadas sejam suficientemente seguras e independentes da chave mestra original. Aqui está uma breve explicação sobre como isso funciona:

HKDF (HMAC-based Key Derivation Function): O HKDF é uma função de derivação de chave que utiliza a HMAC (Hash-based Message Authentication Code) como seu componente fundamental. Ela é projetada para derivar chaves criptográficas seguras a partir de um material inicial de chave, geralmente uma chave mestra.

Processo de derivação: O processo de derivação de chave com o HKDF geralmente envolve três etapas principais:
- Extração (Extract): Se a chave mestra não for uniformemente distribuída, um passo de extração é realizado para transformá-la em uma chave pseudoaleatória de tamanho fixo. Isso é feito aplicando uma função de hash (por exemplo, HMAC) na chave mestra.
- Expansão (Expand): O HKDF usa o material extraído para expandir a chave para produzir chaves criptográficas de tamanho variável. Isso geralmente é feito usando funções de hash criptográfico adicionais.
- Derivação (Derive): Com as chaves expandidas, podem ser derivadas várias chaves criptográficas, cada uma destinada a um propósito específico, como criptografia, autenticação, etc.