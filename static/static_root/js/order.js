var total = localStorage.getItem('total');
if (total === null || total === undefined) {
        localStorage.setItem('total',0);
        total = localStorage.getItem('total');
    }
$(document).ready(function(){
    addToCart()
});
function elimina(id_prod, precio,cantidad) {
    productoId = '#' + id_prod;
    let form = $(productoId).serialize()
    deleteLocal(precio,cantidad)
    event.preventDefault();
    $.ajax({
        type:"POST",
        url: "/logeo/carrito/eliminar/",
        data: form,
        success: function () {
            $("#orders").load(window.location + " #orders*","");
        },
    })       
}

function addToCart() {
    total = 0
    var table = document.getElementById("orders");
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i];
        var quantity = row.cells[2].innerHTML;
        var price = row.cells[4].innerHTML;
        total += Number(price) * Number(quantity) 
      }
      ptotal.innerHTML = "Total: " + total;
      total = total.toString();
      localStorage.setItem("total", total);
    isAdding = true;
  }
function deleteLocal(precio,cantidad) {

    total = parseInt(total);
    tprod = precio * cantidad
    total -= tprod;
    total = total.toString();
    localStorage.setItem("total", total);
    ptotal.innerHTML = "Total: " + total;
}


function aniadirProd(id_produ,precio,cantidad) {
    productoId = '#preci' + id_produ;
    let form = $(productoId).serialize()
    agregardesdevista(precio,cantidad)
    event.preventDefault();

    $.ajax({
        type:"POST",
        url: "/logeo/orders/",
        data: form,
        success: function () {
            $("#orders").load(window.location + " #orders*","");
        },
    })       
}

function agregardesdevista(precio,cantidad) {

    total = parseInt(total);
    tprod = precio * cantidad
    total += tprod;
    total = total.toString();
    localStorage.setItem("total", total);
    ptotal.innerHTML = "Total: " + total;
}