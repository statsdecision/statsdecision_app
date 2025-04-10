document.getElementById('mobileMenuButton').addEventListener('click', function() {
    document.getElementById('mobileMenu').classList.toggle('hidden');
});

// Fermer le menu mobile quand on clique sur un lien
document.querySelectorAll('#mobileMenu a').forEach(link => {
    link.addEventListener('click', function() {
        document.getElementById('mobileMenu').classList.add('hidden');
    });
});

// Recherche globale
document.getElementById('globalSearchInput')?.addEventListener('keyup', function(e) {
    if (e.key === 'Enter') {
        const searchTerm = this.value.trim();
        if (searchTerm) {
            // Implémentez votre logique de recherche ici
            console.log('Recherche pour:', searchTerm);
        }
    }
});

document.getElementById('mobileSearchInput')?.addEventListener('keyup', function(e) {
    if (e.key === 'Enter') {
        const searchTerm = this.value.trim();
        if (searchTerm) {
            // Implémentez votre logique de recherche ici
            console.log('Recherche mobile pour:', searchTerm);
        }
    }
});

// Gestion du widget WhatsApp
const widget = document.getElementById('whatsapp-widget');
const trigger = document.getElementById('whatsapp-trigger');
const closeBtn = document.getElementById('close-whatsapp');

// Afficher après 8 secondes
setTimeout(() => {
    widget.classList.remove('translate-y-4', 'opacity-0');
    widget.classList.add('translate-y-0', 'opacity-100');
}, 8000);

// Toggle au clic
trigger.addEventListener('click', () => {
    widget.classList.toggle('translate-y-4');
    widget.classList.toggle('opacity-0');
    widget.classList.toggle('translate-y-0');
    widget.classList.toggle('opacity-100');
});

// Fermer
closeBtn.addEventListener('click', () => {
    widget.classList.add('translate-y-4', 'opacity-0');
    widget.classList.remove('translate-y-0', 'opacity-100');
});