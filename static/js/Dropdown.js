$(document).ready(function(){
    var region = $("#region");
    var comuna = $("#comuna");
    var $options = comuna.find('option');
    
    region.on('change', function(){
        comuna.html($options.filter('[id="'+ this.value + '"]'));
    }).trigger('change');
});