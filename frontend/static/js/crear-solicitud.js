let saveButton = document.getElementById('saveSolicitud');
let addButtons = document.querySelectorAll('.add-button');
let solicitud = [];
addButtons.forEach(btn => {
  btn.addEventListener('click',function(){
    let row = this.closest('tr');
    let id = row.querySelector(".item-id").textContent;
    let name = row.querySelector(".item-name").innerHTML;
    let stock = row.querySelector(".item-stock").innerHTML;
    let rawPrice = row.querySelector('.item-price').textContent;
    let price =parseInt(rawPrice.replace(/\D/g, ''));
    addToSolicitud(id,name,price,stock)
  });
});

saveButton.addEventListener('click',function(){
  saveSolicitud()
})

function addToSolicitud(id, name, price,stock){
  /*
    <tr>
              <td>#</td>
              <td>Juguete</td>
              <td>20</td>
              <td>$30.000</td>
              <td><button class='btn btn-danger'><i class="bi bi-trash-fill"></i></button></td>
            </tr>
  */
  let objeto = solicitud.find(obj => obj.id === id);
  if (!objeto){
    solicitud.push({id:id,name:name,price:price,amount:1})
  }
  if (objeto && objeto.amount<=stock){
    objeto.amount += 1;
  }
  loadTable()
}

function loadTable(){
  let table = document.getElementById('tblBodySolicitud')
  table.innerHTML="";
  solicitud.forEach(item => {
    table.innerHTML += `
      <tr>
        <td>${item.id}</td>
        <td>${item.name}</td>
        <td>${item.amount}</td>
        <td>${item.price}</td>
        <td><button class="btn btn-danger" onclick="deleteFromSolicitud(${item.id})"><i class="bi bi-trash-fill"></i></button></td>
      </tr>
    `
  });
}

function deleteFromSolicitud(id){
  solicitud = solicitud.filter(item=>item.id != id);
  loadTable();
}
function saveSolicitud(){
  let data = [{'solicitud':solicitud},{'api_key':apiKey}]
  fetch('http://localhost:8000/api/solicitudes/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    if (data.error){
      alert(data.error)
    }
    if (data.message){
      alert(data.message)
      location.reload();
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}
