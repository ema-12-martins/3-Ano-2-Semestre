# Q1
A sequência de bytes gerada pelo bad_otp.py para a criação de chaves é muito menos aleatória, tornando a chave mais previsível e, consequentemente, mais suscetível a ataques.

# Q2
O ataque não contradiz a segurança do OTP, pois esta segurança é baseada na aleatoriedade da chave, no fato de ela ser usada apenas uma vez e em seu comprimento ser tão longo quanto a mensagem a ser criptografada. Como o gerador de chaves não é verdadeiramente aleatório, a segurança é comprometida. O ataque é possível devido à previsibilidade do gerador, que permite prever sequências a partir de um padrão base.

Portanto, o ataque não compromete a segurança do OTP, pois este é baseado em chaves verdadeiramente aleatórias.


