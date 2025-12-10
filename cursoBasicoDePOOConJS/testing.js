class Banda {
    constructor({
        nombre,
        generos = [],
    }) {
        this.nombre = nombre;
        this.generos = generos;
        this.integrantes = [];
    }
    agregarIntegrante(integranteNuevo) {
        // Tu código aquí 👈
        let x = this.integrantes.map(y => {
            if (y.instrumento == (integranteNuevo.instrumento)){
                return true
            };
            
        });

        if (x == false) {
            this.integrantes.push(integranteNuevo)
        }
    }
}

//Crear clase Integrante
class Integrante {
    // Tu código aquí 👈
    constructor({ nombre, instrumento }) {
        this.nombre = nombre,
            this.instrumento = instrumento
    }
}

const data = {
    nombre: "Los Jacks",
    generos: ["rock", "pop", "post-punk"],
    integrantes: [],
}
const banda = new Banda(data)
banda.agregarIntegrante(new Integrante({ nombre: "Erik", instrumento: "Guitarra" }))
banda.agregarIntegrante(new Integrante({ nombre: "Paul", instrumento: "Bateria" }))
banda.agregarIntegrante(new Integrante({ nombre: "Logan", instrumento: "Bateria" }))

console.log(banda)