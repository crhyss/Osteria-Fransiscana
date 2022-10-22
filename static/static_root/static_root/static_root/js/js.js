const forms = document.querySelectorAll('.needs-validation')
Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
        }
        if (form.checkValidity()) {
            const datos = new FormData(event.target);
            const datosCompletos = Object.fromEntries(datos.entries());
            console.log(JSON.stringify(datosCompletos));
        }
        form.classList.add('was-validated')
    }, false)

})