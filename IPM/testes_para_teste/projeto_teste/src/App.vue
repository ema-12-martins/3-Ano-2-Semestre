<template>
  <div id="container-1"> 
    <h1>{{dataAtual}}</h1>
    <h1>{{horaAtual}}</h1>
  </div>

  <div id="container-2"> 
    <Pagina_Teste msg="Vais escrever isto" />
  </div> 

  <div id="container-3">
    <div v-if="visualizacao === 'Ativado'">
      <button @click="mudaVisualizacao">Clique para desativar a visualização</button>
    </div>
    <div v-else>
      <button @click="mudaVisualizacao">Clique para ativar a visualização</button>
    </div>

    <div v-if="visualizacao === 'Ativado'">
      <ul>
        <li v-for='(frase, index) in lista_de_frases' :key='index'>{{ frase }}</li>
      </ul>
    </div>
    <div v-else>
      <p>Nao vamos listar</p>
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

#container-1{
  background-color: aqua;
  grid-area: container-1;
}

#container-2{
  background-color: blueviolet;
  grid-area: container-2;
}

#container-3{
  background-color: goldenrod;
  grid-area: container-3;
}


</style>
