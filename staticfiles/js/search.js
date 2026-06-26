// Dynamic product search from Django database
const SearchManager = {
    async search(query) {
        if (!query.trim()) return [];
        try {
            const response = await fetch(`/api/buscar/?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            return data.productos || [];
        } catch (error) {
            console.error('Error buscando productos:', error);
            return [];
        }
    },

    async showResults(query) {
        const container = document.getElementById('search-results-container');
        if (!container) return;

        if (!query.trim()) {
            container.classList.add('d-none');
            return;
        }

        const results = await this.search(query);
        container.classList.remove('d-none');

        if (results.length === 0) {
            container.innerHTML = '<div class="p-3 text-muted text-center">No se encontraron productos</div>';
            return;
        }

        container.innerHTML = results.map(p => `
            <a href="${p.url}" class="search-result-item">
                <div class="flex-grow-1">
                    <div class="fw-bold">${p.nombre}</div>
                    <small class="text-muted">Stock: ${p.stock}</small>
                </div>
                <div class="text-primary fw-bold ms-3">$${Number(p.precio).toLocaleString('es-CL')}</div>
            </a>
        `).join('');
    }
};

let searchTimeout = null;
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('main-search-input');
    const resultsContainer = document.getElementById('search-results-container');

    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                SearchManager.showResults(e.target.value);
            }, 250);
        });

        document.addEventListener('click', (e) => {
            if (resultsContainer && !searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
                resultsContainer.classList.add('d-none');
            }
        });

        searchInput.addEventListener('focus', (e) => {
            if (e.target.value.trim()) {
                SearchManager.showResults(e.target.value);
            }
        });
    }
});
