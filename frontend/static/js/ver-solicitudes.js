function eliminarSolicitud(api_key, id) {
  fetch(`http://localhost:8000/api/solicitudes/${id}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      api_key: api_key
    }),
  })
    .then(response => response.json())
    .then(data => {
      if (data.message){
        alert(data.message)
        location.reload()
      }
      if (data.error){
        alert(data.error)
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}