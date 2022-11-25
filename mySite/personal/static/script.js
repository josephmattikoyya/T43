const toggle = document.getElementById('darkmode-switch');
const body = document.body;

toggle.addEventListener('input', e => {
    const isChecked = e.target.checked;

    if (isChecked) {
        console.log('True')
        body.classList.add('dark-theme');
    } else {
        console.log('False')
        body.classList.remove('dark-theme');
    }
});
