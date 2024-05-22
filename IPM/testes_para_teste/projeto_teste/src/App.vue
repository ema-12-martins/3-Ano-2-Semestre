<template>
  <Pagina_Teste msg="Vais escrever isto"/>
</template>

<script>
import Pagina_Teste from './components/Pagina_Teste.vue'

export default {
  name: 'App',
  components: {
    Pagina_Teste
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  margin-top: 60px;
}
</style>
