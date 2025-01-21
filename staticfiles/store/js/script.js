document.querySelectorAll('.upload-area').forEach((uploadArea, index) => {
    const fileInput = uploadArea.querySelector('.file-input');
    const fileListContainer = uploadArea.querySelector('.file-list');

    // Highlight upload area on dragover
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.style.borderColor = '#1cc972';
        uploadArea.style.backgroundColor = '#e6ffe6';
    });

    // Remove highlight on dragleave
    uploadArea.addEventListener('dragleave', () => {
        uploadArea.style.borderColor = '#6a6b76';
        uploadArea.style.backgroundColor = 'transparent';
    });

    // Handle file drop
    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.style.borderColor = '#6a6b76';
        uploadArea.style.backgroundColor = 'transparent';
        const files = e.dataTransfer.files;
        handleFiles(files, fileListContainer);
    });

    // Open file dialog on click
    uploadArea.addEventListener('click', () => {
        fileInput.click();
    });

    // Handle file input change
    fileInput.addEventListener('change', (e) => {
        const files = e.target.files;
        handleFiles(files, fileListContainer);
    });

    // Function to handle files and display file names
    function handleFiles(files, fileListContainer) {
        fileListContainer.innerHTML = ''; // Clear the existing list
        Array.from(files).forEach((file) => {
            const listItem = document.createElement('div');
            listItem.classList.add('file-list-item');
            listItem.textContent = file.name;
            fileListContainer.appendChild(listItem);
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const messageElement = document.getElementById('latest-message');
    if (messageElement) {
        setTimeout(() => {
            messageElement.style.display = 'none';
        }, 3000); // 3000ms = 3 seconds
    }
});


document.addEventListener('DOMContentLoaded', () => {
    const notificationContainer = document.querySelector('.notification-container');
    
    if (notificationContainer) {
        // Slide down
        notificationContainer.style.top = '20px';

        // Slide up after 3 seconds
        setTimeout(() => {
            notificationContainer.style.top = '-100px';
        }, 3000); // 3000ms = 3 seconds
    }
});

