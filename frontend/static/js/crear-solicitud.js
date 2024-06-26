let addButtons = document.querySelectorAll('.add-button');
let solicitud = [];
addButtons.forEach(btn => {
  btn.addEventListener('click',function(){
    let row = this.closest('tr');
    let id = row.querySelector(".item-id").textContent;
    let name = row.querySelector(".item-name").innerHTML;
    let rawPrice = row.querySelector('.item-price').textContent;
    let price =parseInt(rawPrice.replace(/\D/g, ''));
    addToSolicitud(id,name,price)
  });
});

function addToSolicitud(id, name, price){
  /*
    <tr>
              <td>#</td>
              <td>Juguete</td>
              <td>20</td>
              <td>$30.000</td>
              <td><button class='btn btn-danger'><i class="bi bi-trash-fill"></i></button></td>
            </tr>
  */
  let table = document.getElementById('tblBodySolicitud')
  let objeto = solicitud.find(obj => obj.id === id);
  if (!objeto){
    solicitud.push({id:id,name:name,price:price,amount:1})
  }
  if (objeto){
    objeto.amount += 1;
  }
}

function loadTable(){
  
}