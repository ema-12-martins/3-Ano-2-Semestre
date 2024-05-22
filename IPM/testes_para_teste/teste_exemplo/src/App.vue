<template>
  <div class="app">
    <div class="cronometro-container">
      <Cronometro />
    </div>
  </div>
</template>

<script>
import Cronometro from './components/Cronometro.vue';

export default {
  name: 'App',
  components: {
    Cronometro
  }
}
</script>

<style>
.app {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: black;
}

.cronometro-container {
  height: 40%; /* Ajuste a altura conforme necessário */
  width: 40%;
  background-color: aliceblue;
}
</style>
