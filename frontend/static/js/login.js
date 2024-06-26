document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var form = this;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var isValid = true;

    if (!username) {
        document.getElementById('username').classList.add('is-invalid');
        isValid = false;
    } else {
        document.getElementById('username').classList.remove('is-invalid');
    }

    if (!password) {
        document.getElementById('password').classList.add('is-invalid');
        isValid = false;
    } else {
        document.getElementById('password').classList.remove('is-invalid');
    }

    if (isValid) {
        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
  });
});
