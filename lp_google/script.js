document.addEventListener('DOMContentLoaded', () => {
  const privacyLink = document.getElementById('privacy-policy-link');
  const privacyModal = document.getElementById('privacy-modal');
  const closeModal = document.querySelector('.close-modal');
  const acceptBtn = document.querySelector('.accept-btn');
  const iframe = document.getElementById('google-form-iframe');

  if (!localStorage.getItem('lgpdConsent')) {
    setTimeout(() => privacyModal.style.display = 'block', 1000);
  }

  privacyLink.onclick = (e) => {
    e.preventDefault();
    privacyModal.style.display = 'block';
  };

  closeModal.onclick = () => privacyModal.style.display = 'none';
  acceptBtn.onclick = () => {
    localStorage.setItem('lgpdConsent', 'true');
    privacyModal.style.display = 'none';
  };
  window.onclick = (e) => {
    if (e.target === privacyModal) privacyModal.style.display = 'none';
  };
});
