function cargarImagen() {
    var inputFile = document.getElementById('cargarArchivo').files[0].name;
    var imagen = document.createElement('img');
    alert(inputFile);
    imagen.src = "../static/images/".concat(inputFile);
    imagen.setAttribute('width', 250);
    imagen.setAttribute('heigt', 250);
    imagen.setAttribute('align', "center");
    document.getElementById("divImagen").appendChild(imagen);
}

function galeria() {
    var dirImagenes = ["buscar.jpeg", "cargar.jpeg", "clave.jpg"];
    for (var i = 0; i < dirImagenes.length; i++) {
        var imagen = document.createElement('img');
        imagen.setAttribute('width', 200);
        imagen.setAttribute('heigt', 200);
        imagen.src = "../static/images/".concat(dirImagenes[i]);
        document.getElementById("divGaleria").appendChild(imagen);
    }
}