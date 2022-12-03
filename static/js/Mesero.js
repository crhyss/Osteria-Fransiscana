$(document).ready(function(){   
    var cat = $("#categoria");
    var prod = $("#producto");
    var $options = prod.find('option');
    csrf_token = "{{ csrf_token }}";

    cat.on('change', function(){
        prod.html($options.filter('[id="'+ this.value + '"]'));
    }).trigger('change');

    $('#add_ped').on('click', function(event){
        let data = $('#agre_pedid').serialize();
        event.preventDefault();
        alert(window.location)
        $.ajax({
            type:"POST",
            url: "/web/vista_mesero/",
            data: data,
            processData: false,
            success: function () {
                $("#lista_pedidos").load(window.location + " #lista_pedidos*","");
            }
        });
        return false
    });
});
