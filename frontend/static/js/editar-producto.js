//contenteditable='true'
document.addEventListener('DOMContentLoaded', function () {
  let editButtons = document.querySelectorAll('.btn-primary');
  editButtons.forEach(button => {
    button.addEventListener('click', function () {
      let row = button.closest('tr');
      let tds = row.querySelectorAll('td:not(.item-id,.buttons-col,.user-username)');
      let data = []
      tds.forEach(td => {
        if (td.getAttribute('contenteditable') === 'true') {
          td.removeAttribute('contenteditable');
          data.push(td.textContent);
        } else {
          td.setAttribute('contenteditable', 'true');
        }
      });
      
      if (data.length > 0) {
        let priceTD = row.querySelector('.item-price');
        let itemPrice =parseInt(priceTD.textContent.replace(/\D/g, ''));
        let new_price = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD',minimumFractionDigits: 0, maximumFractionDigits: 0}).format(itemPrice);
        let stockTD = row.querySelector('.item-stock');
        let new_stock = stockTD.textContent.replace(/\D/g, '')
        stockTD.textContent = new_stock;
        priceTD.textContent = new_price; 
        let itemId = row.querySelector('.item-id').textContent;
        let userKey = row.querySelector('.user-key').textContent;
        let edit_request = {name: data[0],price: itemPrice,stock: new_stock,description: data[3],category:data [4],user_key:userKey};
        editItem(edit_request,itemId);
      }
    });
  });
});


function editItem(data,id){
  let url = `http://localhost:8000/api/items/${id}/`;

  fetch(url, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams(data)
  })
    .then(response => {
      if (response.status === 200) {
        alert("Item editado exitosamente.");
      } else if (response.status === 400) {
        alert("No se encuentra llave de API");
      } else if (response.status === 403) {
        alert("Llave invalida");
      } else {
        alert(`Error al crear el producto. Código de estado: ${response.status}`);
      }
    })
    .catch(error => {
      alert("Error al realizar la solicitud:", error);
    });
}
