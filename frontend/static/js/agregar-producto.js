const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
document.getElementById("addItemForm").addEventListener("submit", function (event) {
  event.preventDefault()
  // Realizar comprobaciones antes de enviar el formulario
  let nombre = document.getElementById("nombre").value;
  let precio = document.getElementById("precio").value;
  let stock = document.getElementById("stock").value;
  let descripcion = document.getElementById("descripcion").value;
  let categoria = document.getElementById("categoria").value;

  if (nombre.trim() === '' || precio.trim() === '' || stock.trim() === '' || descripcion.trim() === '') {
    alert("Por favor, complete todos los campos");
    return;
  }
  if (isNaN(parseFloat(precio)) || parseFloat(precio) <= 0) {
    alert("El precio debe ser un número mayor que cero.");
    return;
  }
  if (isNaN(parseInt(stock)) || parseInt(stock) <= 0) {
    alert("El stock debe ser un número entero mayor que cero.");
    return;
  }
  if (categoria==0){
    alert("Se debe seleccionar una categoria");
    return;
  }

  const data = {
    nombre: nombre,
    precio: precio,
    stock: stock,
    descripcion: descripcion,
    categoria: categoria
  };

  fetch('/api/create-item/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken, // Asegúrate de obtener el token CSRF
    },
    body: JSON.stringify(data)
  })
    .then(response => {
      if (response.ok) {
        console.log('Item creado correctamente');
      } else {
        console.error('Error al crear el item');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
    this.submit();
});

document.getElementById("addCategoryForm").addEventListener("submit", function (event) {
  event.preventDefault()
  let nombre = document.getElementById("nombreCategoria").value;
  console.log('hola ', nombre);
  const data = {
    nombre: nombre
  }
  fetch('/api/create-category/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken, // Asegúrate de obtener el token CSRF
    },
    body: JSON.stringify(data)
  })
    .then(response => {
      if (response.ok) {
        console.log('Categoria creado correctamente');
        window.location.reload();
      } else {
        console.error('Error al crear el item');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
});