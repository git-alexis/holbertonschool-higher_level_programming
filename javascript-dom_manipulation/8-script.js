document.addEventListener('DOMContentLoaded', function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloElement = document.getElementById('hello');
      helloElement.innerHTML = data.hello;
    })
    .catch(error => console.error('Error:', error));
});
