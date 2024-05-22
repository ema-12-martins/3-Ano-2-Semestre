<template>
  <div id="geral">
    <div id="grid">
      <div id="titulo">
        <h1>Countdown 1</h1>
      </div> 
      <div id="lado">
        <h1>Segunda Linha</h1>
      </div>
      <div id="slide">
        <h1>Terceira Linha</h1>
      </div>
      <div id="cancel"> 
        <botom >Cancel</botom>
      </div>
      <div id="save">
        <botom>Save</botom>
      </div>
    </div>
  </div>  
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

#geral{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

#grid{
  display: grid;
  grid-template-columns: 1fr auto;
  grid-template-rows: 1fr auto;
  gap: 20px 10px;
  grid-template-areas:
    ". . . . ."
    ". . titulo . ."
    ". . lado . ."
    ". . slide . ."
    ". cancel . save ."
    ". . . . .";
  color: #000000;
}

#titulo{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  grid-area: titulo;
}

#lado{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  grid-area: lado;
}

#slide{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  grid-area: slide;
}

#cancel{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  grid-area: cancel;
}

#save{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  grid-area: save;
}

</style>
