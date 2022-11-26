var pcart = document.querySelector('#pcart')
var ptotal = document.querySelector('#ptotal')
var carrito = []

function productoCarrito(prod) {
    // obtener nombre
    productoId = '#prod' + prod;
    var nombre = document.querySelector(productoId).innerHTML;
    //obtener precio
    productoPrec = '#prec' + prod;
    var precio = document.querySelector(productoPrec).innerHTML;
    const strprecio = precio
    const newprecio = strprecio.slice(1)

    //obtener imagen
    productoimg = '#img' + prod;
    var imagen = document.querySelector(productoimg).src;
    var orders = JSON.parse(localStorage.getItem('orders')) || [[]];
    var total = localStorage.getItem('total');
    var cartSize = orders.length //la cantidad de productos agregados
    //cantidad de producto
    cantProd = '#cant'+prod;
    var cantidad = document.querySelector(cantProd).value
    // guardar en localstore
    //orders[cartSize] = [nombre,imagen,precio];
    if (orders.length == 0) {
        console.log('No hay productos en el carrito y añado 1')
        orders[cartSize] = {nombre, imagen, precio, cantidad, prod}
        localStorage.setItem('orders', JSON.stringify(orders));
        total = Number(total) + Number(newprecio);
        localStorage.setItem('total', total);
        var cart = document.querySelector('#cart');
        cart.innerHTML = orders.length;
        var cartSize = orders.length
        boton = '<button class="btn btn-danger buttonDelete" onclick="removercompra(' + cartSize + ')" type="button">X</button>'
        ptotal.innerHTML = 'Total:' + total + ' ';
        for (let i = 0; i < cartSize; i++) {
            boton = '<button class="btn btn-danger buttonDelete" onclick="removercompra(' + i + ')" type="button">X</button>'
            pcart.innerHTML += '<div class="col-6 border-bottom">' +
                '<div class="d-flex align-items-center pb-3 pt-3">' +
                '<img src=' + orders[i].imagen + ' class="img-thumbnail" style="width: 35%">' +
                '<p class="mb-0 ml-3" id ="' + orders[i].prod + '" >' + orders[i].nombre + '</p> </div></div>' +
                '<div class="col-2">' +
                '<div class=" d-flex align-items-center h-100 border-bottom pb-2 pt-3">' +
                '<p class="item-price mb-0 ">' + orders[i].precio + '</p> </div> </div>' +
                '<div class="col-4 d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">' +
                '<input class="form-control" id="number' + orders[i].prod + '" onclick="aumentarcompra(\''+i+'\','+orders[i].cantidad+','+orders[i].prod +')" type="number" value="' + orders[i].cantidad + '">' + boton + '</div> </div>'
            ptotal.innerHTML = 'Total: $' + total + ' ';
        }
        
        // for (let i = 0; i < cartSize; i++) {

        //     if (orders[i][4] === prod) {
        //         alert('Ya esta agregado')

        //         var orderprec = orders[i][2]
        //         var num = orderprec.slice(1)
        //         total = Number(total) - Number(num);
        //         a = orders[i]
        //         console.log(a.splice(3, 1, cantidad))
        //         cantidad++
        //         localStorage.setItem('total', total);
        //         orders[cartSize] = [nombre, imagen, precio, cantidad, prod]
        //         localStorage.setItem('orders', JSON.stringify(orders));

        //     } console.log('Me fui del if')
        // }console.log('Me fui del for')
    } else {
        console.log('Lo siento no eres el primero en el carrito asi que procedo a xD')
        var yaExiste = false;
        for (var i in orders) {
            if (orders[i].prod === prod) {
                yaExiste = true;
                console.log(orders[i][4]+ ' Ya está')
            }
        }
        if (yaExiste) {
            console.log('Lo siento hermano ya estoy guardado');
        } else {
            orders[cartSize] = {nombre, imagen, precio, cantidad, prod}
            localStorage.setItem('orders', JSON.stringify(orders));
            total = Number(total) + Number(newprecio);
            localStorage.setItem('total', total);
            var orders = JSON.parse(localStorage.getItem('orders'));
            var total = localStorage.getItem('total');
            var cartSize = orders.length
            pcart.innerHTML = '';
            for (let i = 0; i < cartSize; i++) {
                boton = '<button class="btn btn-danger buttonDelete" onclick="removercompra(' + i + ')" type="button">X</button>'
                pcart.innerHTML += '<div class="col-6 border-bottom">' +
                    '<div class="d-flex align-items-center pb-3 pt-3">' +
                    '<img src=' + orders[i].imagen + ' class="img-thumbnail" style="width: 35%">' +
                    '<p class="mb-0 ml-3" id ="' + orders[i].prod + '" >' + orders[i].nombre + '</p> </div></div>' +
                    '<div class="col-2">' +
                    '<div class=" d-flex align-items-center h-100 border-bottom pb-2 pt-3">' +
                    '<p class="item-price mb-0 ">' + orders[i].precio + '</p> </div> </div>' +
                    '<div class="col-4 d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">' +
                    '<input class="form-control" id="number' + orders[i].prod + '" onclick="aumentarcompra(\''+i+'\','+orders[i].cantidad+','+orders[i].prod +')" type="number" value="' + orders[i].cantidad + '">' + boton + '</div> </div>'
                ptotal.innerHTML = 'Total: $' + total + ' ';
            }
        }
        console.log(localStorage.getItem("orders"))
    }

    // orders[cartSize] = [nombre,imagen,precio,cantidad,prod];
    // localStorage.setItem('orders',JSON.stringify(orders));      
    // total = Number(total) + Number(newprecio) * cantidad;
    // localStorage.setItem('total',total);
    // prueba = orders[cartSize]

    // var cart = document.querySelector('#cart');
    // cart.innerHTML = orders.length;

    // boton = '<button class="btn btn-danger buttonDelete" onclick="removercompra('+cartSize +')" type="button">X</button>'
    // ptotal.innerHTML = 'Total:' + total + ' ';
    // pcart.innerHTML += '<div class="col-6 border-bottom">'+
    //                     '<div class="d-flex align-items-center pb-3 pt-3">'+
    //                     '<img src='+imagen +' class="img-thumbnail" style="width: 35%">'+
    //                     '<p class="mb-0 ml-3" id ="'+ prod +'" >'+nombre+'</p> </div></div>'+
    //                     '<div class="col-2">'+
    //                     '<div class=" d-flex align-items-center h-100 border-bottom pb-2 pt-3">'+
    //                     '<p class="item-price mb-0 ">'+precio +'</p> </div> </div> '+
    //                     '<div class="col-4 d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">'+
    //                     '<input class="form-control" id="number" type="number"value="'+cantidad+'">'+ boton + '</div> </div>'
    // ptotal.innerHTML = 'Total: $' + total + ' ';

}

