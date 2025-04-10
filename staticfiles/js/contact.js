AOS.init({
    duration: 800,
    once: true,
    disable: window.innerWidth < 768 // Désactive AOS sur mobile si nécessaire
});

// Validation du formulaire
document.querySelector('.contact-form')?.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Récupération des valeurs
    const prenom = document.getElementById('prenom').value;
    const nom = document.getElementById('nom').value;
    const email = document.getElementById('email').value;
    const sujet = document.getElementById('sujet').value;
    const message = document.getElementById('message').value;
    const consentement = document.getElementById('consentement').checked;
    
    // Validation simple
    if (!prenom || !nom || !email || !sujet || !message || !consentement) {
        alert('Veuillez remplir tous les champs obligatoires et accepter les conditions');
        return;
    }
    
    // Ici vous pourriez ajouter une requête AJAX pour envoyer le formulaire
    alert('Message envoyé avec succès! Nous vous contacterons bientôt.');
    this.reset();
});