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
    consulta.innerHTML += '<input id="tipoventa" name="tipoventa" hidden value="3"/>'

    if ($('#exampleModal').modal('hide')) {
        if(total > 0){
            Button.disabled = false
        }
        
    }
    $('#exampleModal').modal('hide');
}
DetalleCompra()
function DetalleCompraDelivery(){
    var consulta = document.querySelector('#totalComp');
    const Button = document.getElementById('activador');
    var total = localStorage.getItem('total');
    var TotalProducto = document.querySelector('#TotalProducto');
    var TotalVenta = document.querySelector('#TotalVenta');
    var CostoEnvio = document.querySelector('#CostoEnvio');
    var totalDelivery = Number(total) + 3500
    TotalProducto.innerHTML = '$'+ total
    CostoEnvio.innerHTML = '$3500'
    TotalVenta.innerHTML = '$'+ totalDelivery
    consulta.innerHTML +='<input id="amount" name="amount" hidden value="'+totalDelivery+'"/>' 
    consulta.innerHTML += '<input id="tipoventa" name="tipoventa" hidden value="2"/>'

    if ($('#exampleModal2').modal('hide')) {
        if(total > 0){
            Button.disabled = false
        }
        
    }
    $('#exampleModal2').modal('hide');    
}
DetalleCompraDelivery()
// localStorage.removeItem('total')
// var total = localStorage.getItem('total');
// if (total === null || total === undefined) {
//     localStorage.setItem('total',0);
//     total = localStorage.getItem('total');
// }

