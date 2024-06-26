let dataMapping;
let inputId;
if (isAdmin){
  dataMapping = { 'nombre': 'name', 'categoria': 'category', 'precio': 'price', 'stock': 'stock', 'descripcion': 'description', 'user': 'user_key' };
  inputId = ['nombre', 'categoria', 'precio', 'stock', 'descripcion', 'user']
}else {
  dataMapping = { 'nombre': 'name', 'categoria': 'category', 'precio': 'price', 'stock': 'stock', 'descripcion': 'description', 'user': 'user_key' };
  inputId = ['nombre', 'categoria', 'precio', 'stock', 'descripcion']
}
let addItemButton = document.getElementById('addItemButton');


addItemButton.addEventListener('click', function () {
  let data = { 'name': null, 'price': null, 'stock': null, 'description': null, 'category': null, 'user_key': null }
  inputId.forEach(element => {
    let input = document.getElementById(element);
    let value = input.value;
    data[dataMapping[element]] = value;
  });
  if (!isAdmin){
    data['user_key']=apiKey;
  }
  addToDataBase(data);
  clearAddInputs();
});

function addToDataBase(data) {
  let url = 'http://localhost:8000/api/items/';

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams(data)
  })
    .then(response => {
      if (response.status === 201) {
        alert("Producto creado exitosamente.");
      } else if (response.status === 400) {
        alert("Error en los datos de entrada.");
      } else if (response.status === 403) {
        alert("No tienes permisos para realizar esta acción.");
      } else {
        alert(`Error al crear el producto. Código de estado: ${response.status}`);
      }
    })
    .catch(error => {
      alert("Error al realizar la solicitud:", error);
    });
}

function clearAddInputs(){
  inputId.forEach(element=>{
    let input = document.getElementById(element);
    if (input.tagName==='SELECT'){
      input.selectedIndex = 0;
    }else{
      input.value = '';
    }
  });
}