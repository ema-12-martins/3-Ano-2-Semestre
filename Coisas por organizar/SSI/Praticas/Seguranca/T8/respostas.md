# Q1
Para criar ficheiros usamos o comando:
~~~
touch exemplo_ficheiro1
touch exemplo_ficheiro2
~~~

Para ver as permissões:
~~~
umask -S
umask
~~~
Percemos que as minhas permissões são u=rwx,g=rwx,o=rx.u=rwx,g=rwx,o=rx (0002)

Para colocar todos com todas as permissões,temos de mudar o usemask para 0000.
~~~
umask 0000
~~~

Para ver as permissões dos ficheiros:
~~~
ls -l
~~~

Obtivemos como resultado:
~~~
-rw-rw-r-- 1 emamartins12 emamartins12    0 abr 18 14:20 exemplo_ficheiro1
-rw-rw-r-- 1 emamartins12 emamartins12    0 abr 18 14:20 exemplo_ficheiro2
~~~

Para mudar as permissões do ficheiro:
~~~
chmod o+x exemplo_ficheiro1
~~~
Agora está como executável:
~~~
-rw-rw-r-x 1 emamartins12 emamartins12    0 abr 18 14:20 exemplo_ficheiro1
-rw-rw-r-- 1 emamartins12 emamartins12    0 abr 18 14:20 exemplo_ficheiro2
~~~

Para criar a pasta dir1:
~~~
mkdir dir1
~~~

Como tinhamos mudado o umask, a pasta criada tem permissões para tudo:
~~~
drwxrwxrwx 2 emamartins12 emamartins12 4096 abr 18 14:31 dir1
~~~

# Q2
Para ver os grupos em que estou:
~~~
groups
~~~
Obtive:
~~~
emamartins12 adm cdrom sudo dip plugdev lpadmin lxd sambashare docker
~~~
Para ver os grupos a que pertenço:
~~~
uid=1000(emamartins12) gid=1000(emamartins12) grupos=1000(emamartins12),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),134(lxd),135(sambashare),999(docker)
~~~

---
Vamos criar utilizadores:
~~~
sudo useradd a97678
sudo useradd a108831
sudo useradd a100534
~~~
Para criar um grupo:
~~~
sudo groupadd os_meus_numeros
sudo groupadd sem_todos_numeros
~~~
Para ver os todos os grupos existentes:
~~~
tail /etc/group
~~~
Obtivemos:
~~~
emamartins12:x:1000:
sambashare:x:135:emamartins12
wireshark:x:136:
mysql:x:137:
_flatpak:x:138:
fwupd-refresh:x:139:
docker:x:999:emamartins12
a97678:x:1001:
a108831:x:1002:
os_meus_numeros:x:1003:
~~~
Agora queremos adicionar os utilizadores a97678 e a108831 ao grupo os_meus_numeros:
~~~
sudo usermod -aG os_meus_numeros a97678
sudo usermod -aG os_meus_numeros a108831
sudo usermod -aG os_meus_numeros a100534
sudo usermod -aG sem_todos_numeros a97678
sudo usermod -aG sem_todos_numeros a108831
~~~
Fazendo o comando anterior, vemos que foram adicionados ao grupo:
~~~
os_meus_numeros:x:1003:a97678,a108831
sem_todos_numeros:x:1005:a97678,a108831
~~~
Para mudar a palavra-passe do utilizador:
~~~
sudo passwd a97678
~~~
Para iniciar sessão com o utilizador:
~~~
su a97678
~~~
Percebemos que pertencemos aos seguintes grupos:
~~~
id
uid=1001(a97678) gid=1001(a97678) grupos=1001(a97678),1003(os_meus_numeros),1005(sem_todos_numeros)
~~~

# Q3
Comecei por criar um ficheiro texto.txt com o seguinte conteúdo:
~~~
Olá
Olá
~~~
Criei um ficheiro e C para imprimir no terminal o conteúdo de um ficheiro de texto passado como argumento:
~~~c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s <nome_do_arquivo>\n", argv[0]);
        return 1;
    }

    FILE *arquivo = fopen(argv[1], "r");
    if (arquivo == NULL) {
        fprintf(stderr, "Erro ao abrir o arquivo '%s'\n", argv[1]);
        return 1;
    }

    char linha[256];
    while (fgets(linha, sizeof(linha), arquivo) != NULL) {
        printf("%s", linha);
    }

    fclose(arquivo);

    return 0;
}

~~~
Para definir permissão de setuid para o ficheiro executável gerado a partir do ficheiro anterior:
~~~
sudo chmod u+s ler
~~~
Para confirmar se foi atribuida a elevação de privilégios:
~~~
ls -l
-rwsrwxrwx 1 emamartins12 emamartins12 16208 abr 18 15:08 ler
~~~
Mudei agora de utilizador e verifiquei que mesmo,apesar de não ser o criador do ficheiro, foi-lhe atribuido as mesmas permissões do que as do utilizador que o criou.

# Q4
Para ver as permissões da lista extendida:
~~~
getfacl ler

# file: ler
# owner: emamartins12
# group: emamartins12
# flags: s--
user::rwx
group::rwx
other::rwx
~~~
Agora, o utilizador a97678 tem permissões num ficheiro que não tinha mesmo não pertencendo a nenhum grupo que tem essas permissões.
~~~
sudo setfacl -m u:a97678:w ler
sudo setfacl -m g:os_meus_numeros:w ler
~~~
Podemos verificar que lhe foram atribuidas as permissões:
~~~
getfacl ler

# file: ler
# owner: emamartins12
# group: emamartins12
# flags: s--
user::rwx
user:a97678:-w-
group::rwx
group:os_meus_numeros:-w-
mask::rwx
other::rwx
~~~
