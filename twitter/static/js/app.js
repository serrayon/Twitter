console.log('kjkksljfkljflkjd');

// SECTION subscribe event listeners
var modalBtn = document.querySelector('.modal-btn');
var modalBg = document.querySelector('.modal-bg');
let modalClose = document.querySelector('.modal-close');

modalBtn.addEventListener('click', function () {
  modalBg.classList.add('bg-active');
});
modalClose.addEventListener('click', function () {
  modalBg.classList.remove('bg-active');
});