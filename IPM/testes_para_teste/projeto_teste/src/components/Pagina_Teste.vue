<template>
  <div class="container-1">
    <h1>{{ msg }}</h1>
    <p>Este é só um texto exemplo para testar coisas em CSS.</p>
    <p>Não se percebe porque temos de programar CSS no papel mas faz parte.</p>
  </div>

  <div class="container-2">
    <ul>
      <li>{{ frase1 }}</li>
      <li>{{ frase2 }}</li>
    </ul>
  </div>

  <div class="container-3">
    <input type="text" id="nome" name="nome" :value="frase_nova" @input="atualiza_frase_nova" />
    <button @click="mudaFrase">Clica aqui e muda uma frase</button>
  </div>
</template>

<script>
export default {
  name: 'Pagina_Teste',
  props: {
    msg: String
  },
  data() {
    return {
      frase1: 'Isto é uma lista',
      frase2: 'Temos vários elementos na lista',
      frase_nova: '',
      contador: 0
    }
  },
  methods: {
    atualiza_frase_nova(event) {
      this.frase_nova = event.target.value
    },
    mudaFrase() {
      const valor_a_trocar = this.frase_nova.trim()
      this.contador += 1
      if (valor_a_trocar===''){
        alert('Intruduza texto antes de submeter')
        this.frase_nova=''
      }else{
        if (this.contador % 2 == 0) {
          this.frase2 = valor_a_trocar
          this.frase_nova = ''
        } else {
          this.frase1 = valor_a_trocar
          this.frase_nova = ''
        }
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container-1 {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: rgb(133, 65, 65);
  
}

.container-2{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: grey;
}

.container-3{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-top: 20px;
}

ul{
  list-style-type: none;
}

</style>
