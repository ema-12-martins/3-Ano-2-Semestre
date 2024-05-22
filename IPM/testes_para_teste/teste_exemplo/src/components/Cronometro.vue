<template>
    <my-label :id="cronoName" />
    
    <div class="horiz1">
      <button @click="decrease">&#9664;</button>{{ crValue }}s
      <button @click="increase">&#9658;</button>
    </div>

    <div class="slide">
      <h1>----------------</h1>
    </div>
    
    <div class="horiz2">
      <button @click="onCancel">Cancel</button>
      <button @click="onSave">Save</button>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
      visualizacao_diminuida:false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

#grid{
  display: grid;
  grid-template-columns: 1fr auto;
  grid-template-rows: 1fr auto;
  gap: 20px 20px;
  grid-template-areas:
    ". . . . .";
  color: #000000;
}


</style>
