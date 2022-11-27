// const addToShoppingCartButtons = document.querySelectorAll('.addToCart');
// addToShoppingCartButtons.forEach((addToCartButton) => {
//     addToCartButton.addEventListener('click', addToCartClicked);
// });

// const comprarButton = document.querySelector('.comprarButton');
// comprarButton.addEventListener('click', comprarButtonClicked);

// const shoppingCartItemsContainer = document.querySelector(
//     '.shoppingCartItemsContainer'
// );

// function addToCartClicked(event) {
//     const button = event.target;
//     const item = button.closest('.item');

//     const itemTitle = item.querySelector('.item-title').textContent;
//     const itemPrice = item.querySelector('.item-price').textContent;
//     const itemImage = item.querySelector('.item-image').src;

//     addItemToShoppingCart(itemTitle, itemPrice, itemImage);
// }

// function addItemToShoppingCart(itemTitle, itemPrice, itemImage) {
//     const elementsTitle = shoppingCartItemsContainer.getElementsByClassName(
//         'shoppingCartItemTitle'
//     );
//     for (let i = 0; i < elementsTitle.length; i++) {
//         if (elementsTitle[i].innerText === itemTitle) {
//             let elementQuantity = elementsTitle[
//                 i
//             ].parentElement.parentElement.parentElement.querySelector(
//                 '.shoppingCartItemQuantity'
//             );
//             elementQuantity.value++;
//             $('.toast').toast('show');
//             updateShoppingCartTotal();
//             return;
//         }
//     }

//     const shoppingCartRow = document.createElement('div');
//     const shoppingCartContent = `
//   <div class="row shoppingCartItem">
//         <div class="col-6">
//             <div class="shopping-cart-item d-flex align-items-center h-100 border-bottom pb-2 pt-3">
//                 <img src=${itemImage} class="shopping-cart-image">
//                 <h6 class="shopping-cart-item-title shoppingCartItemTitle text-truncate ml-3 mb-0">${itemTitle}</h6>
//             </div>
//         </div>
//         <div class="col-2">
//             <div class="shopping-cart-price d-flex align-items-center h-100 border-bottom pb-2 pt-3">
//                 <p class="item-price mb-0 shoppingCartItemPrice">${itemPrice}</p>
//             </div>
//         </div>
//         <div class="col-4">
//             <div
//                 class="shopping-cart-quantity d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">
//                 <input class="shopping-cart-quantity-input shoppingCartItemQuantity" type="number"
//                     value="1">
//                 <button class="btn btn-danger buttonDelete" type="button">X</button>
//             </div>
//         </div>
//     </div>`;
//     shoppingCartRow.innerHTML = shoppingCartContent;
//     shoppingCartItemsContainer.append(shoppingCartRow);

//     shoppingCartRow
//         .querySelector('.buttonDelete')
//         .addEventListener('click', removeShoppingCartItem);

//     shoppingCartRow
//         .querySelector('.shoppingCartItemQuantity')
//         .addEventListener('change', quantityChanged);

//     updateShoppingCartTotal();
// }

// function updateShoppingCartTotal() {
//     let total = 0;
//     const shoppingCartTotal = document.querySelector('.shoppingCartTotal');

//     const shoppingCartItems = document.querySelectorAll('.shoppingCartItem');

//     shoppingCartItems.forEach((shoppingCartItem) => {
//         const shoppingCartItemPriceElement = shoppingCartItem.querySelector(
//             '.shoppingCartItemPrice'
//         );
//         const shoppingCartItemPrice = Number(
//             shoppingCartItemPriceElement.textContent.replace('$', '')
//         );
//         const shoppingCartItemQuantityElement = shoppingCartItem.querySelector(
//             '.shoppingCartItemQuantity'
//         );
//         const shoppingCartItemQuantity = Number(
//             shoppingCartItemQuantityElement.value
//         );
//         total = total + shoppingCartItemPrice * shoppingCartItemQuantity;
//     });
//     shoppingCartTotal.innerHTML = `$${total}`;
// }

// function removeShoppingCartItem(event) {
//     const buttonClicked = event.target;
//     buttonClicked.closest('.shoppingCartItem').remove();
//     updateShoppingCartTotal();
// }

