function validarClave() {
    var letras_mayusculas = "ABCDEFGHYJKLMNÑOPQRSTUVWXYZ";
    var clave = document.getElementById("clave").value;
    var estado = true;
    var flag = 0;
    for (i = 0; i < clave.length; i++) {
        if (letras_mayusculas.indexOf(clave.charAt(i), 0) != -1) {
            var flag = 1;
        }
    }

    if (clave.length < 8) {
        alert("Debe tener almenos 8 caracteres.");
        estado = false;
    } else if (flag == 0) {
        alert("La clave debe tener mínimo un caracter en mayúscula.");
        document.getElementById("clave").focus();
        estado = false;
    }
}

function validarCorreo() {
    var correo = document.getElementById("correo").value; // String
    var estado = true;
    if (correo == "") {
        alert("Escriba un correo");
        estado = false;
    } else if (correo.indexOf("@") == 0 || correo.indexOf("@") == correo.length - 1) {
        alert("Correo incorrecto.");
        estado = false;
    }
    return estado;
}

function validarInfo() {
    return validarCorreo() && validarClave();
}

function mostrarPassword() {
    document.getElementById("clave").type = "text";
}

function ocultarPassword() {
    document.getElementById("clave").type = "password";
}