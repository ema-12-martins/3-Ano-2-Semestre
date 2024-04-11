const app = Vue.createApp({
    data: function () {
        return {
            nome_mecanico: "",
            pass_mecanico: ""
        }
    },
    methods: {
        valida_mecanico(){ 
            if((this.nome_mecanico=="venancio" && this.pass_mecanico=="1234")){
                return true
            }else{
                return false
            }
        }
    },
});

app.mount("#reactive-app");