// Shopping cart management using localStorage
// Handles adding, removing, updating quantities and rendering

const MAX_UNITS_PER_PRODUCT = 10;

const CartManager = {
    getCart() {
        return JSON.parse(localStorage.getItem('cart')) || [];
    },

    saveCart(cartItems) {
        localStorage.setItem('cart', JSON.stringify(cartItems));
    },

    addItem(id, name, price, image, stock = MAX_UNITS_PER_PRODUCT) {
        const cart = this.getCart();
        const existingItem = cart.find(item => item.id === id);
        const availableStock = Number(stock) || 0;
        const maxAllowed = Math.min(MAX_UNITS_PER_PRODUCT, availableStock);

        if (maxAllowed <= 0) {
            alert(`El producto ${name} no tiene stock disponible.`);
            return;
        }

        if (existingItem) {
            existingItem.stock = availableStock;
            if (existingItem.quantity >= maxAllowed) {
                this.showLimitMessage(name, maxAllowed);
                this.showCart();
                return;
            }
            existingItem.quantity += 1;
        } else {
            cart.push({ id, name, price, image, quantity: 1, stock: availableStock });
        }

        this.saveCart(cart);
        this.updateBadge();
        this.renderCart();
        this.showCart();
    },

    removeItem(id) {
        let cart = this.getCart();
        cart = cart.filter(item => item.id !== id);
        this.saveCart(cart);
        this.refresh();
    },

    updateQuantity(id, newQuantity) {
        let cart = this.getCart();
        const item = cart.find(item => item.id === id);

        if (!item) return;

        const maxAllowed = Math.min(MAX_UNITS_PER_PRODUCT, Number(item.stock) || MAX_UNITS_PER_PRODUCT);

        if (newQuantity > maxAllowed) {
            this.showLimitMessage(item.name, maxAllowed);
            return;
        }

        if (newQuantity > 0) {
            item.quantity = newQuantity;
        } else {
            cart = cart.filter(item => item.id !== id);
        }

        this.saveCart(cart);
        this.refresh();
    },

    updateBadge() {
        const badges = document.querySelectorAll('.cart-badge');
        const cart = this.getCart();
        const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
        badges.forEach(badge => badge.innerText = totalItems);
    },

    renderCart() {
        const container = document.getElementById('cart-items-container');
        const totalElement = document.getElementById('cart-total');

        if (!container) return;

        const cart = this.getCart();
        container.innerHTML = '';
        let total = 0;

        if (cart.length === 0) {
            container.innerHTML = `
                <div class="text-center py-5 text-muted">
                    <i class="bi bi-cart-x fs-1"></i>
                    <p class="mt-2">Tu carrito está vacío</p>
                </div>
            `;
            if (totalElement) totalElement.innerText = '0';
            return;
        }

        cart.forEach((item) => {
            const subtotal = item.price * item.quantity;
            total += subtotal;

            container.innerHTML += `
                <div class="d-flex align-items-center mb-3 pb-3 border-bottom">
                    <img src="${item.image}" class="rounded me-3" style="width:50px;height:50px;object-fit:cover;" alt="${item.name}">
                    <div class="flex-grow-1">
                        <h6 class="mb-0 small fw-bold">${item.name}</h6>
                        <div class="d-flex align-items-center mt-1">
                            <button class="btn btn-sm btn-light border px-2 py-0" onclick="CartManager.updateQuantity('${item.id}', ${item.quantity - 1})">-</button>
                            <span class="mx-2 small">${item.quantity}</span>
                            <button class="btn btn-sm btn-light border px-2 py-0" onclick="CartManager.updateQuantity('${item.id}', ${item.quantity + 1})" ${item.quantity >= Math.min(MAX_UNITS_PER_PRODUCT, Number(item.stock) || MAX_UNITS_PER_PRODUCT) ? 'disabled' : ''}>+</button>
                        </div>
                        <small class="text-muted">Stock: ${item.stock ?? 'N/D'} | Máximo ${Math.min(MAX_UNITS_PER_PRODUCT, Number(item.stock) || MAX_UNITS_PER_PRODUCT)} unidades</small>
                    </div>
                    <div class="text-end">
                        <span class="fw-bold small d-block">$${subtotal.toLocaleString('es-CL')}</span>
                        <button class="btn btn-sm text-danger p-0" onclick="CartManager.removeItem('${item.id}')">
                            <i class="bi bi-trash"></i>
                        </button>
                    </div>
                </div>
            `;
        });

        if (totalElement) {
            totalElement.innerText = total.toLocaleString('es-CL');
        }
    },

    renderCheckout() {
        const cart = this.getCart();
        const container = document.getElementById('checkout-items');
        const totalElement = document.getElementById('checkout-total');
        const shippingElement = document.getElementById('shipping-price');

        if (!container || !totalElement) return;

        container.innerHTML = '';

        if (cart.length === 0) {
            container.innerHTML = `
                <div class="text-center text-muted py-5">
                    <i class="bi bi-cart-x fs-1"></i>
                    <p class="mt-3">Tu carrito está vacío</p>
                </div>
            `;
            totalElement.innerText = '0';
            return;
        }

        let total = 0;
        cart.forEach(item => {
            const subtotal = item.price * item.quantity;
            total += subtotal;

            container.innerHTML += `
                <div class="d-flex align-items-center mb-3 pb-3 border-bottom">
                    <img src="${item.image}" width="70" height="70" class="rounded me-3" style="object-fit:cover;" alt="${item.name}">
                    <div class="flex-grow-1">
                        <h6 class="fw-bold mb-1">${item.name}</h6>
                        <small class="text-muted">Cantidad: ${item.quantity} | Stock: ${item.stock ?? 'N/D'}</small>
                    </div>
                    <div class="fw-bold text-primary">
                        $${subtotal.toLocaleString('es-CL')}
                    </div>
                </div>
            `;
        });

        const delivery = document.querySelector('input[name="delivery"]:checked')?.value;
        const shippingCost = delivery === "delivery" ? 10990 : 0;

        if (shippingElement) {
            shippingElement.innerText = shippingCost === 0 ? "Gratis" : "$" + shippingCost.toLocaleString('es-CL');
        }

        total += shippingCost;
        totalElement.innerText = total.toLocaleString('es-CL');
    },

    refresh() {
        this.updateBadge();
        this.renderCart();
        this.renderCheckout();
    },

    showCart() {
        const offcanvasElement = document.getElementById('offcanvasCart');
        if (offcanvasElement) {
            const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasElement) || new bootstrap.Offcanvas(offcanvasElement);
            bsOffcanvas.show();
        }
    },

    showLimitMessage(productName, maxAllowed = MAX_UNITS_PER_PRODUCT) {
        alert(`No puedes agregar más de ${maxAllowed} unidades de ${productName}.`);
    },

    clearCart() {
        localStorage.removeItem('cart');
        this.refresh();
    },

    confirmPurchase() {
        const cart = this.getCart();

        if (cart.length === 0) {
            alert('No puedes confirmar una compra con el carrito vacío.');
            return;
        }

        alert('Compra completada con éxito');
        this.clearCart();
        window.location.href = '/inicio/';
    },

    togglePaymentFields() {
        const method = document.querySelector('input[name="payment"]:checked')?.value;
        const cardFields = document.getElementById('card-fields');
        if (!cardFields) return;
        cardFields.style.display = method === "paypal" ? "none" : "block";
    },

    toggleDeliveryFields() {
        const method = document.querySelector('input[name="delivery"]:checked')?.value;
        const address = document.getElementById('address-field');
        if (!address) return;
        address.style.display = method === "pickup" ? "none" : "block";
        this.renderCheckout();
    }
};

// Global function for adding to cart from HTML
window.addToCart = function (id, name, price, image, stock = MAX_UNITS_PER_PRODUCT) {
    CartManager.addItem(id, name, price, image, stock);
};

// Initialize cart on page load
document.addEventListener('DOMContentLoaded', () => {
    CartManager.updateBadge();
    CartManager.renderCart();
    CartManager.renderCheckout();
    CartManager.togglePaymentFields();
    CartManager.toggleDeliveryFields();
});
