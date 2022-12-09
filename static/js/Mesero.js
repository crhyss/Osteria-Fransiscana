$(document).ready(function(){   
    var cat = $("#categoria");
    var prod = $("#producto");
    var $options = prod.find('option');

    cat.on('change', function(){
        prod.html($options.filter('[id="'+ this.value + '"]'));
    }).trigger('change');

    $('#add_ped').on('click', function(event){
        let data = $('#agre_pedid').serialize();
        event.preventDefault();
        $.ajax({
            type:"POST",
            url: "/web/vista_mesero/",
            data: data,
            processData: false,
            success: function () {
                $("#lista_pedidos").load(window.location + " #lista_pedidos*","");
                $("#ModalData").load(window.location + " #ModalData*","");
            }
        });
    });
});

function pagar_pedido(){
    let data = $('#enviar_pago').serialize();
    $.ajax({
        type:"POST",
        url: "/web/terminar_venta/",
        data: data,
        success: function(){
            window.location = "/web/vista_mesas/"
        }
    })
}

function pedido_entregado(pedido_id) {
    let id_procesada = '#' + pedido_id;
    var form = $(id_procesada).serialize()
    event.preventDefault();
    
    $.ajax({
        type:"POST",
        url: "/web/mesero/entregar_ped",
        data: form,
        processData: false,
        success: function () {
            $("#lista_pedidos").load(window.location + " #lista_pedidos*","");
        }
    });       
}

function calcular_total(){
    let total_vta = $("#totalVenta").text()
    let total = $("#total")
    let propina = $("#propina")
    total_vta = total_vta.split(" ")[2]
    console.log(propina)
    total.text("Total: " + (parseInt(propina.val()) + parseInt(total_vta)))
}