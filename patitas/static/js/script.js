$(document).ready(function() {
    $('#ingresar-btn').click(function(e) {
        e.preventDefault(); 

        var usuario = $('#usuario').val();
        var contrasena = $('#contrasena').val();

        // Validar campos
        if (usuario === '' || contrasena === '') {
            alert('No pueden haber campos vacios.');
            return;
        }
        $('#msj-modal').css('display', 'block');
    });

    $('.cerrar, #msj-modal').click(function() {
        $('#msj-modal').css('display', 'none');
    });

    $('.cont-modal').click(function(e) {
        e.stopPropagation(); 
    });
});

/*FORMULARIO CONTACTO*/
function validarFormulario(){
 
    $('.alert').remove();
    
    var nombre=$('#nombre').val(),
        correo=$('#correo').val(),
        asunto=$('#asunto').val(),
        mensaje=$('#mensaje').val();

    
    //validacion del nombre
    if(nombre=="" || nombre==null){
  
        cambiarColor("nombre");
        mostraAlerta("Ingrese un nombre");
        return false;

    }else{
        var expresion= /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(nombre)){
           
            cambiarColor("nombre");
            mostraAlerta("No se permiten carateres especiales o numeros");
            return false;
        }
    }
    // validacion del correo
    if(correo=="" || correo==null){
  
        cambiarColor("correo");
        mostraAlerta("Ingrese un correo electronico");
        return false;

    }else{
        var expresion= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if(!expresion.test(correo)){
            
            cambiarColor("correo");
            mostraAlerta("Por favor ingrese un correo válido");
            return false;
        }
    }
    // validacion del asunto
    if(asunto=="" || asunto==null){
  
        cambiarColor("asunto");
        mostraAlerta("Asunto vacío");
        return false;

    }else{
        var expresion= /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(asunto)){
            
            cambiarColor("asunto");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }
  
     // validar el mensaje
     if(mensaje=="" || mensaje==null){
  
        cambiarColor("mensaje");
        mostraAlerta("No puede quedar mensaje vacío");
        return false;
    }else{
        var expresion= /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(mensaje)){
           
            cambiarColor("mensaje");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }
  
    $('form').submit();
    return true; 
} 
  
  $('input').focus(function(){
    $('.alert').remove();
    colorDefault('nombre');
    colorDefault('correo');
    colorDefault('asunto');
  });
  
  $('textarea').focus(function(){
    $('.alert').remove();
    colorDefault('mensaje');
  });
  
  
  function colorDefault(dato){
    $('#' + dato).css({
        border: "1px solid #999"
    });
  }
  
  function cambiarColor(dato){
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });
  }
  
  function mostraAlerta(texto){
    $('#nombre').before('<div class="alert">Error: '+ texto +'</div>');
  }

/*Formulario REGISTRO */
$(document).ready(function() {
    $('#form-registro').submit(function(e) {
        e.preventDefault(); 

        var nombres = $('#nombres').val();
        var apellidos = $('#apellidos').val();
        var correo = $('#correo').val();
        var contrasena = $('#contrasena').val();
        var acuerdo = $('#confirm').prop('checked');

        // Validar campos
        if (nombres.trim() === '') {
            alert('Por favor, ingrese su nombre.');
            return;
        }

        if (apellidos.trim() === '') {
            alert('Por favor, ingrese su apellido.');
            return;
        }

        if (correo.trim() === '') {
            alert('Por favor, ingrese su correo electrónico.');
            return;
        }

        if (contrasena.trim() === '') {
            alert('Por favor, ingrese su contraseña.');
            return;
        }

        if (!acuerdo) {
            alert('Por favor, acepte los términos y condiciones.');
            return;
        }

        $('#msj-modal').css('display', 'block');
    });

    $('.cerrar, #msj-modal').click(function() {
        $('#msj-modal').css('display', 'none');
    });

    $('.cont-modal').click(function(e) {
        e.stopPropagation(); 
    });
});

