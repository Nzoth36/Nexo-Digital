// Contact form handling
document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.querySelector('form') ? document.querySelector('form') : null;

    if (contactForm && contactForm.closest('#contacto')) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const fullName = contactForm.querySelector('[placeholder*="Ej. Juan"]')?.value || '';
            const company = contactForm.querySelector('[placeholder*="compañía"]')?.value || '';
            const email = contactForm.querySelector('[type="email"]')?.value || '';
            const message = contactForm.querySelector('textarea')?.value || '';
            const submitBtn = contactForm.querySelector('button[type="button"]');

            if (!fullName || !email || !message) {
                alert('Por favor completa los campos requeridos');
                return;
            }

            try {
                submitBtn.disabled = true;
                submitBtn.innerHTML = 'Enviando...';

                const response = await fetch('/api/contact/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        full_name: fullName,
                        email: email,
                        company: company,
                        message: message
                    })
                });

                if (response.ok) {
                    alert('¡Mensaje enviado exitosamente! Te contactaremos pronto.');
                    contactForm.reset();
                } else {
                    alert('Error al enviar el mensaje. Intenta de nuevo.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error al enviar el mensaje.');
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = 'Enviar Mensaje';
            }
        });
    }
});
