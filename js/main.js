// main.js — Cart & Wishlist functionality using localStorage

// Utility functions
function getStorage(name) {
  return JSON.parse(localStorage.getItem(name)) || [];
}

function setStorage(name, data) {
  localStorage.setItem(name, JSON.stringify(data));
}

// Add item to cart
function addToCart(productId) {
  const cart = getStorage('cart');
  if (!cart.includes(productId)) {
    cart.push(productId);
    setStorage('cart', cart);
    alert('Item added to cart!');
    updateCartCount();
  } else {
    alert('Item already in cart');
  }
}

// Add item to wishlist
function addToWishlist(productId) {
  const wishlist = getStorage('wishlist');
  if (!wishlist.includes(productId)) {
    wishlist.push(productId);
    setStorage('wishlist', wishlist);
    alert('Item added to wishlist!');
  } else {
    alert('Item already in wishlist');
  }
}


let current = 0;
const slides = document.querySelectorAll('.slide');
const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    if (i === index) slide.classList.add('active');
  });
}

nextBtn.addEventListener('click', () => {
  current = (current + 1) % slides.length;
  showSlide(current);
});

prevBtn.addEventListener('click', () => {
  current = (current - 1 + slides.length) % slides.length;
  showSlide(current);
});

// Auto-play
setInterval(() => {
  current = (current + 1) % slides.length;
  showSlide(current);
}, 3000);



// Update cart count in navbar
function updateCartCount() {
  const cart = getStorage('cart');
  const cartLink = document.querySelector("a[href='cart.html']");
  if (cartLink) {
    cartLink.textContent = `🛒Cart(${cart.length})`;
  }
}

// On page load
document.addEventListener('DOMContentLoaded', () => {
  updateCartCount();
});


