// Toast notification functionality
function showToast(message, type = 'info') {
    // Remove any existing toasts
    const existingToast = document.querySelector('.toast');
    if (existingToast) {
        existingToast.remove();
    }
    
    // Create toast elements
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    let iconClass = 'fa-info-circle';
    switch(type) {
        case 'error':
            iconClass = 'fa-exclamation-circle';
            break;
        case 'success':
            iconClass = 'fa-check-circle';
            break;
        case 'warning':
            iconClass = 'fa-exclamation-triangle';
            break;
    }
    
    toast.innerHTML = `
        <div class="toast-icon"><i class="fas ${iconClass}"></i></div>
        <div class="toast-message">${message}</div>
        <button class="toast-close"><i class="fas fa-times"></i></button>
    `;
    
    document.body.appendChild(toast);
    
    // Show the toast
    setTimeout(() => {
        toast.classList.add('show');
    }, 10);
    
    // Add event listener to close button
    const closeBtn = toast.querySelector('.toast-close');
    closeBtn.addEventListener('click', () => {
        toast.classList.remove('show');
        setTimeout(() => {
            toast.remove();
        }, 300); // Wait for transition to complete
    });
    
    // Auto-close after 5 seconds
    setTimeout(() => {
        if (document.body.contains(toast)) {
            toast.classList.remove('show');
            setTimeout(() => {
                if (document.body.contains(toast)) {
                    toast.remove();
                }
            }, 300);
        }
    }, 5000);
}

// Enhance the main.js functionality with toast notifications
document.addEventListener('DOMContentLoaded', function() {
    // Override the showError function to use toast
    if (typeof window.showError === 'function') {
        const originalShowError = window.showError;
        window.showError = function(message) {
            showToast(message, 'error');
            originalShowError(message);
        };
    }
    
    // Replace the original translateError with our enhanced version
    if (typeof window.translateError === 'function') {
        const originalTranslateError = window.translateError;
        window.translateError = function() {
            const errorInput = document.getElementById('error-input').value.trim();
            
            if (!errorInput) {
                showToast('Please enter an error message to translate.', 'warning');
                return;
            }
            
            // Call the original function
            originalTranslateError();
        };
    }
    
    // Listen for successful translations to show toast
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'attributes' && 
                mutation.attributeName === 'style' && 
                document.getElementById('translation-content').style.display !== 'none') {
                
                // Get output language for the toast message
                const outputLangIndicator = document.querySelector('.output-language-indicator');
                let toastMessage = 'Error message translated successfully!';
                
                if (outputLangIndicator) {
                    toastMessage = `Error message translated to ${outputLangIndicator.textContent}!`;
                }
                
                showToast(toastMessage, 'success');
                
                // Once we've shown the toast, disconnect to avoid showing it multiple times
                observer.disconnect();
                // Reconnect after a short delay
                setTimeout(() => {
                    const translationContent = document.getElementById('translation-content');
                    if (translationContent) {
                        observer.observe(translationContent, { attributes: true });
                    }
                }, 1000);
            }
        });
    });
    
    const translationContent = document.getElementById('translation-content');
    if (translationContent) {
        observer.observe(translationContent, { attributes: true });
    }
});

// Add event listener for help button
document.addEventListener('DOMContentLoaded', function() {
    const helpBtn = document.getElementById('help-btn');
    if (helpBtn) {
        helpBtn.addEventListener('click', showHelpModal);
    }
});

// Function to show help modal
function showHelpModal() {
    // Remove any existing modal
    const existingModal = document.querySelector('.modal');
    if (existingModal) {
        existingModal.remove();
    }
    
    // Create modal elements
    const modal = document.createElement('div');
    modal.className = 'modal';
    
    const modalContent = document.createElement('div');
    modalContent.className = 'modal-content card';
    
    const closeBtn = document.createElement('button');
    closeBtn.className = 'modal-close';
    closeBtn.innerHTML = '<i class="fas fa-times"></i>';
    
    const title = document.createElement('h2');
    title.textContent = 'How Error Message Translator Works';
    
    const content = document.createElement('div');
    content.className = 'modal-body';
    content.innerHTML = `
        <p>Error Message Translator helps beginner developers understand and fix cryptic error messages by:</p>
        <ol>
            <li>
                <strong>Paste Your Error</strong>
                <p>Copy the error message from your console or IDE and paste it into the input box.</p>
            </li>
            <li>
                <strong>Select Language (Optional)</strong>
                <p>Choose the programming language to help with more accurate translations, or let the system auto-detect it.</p>
            </li>
            <li>
                <strong>Get Translation</strong>
                <p>Click "Translate Error" and receive a beginner-friendly explanation of what went wrong.</p>
            </li>
            <li>
                <strong>Apply Solution</strong>
                <p>Follow the provided solution steps and code examples to fix your issue.</p>
            </li>
        </ol>
        <p>Your recent searches are saved locally for easy reference. You can also share error translations with others via a shareable link.</p>
    `;
    
    // Assemble the modal
    modalContent.appendChild(closeBtn);
    modalContent.appendChild(title);
    modalContent.appendChild(content);
    modal.appendChild(modalContent);
    
    // Add event listener to close button
    closeBtn.addEventListener('click', () => {
        modal.classList.remove('show');
        setTimeout(() => {
            modal.remove();
        }, 300);
    });
    
    // Add event listener to close on outside click
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.remove();
            }, 300);
        }
    });
    
    // Add to DOM and show
    document.body.appendChild(modal);
    setTimeout(() => {
        modal.classList.add('show');
    }, 10);
}

// Add helper functions for loading overlay
function showLoadingOverlay() {
    if (typeof window.showLoading === 'function') {
        window.showLoading(true);
    } else {
        const loadingOverlay = document.getElementById('loading-overlay');
        if (loadingOverlay) {
            loadingOverlay.style.display = 'flex';
        }
    }
}

function hideLoadingOverlay() {
    if (typeof window.showLoading === 'function') {
        window.showLoading(false);
    } else {
        const loadingOverlay = document.getElementById('loading-overlay');
        if (loadingOverlay) {
            loadingOverlay.style.display = 'none';
        }
    }
}

// Add helper for adding to history
function addToHistory(errorMessage, explanation, solution) {
    if (typeof window.addToRecentSearches === 'function') {
        window.addToRecentSearches({
            original: errorMessage,
            explanation: explanation,
            solution: solution
        });
    }
} 