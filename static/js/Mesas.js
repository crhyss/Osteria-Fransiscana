$(document).ready(function(){  
    var locales = $("#LocalSelect");
    var mesas = $("#ListaMesas")
    var $mesa = mesas.find("div")

    locales.on('change', function(){
        if (this.value == 0) {
            $("#ListaMesas").load(window.location + " #ListaMesas*","");
        }
        else{
            mesas.html($mesa.filter('[id="'+ this.value + '"]'));
        }
    }).trigger('change');
});