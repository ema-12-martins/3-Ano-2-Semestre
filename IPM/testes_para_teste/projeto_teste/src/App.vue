<template>
  <div id="container-1" class="container"> 
    <h1>{{ dataAtual }}</h1>
    <h1>{{ horaAtual }}</h1>
  </div>

  <div id="container-2" class="container"> 
    <Pagina_Teste msg="Vais escrever isto" @lista_de_frases="atualizarListaDeFrases" />
  </div> 

  <div id="container-3" class="container">
    <button @click="mudaVisualizacao">
      Clique para {{ visualizacao === 'Ativado' ? 'desativar' : 'ativar' }} a visualização
    </button>
    
    <div v-if="visualizacao === 'Ativado'">
      <ul>
        <li v-for="(frase, index) in lista_de_frases" :key="index">{{ frase }}</li>
      </ul>
    </div>
    <div v-else>
      <p>Não vamos listar</p>
    </div>
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
      visualizacao: 'Desativado',
    }
  },
  created() {
    this.atualizarDataEHora();
    // Atualiza a hora a cada minuto
    setInterval(this.atualizarDataEHora, 60000);
  },
  methods: {
    atualizarDataEHora() {
      const dataAtual = new Date();
      this.dataAtual = dataAtual.toLocaleDateString();
      this.horaAtual = dataAtual.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    },
    mudaVisualizacao() {
      this.visualizacao = this.visualizacao === 'Ativado' ? 'Desativado' : 'Ativado';
    },
    atualizarListaDeFrases(novaListaDeFrases) {
      this.lista_de_frases = novaListaDeFrases;
    }
  }
}
</script>

<style>
#app {
  display: grid;
  grid-template-columns: 1fr auto;
  grid-template-rows: 1fr auto;
  gap: 20px 10px;
  grid-template-areas:
    "container-1"
    "container-2"
    "container-3";
  color: #000000;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  margin: 5px 0;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

#container-1 {
  background-color: aqua;
  grid-area: container-1;
}

#container-2 {
  background-color: blueviolet;
  grid-area: container-2;
}

#container-3 {
  background-color: goldenrod;
  grid-area: container-3;
}

@media screen and (max-width: 640px) {
  .container {
    min-width: 300px;
  }
}
</style>