//Mantiene el carrito actualizado
function pshoppinCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length
    pcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        boton = '<button class="btn btn-danger buttonDelete" onclick="removercompra(' + i + ')" type="button">X</button>'
        pcart.innerHTML += '<div class="col-6 border-bottom">' +
        '<div class="d-flex align-items-center pb-3 pt-3">' +
        '<img src=' + orders[i].imagen + ' class="img-thumbnail" style="width: 35%">' +
        '<p class="mb-0 ml-3" id ="' + orders[i].prod + '" >' + orders[i].nombre + '</p> </div></div>' +
        '<div class="col-2">' +
        '<div class=" d-flex align-items-center h-100 border-bottom pb-2 pt-3">' +
        '<p class="item-price mb-0 ">' + orders[i].precio + '</p> </div> </div>' +
        '<div class="col-4 d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">' +
        '<input class="form-control" id="number' + orders[i].prod + '" onclick="aumentarcompra(\''+i+'\','+orders[i].cantidad+','+orders[i].prod +')" type="number" value="' + orders[i].cantidad + '">' + boton + '</div> </div>'
        ptotal.innerHTML = 'Total: $' + total + ' ';
    }


}

pshoppinCart();

function removercompra(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var orderprec = orders[n].precio
    var num = orderprec.slice(1)
    total = Number(total) - Number(num);
    orders.splice(n, 1);
    //actualizar numero carrito
    cart.innerHTML = orders.length;
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    ptotal.innerHTML = 'Total: $' + total + ' ';
    pshoppinCart();
}
function aumentarcompra(arreglo,cantidad,idproducto) {
    console.log('Estoy dentro de aumentarcompra')
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total'); 
    var orderprec = orders[arreglo].precio
    var num = orderprec.slice(1)
    console.log(orderprec)
                        //actualizar numero carrito
    var cant = 'number' + idproducto;
    console.log(cant)
    var suma = document.getElementById(cant).value
                        // orders[i].splice(3, 1, suma)
    total = Number(num) * suma;
                        //console.log(ValorProducto)
    ptotal.innerHTML = 'Total: $' + total + ' ';
    orders[i].update({'cantidad':suma})
    localStorage.setItem('orders', JSON.stringify(orders));
        

    
}

