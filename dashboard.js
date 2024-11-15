document.getElementById('file-input').addEventListener('change', handleFileSelect);

function handleFileSelect(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
        const content = e.target.result;
        // Parse CSV and send it to backend
    };
    reader.readAsText(file);
}

function sendEmail() {
    const subject = document.getElementById('email-subject').value;
    const body = document.getElementById('email-body').value;
    // Send email request to the backend
    fetch('/send-email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ subject, body }),
    })
    .then(response => response.json())
    .then(data => updateAnalytics(data));
}

function updateAnalytics(data) {
    document.getElementById('total-sent').textContent = data.sent;
    document.getElementById('failed-emails').textContent = data.failed;
    document.getElementById('scheduled-emails').textContent = data.scheduled;
}
