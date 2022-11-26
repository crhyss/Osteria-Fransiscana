function TotalCompra(){
    var total = localStorage.getItem('total');
    var consulta = document.querySelector('#totalComp');
    var consulta1 = document.querySelector('#totalComp');
    var detalle = document.querySelector('#detalle');
    var TotaCompra = Number(total) + 3500;
    console.log(TotaCompra)
    detalle.innerHTML += 'Se agregará $3500 al total por envio. Total:'+total;
    consulta1.innerHTML += TotaCompra;
    consulta.innerHTML +='<input id="amount" name="amount" hidden value="'+TotaCompra+'"/>' 
    console.log(document.querySelector('#totalComp').innerHTML)
}
TotalCompra()
