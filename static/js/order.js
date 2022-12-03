$(document).ready(function(){   
    var resume_table = document.getElementById("orders");
    var ptotal = document.getElementById('ptotal');
    var total = 0
    // for (var i = 0, row; row = orders.length; i++ ){
    for (var i = 1, row; row = resume_table.rows[i]; i++) {
        var precio = 0;
        var cant = 0;
        for (var j = 0, col; col = row.cells[j]; j++) {
            if (j == 2) {
                cant = col.innerHTML    
            }
            if (j == 3) {
                precio = col.innerHTML     
            }
        }
        total += precio * cant
    }
    ptotal.innerHTML = "Total: " + total;

    // $('#delete').on('click', function(event){
    //     let data = $('#formCarrito').serialize();
    //     console.log(data)
    //     event.preventDefault();
    //     alert("pintamos toda la casa")
    //     $.ajax({
    //         type:"POST",
    //         url: "/logeo/carrito/eliminar",
    //         data: data,
    //         processData: false,
    //         success: function () {
    //             $("#orders").load(window.location + " #orders*","");
    //         }
    //     });
    //     alert(data)
    //     return false
    // });


    
    /*for (let i = 0; i < orders.length; i++) {
        var cantidad = orders[i][2]
        var precio = orders[i][3]
        total += cantidad * precio
        alert(orders.length)
    }*/



});


function elimina(id_prod) {
    productoId = '#' + id_prod;
    var id = document.getElementById(productoId)
    console.log(productoId)
    var form = $(productoId).serialize()
    console.log(form)
    event.preventDefault();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    alert(window.location)
    $.ajax({
        type:"POST",
        url: "http://127.0.0.1:8000/logeo/carrito/eliminar",
        data: form,
        processData: false,
        success: function () {
            $("#orders").load(window.location + " #orders*","");
        }
    })       
    alert(id_prod)
    return false

}