// function quantityChanged(event) {
//     const input = event.target;
//     input.value <= 0 ? (input.value = 1) : null;
//     updateShoppingCartTotal();
// }

// function comprarButtonClicked() {
//     shoppingCartItemsContainer.innerHTML = '';
//     updateShoppingCartTotal();
// }
// class Pushbar {
//     constructor(config = { overlay: true, blur: false }) {
//         this.activeId;
//         this.activeElement;
//         this.overlayElement;
//         if (config.overlay) {
//             this.overlayElement = document.createElement('div');
//             this.overlayElement.classList.add('pushbar_overlay');
//             document.querySelector('body').appendChild(this.overlayElement);
//         }
//         if (config.blur) {
//             const mainContent = document.querySelector('.pushbar_main_content');
//             if (mainContent) {
//                 mainContent.classList.add('pushbar_blur');
//             }
//         }
//         this.bindEvents();
//     }

//     emitOpening() {
//         const event = new CustomEvent('pushbar_opening', { bubbles: true, detail: { element: this.activeElement, id: this.activeId } });
//         this.activeElement.dispatchEvent(event);
//     }

//     emitClosing() {
//         const event = new CustomEvent('pushbar_closing', { bubbles: true, detail: { element: this.activeElement, id: this.activeId } });
//         this.activeElement.dispatchEvent(event);
//     }

//     handleOpenEvent(e) {
//         e.preventDefault();
//         const pushbarId = e.currentTarget.getAttribute('data-pushbar-target');
//         this.open(pushbarId);
//     }

//     handleCloseEvent(e) {
//         e.preventDefault();
//         this.close();
//     }

//     handleKeyEvent(e) {
//         if (e.keyCode === 27) this.close();
//     }

//     bindEvents() {
//         const triggers = document.querySelectorAll('[data-pushbar-target]');
//         const closers = document.querySelectorAll('[data-pushbar-close]');
//         triggers.forEach(trigger => trigger.addEventListener('click', e => this.handleOpenEvent(e), false));
//         closers.forEach(closer => closer.addEventListener('click', e => this.handleCloseEvent(e), false));
//         if (this.overlayElement) {
//             this.overlayElement.addEventListener('click', e => this.handleCloseEvent(e), false);
//         }
//         document.addEventListener('keyup', e => this.handleKeyEvent(e));
//     }

//     open(pushbarId) {
//         if (this.activeId === String(pushbarId) || !pushbarId) return;
//         if (this.activeId && this.activeId !== String(pushbarId)) this.close();
//         this.activeId = pushbarId
//         this.activeElement = document.querySelector(`[data-pushbar-id="${this.activeId}"]`)
//         if (!this.activeElement) return;
//         this.emitOpening();
//         this.activeElement.classList.add('opened');
//         const pageRootElement = document.querySelector('html')
//         pageRootElement.classList.add('pushbar_locked');
//         pageRootElement.setAttribute('pushbar', pushbarId)
//     }

//     close() {
//         if (!this.activeId) return;
//         this.emitClosing();
//         this.activeElement.classList.remove('opened');
//         const pageRootElement = document.querySelector('html')
//         pageRootElement.classList.remove('pushbar_locked');
//         pageRootElement.removeAttribute('pushbar')
//         this.activeId = null;
//         this.activeElement = null;
//     }
// }

var hours = 24;
var now = new Date().getTime();
var stepTime = localStorage.getItem('stepTime')
if (stepTime == null) {
    localStorage.setItem('stepTime',now);
} else {
    if (now - stepTime > hours*60*60*1000) {
        localStorage.clear();
        localStorage.setItem('stepTime',now)
        
    }
}

var orders = JSON.parse(localStorage.getItem('orders'));
var total = localStorage.getItem('total');
if (orders === null || orders === undefined) {
    localStorage.setItem('orders',JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'))
}

if (total === null || total === undefined) {
    localStorage.setItem('total',0);
    total = localStorage.getItem('total');
}
var cart = document.querySelector('#cart');
cart.innerHTML = orders.length;