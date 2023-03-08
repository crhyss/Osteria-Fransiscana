const lista = document.getElementById('lista');

Sortable.create(lista,{
    animation: 150,
    chosenClass: "seleccionado",
    dragClass:"drag",

    onEnd: () => {
        console.log('se inserto un elemento')
    },
    group:"lista-graficos",
    store: {
        //guarda el orden de los graficos
        set: (sortable) => {
            const orden = sortable.toArray();
            localStorage.setItem(sortable.options.group.name,orden.join('-'));
        },
        //obtener el orden de los graficos
        get: (sortable) =>{
            const orden = localStorage.getItem(sortable.options.group.name);
            return orden ? orden.split('-') : [];
        }
    },
})