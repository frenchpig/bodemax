function deleteItem(api_key, id) {
  let url = `http://localhost:8000/api/items/${id}/?user_key=${api_key}`;

const requestOptions = {
  method: 'DELETE',
  headers: {
    'Content-Type': 'application/json'
  }
};
  // Realizar la solicitud DELETE
  fetch(url, requestOptions)
    .then(response => {
      // Verificar el código de estado de la respuesta
      if (response.status === 204) {
        console.log("Producto eliminado exitosamente.");
        location.reload();
      } else if (response.status === 403) {
        console.log("No tienes permisos para eliminar este producto.");
      } else if (response.status === 404) {
        console.log("El producto no existe.");
      } else {
        console.log(`Error al eliminar el producto. Código de estado: ${response.status}`);
      }
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded',function(){
  let deleteButtons = document.querySelectorAll('.btn-danger');
  deleteButtons.forEach(button=>{
    button.addEventListener('click',function(){
      let row = button.closest('tr');
      let itemId = row.querySelector('.item-id').textContent;
      let userKey = row.querySelector('.user-key').textContent;
      deleteItem(userKey,itemId)
    });
  });
});