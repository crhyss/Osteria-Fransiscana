
var ptotal = document.querySelector('#ptotal')


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
        orders[cartSize] = [nombre, imagen, precio, cantidad, prod,precio]
        localStorage.setItem('orders', JSON.stringify(orders));
        total = Number(total) + Number(newprecio);
        localStorage.setItem('total', total);
        pshoppinCart();
    } else {
        console.log('Lo siento no eres el primero en el carrito asi que procedo a xD')
        var yaExiste = false;
        for (var i in orders) {
            if (orders[i][4] === prod) {
                yaExiste = true;
                console.log(orders[i][4]+ ' Ya está')
            }
        }
        if (yaExiste) {
            console.log('Lo siento hermano ya estoy guardado');
        } else {
            orders[cartSize] = [nombre, imagen, precio, cantidad, prod,precio]
            localStorage.setItem('orders', JSON.stringify(orders));
            total = Number(total) + Number(newprecio);
            localStorage.setItem('total', total);
            pshoppinCart();
        }
        console.log(localStorage.getItem("orders"))
    }
}


//Mantiene el carrito actualizado
function pshoppinCart() {
    var pcart = document.querySelector('#pcart')
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length
    pcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        boton = '<button class="btn btn-danger buttonDelete" onclick="removercompra(' + i + ')" type="button">X</button>'
        pcart.innerHTML += '<div class="col-6 border-bottom">' +
            '<div class="d-flex align-items-center pb-3 pt-3">' +
            '<img src=' + orders[i][1] + ' class="img-thumbnail" style="width: 35%">' +
            '<p class="mb-0 ml-3" id ="' + orders[i][4] + '" >' + orders[i][0] + '</p> </div></div>' +
            '<div class="col-2">' +
            '<div class=" d-flex align-items-center h-100 border-bottom pb-2 pt-3">' +
            '<p class="item-price mb-0 ">' + orders[i][2] + '</p> </div> </div>' +
            '<div class="col-4 d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">' +
            '<input class="form-control" min="1" id="number' + orders[i][4] + '" onclick="aumentarcompra(\''+i+'\','+orders[i][4]+')" type="number" value="' + orders[i][3] + '">' + boton + '</div> </div>'
        ptotal.innerHTML = 'Total: $' + total + ' ';
    }
}


pshoppinCart();


function removercompra(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var orderprec = orders[n][5]
    total = Number(total) - Number(orderprec);
    orders.splice(n, 1);
    //actualizar numero carrito
    cart.innerHTML = orders.length;
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    ptotal.innerHTML = 'Total: $' + total + ' ';
    pshoppinCart();
}

function aumentarcompra(arreglo,idproducto) {
    console.log('Estoy dentro de aumentarcompra')
    var orders = JSON.parse(localStorage.getItem('orders'));

    var orderprec = orders[arreglo][2]
    var num = orderprec.slice(1)
    console.log(orderprec)
    //obtengo la id cantidad
    var cant = 'number' + idproducto;
    var suma = document.getElementById(cant).value
    //obtengo la id precio2
    var total = localStorage.getItem('total');
    orders[arreglo].splice(3, 1, suma)

    total = Number(num) * suma;
    orders[arreglo].splice(5, 1, total)
    var sumador=0;
    for (var i = 0; i < orders.length; i++) {
      sumador = sumador+orders[i][5];
      
    }
    var retornado = sumador
    ptotal.innerHTML = 'Total: $' + retornado + ' ';
    localStorage.setItem('total', retornado);
    localStorage.setItem('orders', JSON.stringify(orders));  
}


