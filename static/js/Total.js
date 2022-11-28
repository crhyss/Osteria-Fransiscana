// function TotalCompra(){
//     var total = localStorage.getItem('total');
//     var consulta = document.querySelector('#totalComp');
//     var consulta1 = document.querySelector('#totalComp');
//     var detalle = document.querySelector('#detalle');
//     var TotaCompra = Number(total) + 3500;
//     console.log(TotaCompra)
//     detalle.innerHTML += 'Se agregará $3500 al total por envio. Total:'+total;
//     consulta1.innerHTML += TotaCompra;
//     consulta.innerHTML +='<input id="amount" name="amount" hidden value="'+TotaCompra+'"/>' 
//     console.log(document.querySelector('#totalComp').innerHTML)
// }
// TotalCompra()

function DetalleCompra(){
    var consulta = document.querySelector('#totalComp');
    const Button = document.getElementById('activador');
    var total = localStorage.getItem('total');
    var TotalProducto = document.querySelector('#TotalProducto');
    var TotalVenta = document.querySelector('#TotalVenta');
    var CostoEnvio = document.querySelector('#CostoEnvio');
    TotalProducto.innerHTML = '$'+ total
    CostoEnvio.innerHTML = '$0'
    TotalVenta.innerHTML = '$'+ total;
    consulta.innerHTML +='<input id="amount" name="amount" hidden value="'+total+'"/>' 
    if ($('#exampleModal').modal('hide')) {
        Button.disabled = false
    }
    $('#exampleModal').modal('hide');
    localStorage.removeItem('total')
    localStorage.removeItem('orders')
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    if (orders === null || orders === undefined) {
        localStorage.setItem('orders',JSON.stringify([]));
        orders = JSON.parse(localStorage.getItem('orders'))
    }

    if (total === null || total === undefined) {
        localStorage.setItem('total',0);
        total = localStorage.getItem('total');
    }
}
DetalleCompra()

