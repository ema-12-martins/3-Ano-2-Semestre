<template>
  <h1>{{dataAtual}}</h1>
  <h1>{{horaAtual}}</h1>

  <Pagina_Teste msg="Vais escrever isto" />

  <div v-if="visualizacao === 'Ativado'">
    <button @click="mudaVisualizacao">Clique para desativar a visualização</button>
  </div>
  <div v-else>
    <button @click="mudaVisualizacao">Clique para ativar a visualização</button>
  </div>

  <div v-if="visualizacao === 'Ativado'">
    <ul>
      <li v-for="(frase, index) in lista_de_frases" :key="index">{{ frase }}</li>
    </ul>
  </div>
  <div v-else>
    <p>Nao vamos listar</p>
  </div>

</template>

<script>
import Pagina_Teste from './components/Pagina_Teste.vue'

export default {
  name: 'App',
  components: {
    Pagina_Teste
  },
  data() {
    return {
      dataAtual: new Date().toLocaleDateString(),
      horaAtual: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      visualizacao: 'Desativado'
    }
  },
  created() {
    this.atualizarDataEHora();
    // Verifica a hora a cada segundo
    setInterval(this.atualizarDataEHora, 1000);
  },
  methods: {
    atualizarDataEHora() {
      const dataAtual = new Date();
      const dia = String(dataAtual.getDate()).padStart(2, '0');
      const mes = String(dataAtual.getMonth() + 1).padStart(2, '0');
      const ano = dataAtual.getFullYear();
      const hora = String(dataAtual.getHours()).padStart(2, '0');
      const minutos = String(dataAtual.getMinutes()).padStart(2, '0');
      this.dataAtual = `${dia}-${mes}-${ano}`;
      this.horaAtual = `${hora}:${minutos}`;
    },
    mudaVisualizacao() {
      if (this.visualizacao === 'Ativado') {
        this.visualizacao = 'Desativado';
      } else {
        this.visualizacao = 'Ativado';
      }
    }
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
