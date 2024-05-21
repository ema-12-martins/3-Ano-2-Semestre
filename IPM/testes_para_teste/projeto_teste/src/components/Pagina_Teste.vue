<template>
  <div class="container-1">
    <h1>{{ msg }}</h1>
    <p>Este é só um texto exemplo para testar coisas em CSS.</p>
    <p>Não se percebe porque temos de programar CSS no papel mas faz parte.</p>
  </div>
</template>

<script>
export default {
  name: 'Pagina_Teste',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container-1{
  display: flex;
  flex-direction: column;
  justify-content: space-around;

  background-color: aqua;
}
</style>
