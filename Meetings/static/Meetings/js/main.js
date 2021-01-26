$(function(){
    $("[data-toggle='tooltip']").tooltip();
    $('.carouselHNAS').carousel({
        interval: 2200
    });
    /* Trabajamos con los ID de los li del menu superior */
    let identificadores = ['#conteoIngreso', '#conteoContacto', '#conteoRegistro'];
    identificadores.forEach(function(id){
        $(id).on('click', function(e){
            console.log('Se ha ingresado a modal ' + id)
        });
    });
    let identificadores2 = ['#modalContacto', '#modalIngreso'];
    identificadores2.forEach(function(id2){
        $(id2).on('click', function(e){
            console.log('Se ha emitido la peticion de ' + id2)
        })
    })
    const menuSup = document.querySelector('.menuSup');
    menuSup.style.setProperty('--animate-duration', '2s');

    const tituloPrincipal = document.querySelector('.titulo');
    tituloPrincipal.style.setProperty('--animate-duration', '1s');
  });

