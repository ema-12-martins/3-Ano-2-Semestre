const app = Vue.createApp({
    data() {
        return {
            nome_mecanico: "",
            pass_mecanico: "",
            data: new Date().toLocaleDateString(),
            hora: new Date().toLocaleTimeString()
        }
    },
    methods: {
        validaMecanico() { 
            let nome = this.nome_mecanico.trim()
            let pass = this.pass_mecanico.trim()

            if (nome === "venancio" && pass === "1234") {
                console.log("Próxima Página")
            } else {
                console.log("Dados incorretos")
            }
        }
    },
    mounted() {
        setInterval(() => {
            this.hora = new Date().toLocaleTimeString()
        }, 1000);
    }
});

app.mount("#app");