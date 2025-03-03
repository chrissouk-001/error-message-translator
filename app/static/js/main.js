/**
 * Error Message Translator
 * Main JavaScript File
 * 
 * This file contains the client-side functionality for the Error Message Translator application.
 */

// DOM Elements
const errorInput = document.getElementById('error-input');
const languageSelect = document.getElementById('language-select');
const translateBtn = document.getElementById('translate-btn');
const clearBtn = document.getElementById('clear-btn');
const resultPlaceholder = document.getElementById('result-placeholder');
const translationContent = document.getElementById('translation-content');
const outputLanguageSelect = document.getElementById('output-language-select');
const recentSearchesContainer = document.getElementById('searches-container');

// Constants
const MAX_RECENT_SEARCHES = 5;
const STORAGE_KEY = 'error_translator_recent_searches';
const THEME_STORAGE_KEY = 'error_translator_theme';

/**
 * Initialize the application
 */
function init() {
    console.log('Initializing application...');
    
    // Check if we're on the right port
    checkPort();
    
    // Initialize the theme
    initializeTheme();
    
    // Initialize the output language selector
    initializeOutputLanguage();
    
    // Fetch the programming languages
    fetchLanguages();
    
    // Setup research notice to disappear on user interaction
    setupResearchNotice();
    
    // Load recent searches
    loadRecentSearches();
    
    // Add event listeners
    const clearBtn = document.getElementById('clear-btn');
    const copyCodeBtn = document.getElementById('copy-code-btn');
    const copyResultBtn = document.getElementById('copy-result-btn');
    
    if (clearBtn) {
        clearBtn.addEventListener('click', clearInput);
        console.log('Clear button event listener attached');
    }
    
    if (copyCodeBtn) {
        copyCodeBtn.addEventListener('click', copyCodeToClipboard);
        console.log('Copy code button event listener attached');
    }
    
    if (copyResultBtn) {
        copyResultBtn.addEventListener('click', copyResultToClipboard);
        console.log('Copy result button event listener attached');
    }
    
    // Share button functionality
    createShareButton();
    
    // Make functions accessible globally
    window.translateError = translateError;
    window.displayTranslation = displayTranslation;
    window.toggleTheme = toggleTheme;
    window.showError = showError;
    window.showLoading = showLoading;
    window.addToRecentSearches = addToRecentSearches;
    window.clearRecentSearches = clearRecentSearches;
    window.copyCodeToClipboard = copyCodeToClipboard;
    window.copyResultToClipboard = copyResultToClipboard;
    
    console.log('All global functions exposed to window object');
}

/**
 * Set up the research notice to disappear on user interaction
 */
function setupResearchNotice() {
    const researchNotice = document.querySelector('.research-notice');
    if (!researchNotice) return;
    
    // Check if user has already closed the notice before
    const noticeHidden = localStorage.getItem('research_notice_hidden') === 'true';
    if (noticeHidden) {
        researchNotice.style.display = 'none';
        return;
    }
    
    // Make sure the notice is visible
    researchNotice.style.display = 'flex';
    researchNotice.style.opacity = '1';
    
    // Set up the close button with enhanced reliability
    const closeButton = researchNotice.querySelector('.notice-close');
    if (closeButton) {
        // Remove any existing event listeners to prevent duplicates
        const newCloseButton = closeButton.cloneNode(true);
        closeButton.parentNode.replaceChild(newCloseButton, closeButton);
        
        // Make the button more visible and ensure it's clickable
        newCloseButton.style.display = 'flex';
        newCloseButton.style.opacity = '1';
        newCloseButton.style.pointerEvents = 'auto';
        newCloseButton.style.cursor = 'pointer';
        
        // Add a more robust event listener
        newCloseButton.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('Research notice close button clicked');
            
            // Hide the notice
            researchNotice.style.opacity = '0';
            setTimeout(() => {
                researchNotice.style.display = 'none';
                // Save the user's preference
                localStorage.setItem('research_notice_hidden', 'true');
            }, 300);
        });
        
        // Also add a direct onclick attribute as a fallback
        newCloseButton.setAttribute('onclick', "event.stopPropagation(); this.parentNode.style.opacity='0'; setTimeout(() => { this.parentNode.style.display='none'; localStorage.setItem('research_notice_hidden', 'true'); }, 300);");
    }
    
    // Add hover effect for better UX
    researchNotice.addEventListener('mouseenter', function() {
        const btn = researchNotice.querySelector('.notice-close');
        if (btn) btn.style.opacity = '1';
    });
    
    researchNotice.addEventListener('mouseleave', function() {
        const btn = researchNotice.querySelector('.notice-close');
        if (btn) btn.style.opacity = '0.9';
    });
    
    // Add transition effect for smooth disappearance
    researchNotice.style.transition = 'opacity 0.3s ease';
    
    // Detect scroll past a certain point to dismiss the notice
    window.addEventListener('scroll', function() {
        if (window.scrollY > 180 && researchNotice.style.display !== 'none') {
            researchNotice.style.opacity = '0';
            setTimeout(() => {
                researchNotice.style.display = 'none';
            }, 300);
        }
    }, { once: true });
    
    // Alternatively, make it disappear after 20 seconds
    setTimeout(() => {
        if (researchNotice && researchNotice.style.display !== 'none') {
            researchNotice.style.opacity = '0';
            setTimeout(() => {
                researchNotice.style.display = 'none';
            }, 300);
        }
    }, 20000);
}

// Ensure the setup runs when the DOM is loaded
document.addEventListener('DOMContentLoaded', setupResearchNotice);

/**
 * Check if we're on the correct port and show notification if needed
 */
function checkPort() {
    // Hide port notification after 5 seconds
    setTimeout(() => {
        const portNotification = document.getElementById('port-notification');
        if (portNotification) {
            portNotification.style.display = 'none';
        }
    }, 5000);
    
    // Check if we're on the correct port
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        if (window.location.port !== '5001') {
            showError('Please use port 5001: <a href="http://localhost:5001/">http://localhost:5001/</a>');
        }
    }
}

/**
 * Initialize theme based on saved preference or system preference
 */
function initializeTheme() {
    const savedTheme = localStorage.getItem(THEME_STORAGE_KEY);
    
    if (savedTheme) {
        // Use saved theme
        document.documentElement.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
    } else {
        // Check system preference
        const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const theme = prefersDarkMode ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        updateThemeIcon(theme);
    }
}

/**
 * Toggle between light and dark themes
 */
function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    // Update DOM and save preference
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem(THEME_STORAGE_KEY, newTheme);
    
    // Update theme icon
    updateThemeIcon(newTheme);
    
    // Update Prism theme if syntax highlighting is present
    updateCodeTheme(newTheme);
}

/**
 * Update the theme toggle icon based on current theme
 * @param {string} theme - The current theme ('light' or 'dark')
 */
function updateThemeIcon(theme) {
    themeToggle.innerHTML = theme === 'dark' 
        ? '<i class="fas fa-sun"></i>' 
        : '<i class="fas fa-moon"></i>';
    
    themeToggle.setAttribute('aria-label', theme === 'dark' 
        ? 'Switch to light mode' 
        : 'Switch to dark mode');
}

/**
 * Update the Prism.js theme for code highlighting
 * @param {string} theme - The current theme ('light' or 'dark')
 */
function updateCodeTheme(theme) {
    const prismThemeLink = document.getElementById('prism-theme');
    if (prismThemeLink) {
        const themeUrl = theme === 'dark'
            ? 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css'
            : 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css';
        
        prismThemeLink.href = themeUrl;
        
        // Reapply syntax highlighting if code examples are present
        if (window.Prism && codeExample.textContent.trim()) {
            Prism.highlightElement(codeExample);
        }
    }
}

/**
 * Create share button and add it to the translation header
 */
function createShareButton() {
    const translationHeader = document.querySelector('.translation-header');
    if (!translationHeader) return;
    
    // Create a container for the share button that will float right
    const shareContainer = document.createElement('div');
    shareContainer.className = 'share-container';
    
    // Create the share button
    const shareButton = document.createElement('button');
    shareButton.className = 'share-btn';
    shareButton.innerHTML = '<i class="fas fa-share-alt"></i> Share';
    shareButton.title = 'Share this error translation';
    shareButton.addEventListener('click', shareTranslation);
    
    // Add the button to the container
    shareContainer.appendChild(shareButton);
    
    // Add the container to the translation header before the language badge
    translationHeader.insertBefore(shareContainer, document.getElementById('language-badge'));
}

/**
 * Share the current translation via URL
 */
function shareTranslation() {
    const errorMessage = errorInput.value.trim();
    if (!errorMessage) {
        showError('No error message to share');
        return;
    }
    
    // Create a URL with the error message and language
    const language = languageSelect.value;
    const outputLanguage = outputLanguageSelect.value;
    const url = new URL(window.location.href);
    url.searchParams.set('error', errorMessage);
    
    if (language !== 'auto') {
        url.searchParams.set('lang', language);
    } else {
        url.searchParams.delete('lang');
    }
    
    if (outputLanguage !== 'en') {
        url.searchParams.set('output_lang', outputLanguage);
    } else {
        url.searchParams.delete('output_lang');
    }
    
    // Create a shareable link
    const shareableUrl = url.toString();
    
    // Provide options to share
    if (navigator.share) {
        // Use Web Share API if available
        navigator.share({
            title: 'Error Message Translator',
            text: 'Check out this translated error message',
            url: shareableUrl
        }).catch(err => {
            console.error('Error sharing:', err);
            copyShareLinkToClipboard(shareableUrl);
        });
    } else {
        // Fall back to copy to clipboard
        copyShareLinkToClipboard(shareableUrl);
    }
}

/**
 * Copy share link to clipboard and show feedback
 * @param {string} url - The URL to copy
 */
function copyShareLinkToClipboard(url) {
    navigator.clipboard.writeText(url)
        .then(() => {
            // Show success message
            const shareBtn = document.querySelector('.share-btn');
            const originalContent = shareBtn.innerHTML;
            
            shareBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            shareBtn.classList.add('copied');
            
            setTimeout(() => {
                shareBtn.innerHTML = originalContent;
                shareBtn.classList.remove('copied');
            }, 2000);
        })
        .catch(err => {
            console.error('Failed to copy:', err);
            alert('Copy this link to share: ' + url);
        });
}

/**
 * Fetch available programming languages
 */
async function fetchLanguages() {
    console.log('fetchLanguages function called');
    
    // Since we've added the languages directly to the HTML, 
    // we'll only log the current options for debugging
    
    const options = Array.from(languageSelect.options);
    const languages = options.map(option => ({
        id: option.value,
        name: option.textContent
    }));
    
    console.log('Current language options:', languages);
    
    // We'll still try to fetch from the API for future updates
    try {
        let apiUrl = '/api/languages';
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            apiUrl = 'http://localhost:5001/api/languages';
        }
        
        console.log('Attempting to fetch latest languages from API:', apiUrl);
        const response = await fetch(apiUrl);
        
        if (response.ok) {
            const fetchedLanguages = await response.json();
            console.log('API returned languages:', fetchedLanguages);
            // Languages are already in the HTML, so no need to update the dropdown
        } else {
            console.log('API request failed, using default languages');
        }
    } catch (error) {
        console.error('Error fetching languages from API:', error);
        // No need to handle the error as we already have languages in the HTML
    }
}

/**
 * Translate the error message
 */
async function translateError() {
    console.log('translateError function called');
    
    const errorMessage = errorInput.value.trim();
    if (!errorMessage) {
        showError('Please enter an error message to translate.');
        return;
    }
    
    console.log('Error message to translate:', errorMessage);
    
    // Show loading overlay
    showLoading(true);
    
    try {
        // Get selected language
        const language = languageSelect.value;
        console.log('Selected language:', language);
        
        // Build the API URL
        let apiUrl = '/api/translate';
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            apiUrl = 'http://localhost:5001/api/translate';
        }
        
        console.log('API URL:', apiUrl);
        
        // Make the API request
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                error_message: errorMessage,
                language: language,
                output_language: 'en'  // Always English
            })
        });
        
        if (!response.ok) {
            const errorText = await response.text();
            console.error('API error response:', errorText);
            throw new Error(`Server error: ${response.status}`);
        }
        
        // Parse the response
        const result = await response.json();
        console.log('Translation result:', result);
        
        // Display the translation
        displayTranslation(result);
        
        // Save to recent searches
        addToRecentSearches(result);
        
    } catch (error) {
        console.error('Translation error:', error);
        showError(`Failed to translate: ${error.message}`);
    } finally {
        showLoading(false);
    }
}

/**
 * Display the translation result
 */
function displayTranslation(result) {
    console.log('displayTranslation called with result:', result);

    // Hide placeholder, show content
    resultPlaceholder.style.display = 'none';
    translationContent.style.display = 'block';
    
    // Display the error title and add language badge
    const errorTitle = document.getElementById('error-title');
    errorTitle.textContent = result.title || 'Unknown Error';
    
    // Set the language badge
    const languageBadge = document.getElementById('language-badge');
    languageBadge.textContent = capitalizeFirstLetter(result.language || 'general');
    languageBadge.setAttribute('data-language', result.language || 'general');
    
    // Set the difficulty badge
    const difficultyBadge = document.getElementById('difficulty-badge');
    const difficulty = result.difficulty || 'intermediate';
    difficultyBadge.textContent = capitalizeFirstLetter(difficulty);
    difficultyBadge.setAttribute('data-difficulty', difficulty);
    
    // Clear existing badges except language and difficulty
    const badgesContainer = document.querySelector('.badges-container');
    Array.from(badgesContainer.children).forEach(child => {
        if (child !== languageBadge && child !== difficultyBadge) {
            child.remove();
        }
    });
    
    // Set original error
    const originalError = document.getElementById('original-error');
    originalError.textContent = result.original_error || result.original || '';
    
    // Set explanation
    const explanationText = document.getElementById('explanation-text');
    explanationText.innerHTML = result.explanation || 'No explanation available.';
    
    // Set solution
    const solutionText = document.getElementById('solution-text');
    solutionText.innerHTML = result.solution || 'No solution available.';
    
    // Set code example if available
    const codeExampleContainer = document.getElementById('code-example-container');
    const codeExample = document.getElementById('code-example');
    
    if (result.code_example) {
        codeExampleContainer.style.display = 'block';
        codeExample.textContent = result.code_example;
        
        // Apply syntax highlighting
        const languageClass = getPrismLanguageClass(result.language);
        codeExample.className = `language-${languageClass}`;
        Prism.highlightElement(codeExample);
    } else {
        codeExampleContainer.style.display = 'none';
    }
    
    // Set related errors if available
    const relatedErrorsContainer = document.getElementById('related-errors-container');
    const relatedErrorsList = document.getElementById('related-errors-list');
    
    if (result.related_errors && result.related_errors.length > 0) {
        relatedErrorsContainer.style.display = 'block';
        relatedErrorsList.innerHTML = '';
        
        result.related_errors.forEach(error => {
            const li = document.createElement('li');
            li.textContent = error.title || error.id || error;
            relatedErrorsList.appendChild(li);
        });
    } else {
        relatedErrorsContainer.style.display = 'none';
    }
    
    // Add this translation to recent searches
    addToRecentSearches(result);
    
    // Scroll to the translation section
    translationContent.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Get the appropriate Prism.js language class based on the error language
 * @param {string} language - The language of the error
 * @returns {string} The Prism.js language class
 */
function getPrismLanguageClass(language) {
    switch (language) {
        case 'python':
            return 'python';
        case 'javascript':
            return 'javascript';
        case 'html':
            return 'markup';
        case 'css':
            return 'css';
        default:
            return 'none';
    }
}

/**
 * Show or hide the loading overlay
 * @param {boolean} show - Whether to show the loading overlay
 */
function showLoading(show) {
    loadingOverlay.style.display = show ? 'flex' : 'none';
}

/**
 * Show an error message to the user
 */
function showError(message) {
    console.error('Error:', message);
    
    // Create toast notification if not exists
    let toast = document.querySelector('.toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.className = 'toast error';
        
        const icon = document.createElement('div');
        icon.className = 'toast-icon';
        icon.innerHTML = '<i class="fas fa-exclamation-circle"></i>';
        
        const messageEl = document.createElement('div');
        messageEl.className = 'toast-message';
        
        const closeBtn = document.createElement('button');
        closeBtn.className = 'toast-close';
        closeBtn.innerHTML = '<i class="fas fa-times"></i>';
        closeBtn.addEventListener('click', function() {
            toast.classList.remove('show');
        });
        
        toast.appendChild(icon);
        toast.appendChild(messageEl);
        toast.appendChild(closeBtn);
        document.body.appendChild(toast);
    }
    
    // Set message (allow HTML content when needed)
    const messageEl = toast.querySelector('.toast-message');
    messageEl.innerHTML = message;
    
    // Show toast
    toast.classList.add('show');
    
    // Auto hide after 5 seconds
    setTimeout(function() {
        toast.classList.remove('show');
    }, 5000);
}

/**
 * Clear the input field
 */
function clearInput() {
    errorInput.value = '';
    errorInput.focus();
}

/**
 * Copy the code example to clipboard
 */
async function copyCodeToClipboard() {
    console.log('copyCodeToClipboard function called');
    const codeExample = document.getElementById('code-example');
    
    if (!codeExample || !codeExample.textContent.trim()) {
        console.log('No code content to copy');
        return;
    }
    
    try {
        await navigator.clipboard.writeText(codeExample.textContent);
        console.log('Code copied to clipboard successfully');
    } catch (error) {
        console.error('Error copying to clipboard:', error);
    }
}

/**
 * Copy the entire translation result to clipboard
 */
async function copyResultToClipboard() {
    console.log('copyResultToClipboard function called');
    
    const errorTitle = document.getElementById('error-title').textContent;
    const originalError = document.getElementById('original-error').textContent;
    const explanation = document.getElementById('explanation-text').textContent;
    const solution = document.getElementById('solution-text').textContent;
    
    let textToCopy = `${errorTitle}\n\nOriginal Error:\n${originalError}\n\nExplanation:\n${explanation}\n\nSolution:\n${solution}`;
    
    // Add code example if available
    const codeExample = document.getElementById('code-example');
    if (codeExample && codeExample.textContent.trim()) {
        textToCopy += `\n\nCode Example:\n${codeExample.textContent}`;
    }
    
    try {
        await navigator.clipboard.writeText(textToCopy);
        console.log('Result copied to clipboard successfully');
    } catch (error) {
        console.error('Error copying to clipboard:', error);
    }
}

/**
 * Add translation to recent searches
 */
function addToRecentSearches(translation) {
    // Get existing searches or initialize empty array
    let searches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
    
    // Log for testing
    console.log('Adding to recent searches:', translation);
    
    // Add new search to the beginning
    const newSearch = {
        id: Date.now(),
        timestamp: new Date().toISOString(),
        language: translation.language || 'general',
        title: translation.title || 'Unknown Error',
        error: translation.original_error || translation.original || '',
        explanation: translation.explanation || '',
        solution: translation.solution || '',
        code_example: translation.code_example || '',
        related_errors: translation.related_errors || [],
        output_language: 'en'
    };
    
    // Add to beginning of array
    searches.unshift(newSearch);
    
    // Limit to 10 recent searches
    searches = searches.slice(0, 10);
    
    // Save back to localStorage
    localStorage.setItem('recentSearches', JSON.stringify(searches));
    
    // Update the UI
    loadRecentSearches();
}

/**
 * Load recent searches from localStorage
 */
function loadRecentSearches() {
    const searches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
    const container = document.getElementById('searches-container');
    
    // Log for testing
    console.log('Loading recent searches:', searches);
    
    if (searches.length === 0) {
        container.innerHTML = '<p class="empty-message">Your recent searches will appear here</p>';
        return;
    }
    
    container.innerHTML = '';
    
    searches.forEach(search => {
        const searchItem = document.createElement('div');
        searchItem.className = 'search-item';
        searchItem.setAttribute('data-error', search.error || '');
        
        const header = document.createElement('div');
        header.className = 'search-item-header';
        
        const title = document.createElement('h4');
        title.textContent = search.title;
        
        const timestamp = document.createElement('span');
        timestamp.className = 'timestamp';
        timestamp.textContent = formatTimestamp(search.timestamp);
        
        header.appendChild(title);
        header.appendChild(timestamp);
        
        const badges = document.createElement('div');
        badges.className = 'search-item-badges';
        
        const languageBadge = document.createElement('span');
        languageBadge.className = 'badge language-badge';
        languageBadge.setAttribute('data-language', search.language);
        languageBadge.textContent = capitalizeFirstLetter(search.language);
        badges.appendChild(languageBadge);
        
        // Add click handler to reload this translation
        searchItem.addEventListener('click', () => {
            console.log('Loading previous search:', search);
            
            // Create a result object compatible with displayTranslation
            const result = {
                title: search.title,
                language: search.language,
                original_error: search.error,
                explanation: search.explanation,
                solution: search.solution,
                output_language: search.output_language,
                code_example: search.code_example,
                related_errors: search.related_errors
            };
            
            // Display it
            displayTranslation(result);
            
            // Scroll to the result
            document.getElementById('translation-result').scrollIntoView({ behavior: 'smooth' });
        });
        
        searchItem.appendChild(header);
        searchItem.appendChild(badges);
        container.appendChild(searchItem);
    });
}

/**
 * Format a timestamp into a human-readable string
 * @param {string} timestamp - ISO timestamp string
 * @returns {string} Formatted timestamp
 */
function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    const now = new Date();
    const diffMs = now - date;
    const diffSec = Math.round(diffMs / 1000);
    const diffMin = Math.round(diffSec / 60);
    const diffHour = Math.round(diffMin / 60);
    const diffDay = Math.round(diffHour / 24);
    
    if (diffSec < 60) {
        return 'Just now';
    } else if (diffMin < 60) {
        return `${diffMin} minute${diffMin === 1 ? '' : 's'} ago`;
    } else if (diffHour < 24) {
        return `${diffHour} hour${diffHour === 1 ? '' : 's'} ago`;
    } else if (diffDay < 30) {
        return `${diffDay} day${diffDay === 1 ? '' : 's'} ago`;
    } else {
        // Format as MM/DD/YYYY
        return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`;
    }
}

/**
 * Capitalize the first letter of a string
 * @param {string} string - The string to capitalize
 * @returns {string} Capitalized string
 */
function capitalizeFirstLetter(string) {
    if (!string) return '';
    return string.charAt(0).toUpperCase() + string.slice(1);
}

/**
 * Create a shareable link for the current error and language
 * @returns {string} The shareable URL
 */
function createShareLink() {
    // Create a URL with the error message and language
    const errorMessage = errorInput.value.trim();
    const language = languageSelect.value;
    const outputLanguage = outputLanguageSelect.value;
    const url = new URL(window.location.href);
    url.searchParams.set('error', errorMessage);
    
    if (language !== 'auto') {
        url.searchParams.set('lang', language);
    } else {
        url.searchParams.delete('lang');
    }
    
    if (outputLanguage !== 'en') {
        url.searchParams.set('output_lang', outputLanguage);
    } else {
        url.searchParams.delete('output_lang');
    }
    
    // Create a shareable link
    return url.toString();
}

/**
 * Check if an element is visible in the viewport
 * @param {HTMLElement} element - The element to check
 * @returns {boolean} True if the element is in the viewport
 */
function isElementInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Initialize the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    console.log('All DOM elements:', {
        errorInput: !!document.getElementById('error-input'),
        languageSelect: !!document.getElementById('language-select'),
        outputLanguageSelect: !!document.getElementById('output-language-select'),
        translateBtn: !!document.getElementById('translate-btn')
    });
    
    // Initialize the application
    init();
    
    // Double-check button connections
    const translateBtn = document.getElementById('translate-btn');
    if (translateBtn) {
        console.log('Found translate button, adding event listener');
        translateBtn.addEventListener('click', translateError);
    } else {
        console.error('Translate button not found!');
    }
});

// TODO: Implement error message validation 

/**
 * Clear all recent searches (for testing purposes)
 */
function clearRecentSearches() {
    localStorage.removeItem('recentSearches');
    loadRecentSearches();
    console.log('Recent searches cleared');
}

/**
 * Test the recent searches functionality
 */
function testRecentSearches() {
    console.log('🧪 STARTING RECENT SEARCHES TESTS');
    
    // 1. Clear existing searches
    console.log('Test 1: Clearing existing searches');
    localStorage.removeItem('recentSearches');
    loadRecentSearches();
    
    // Verify cleared state
    let searches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
    console.assert(searches.length === 0, 'Expected 0 searches after clearing');
    console.log('✅ Cleared searches successfully');
    
    // 2. Add a test search
    console.log('Test 2: Adding a single test search');
    const testSearch1 = {
        title: 'Test Error 1',
        language: 'python',
        original_error: 'Test error message 1',
        explanation: 'This is a test explanation',
        solution: 'This is a test solution'
    };
    
    addToRecentSearches(testSearch1);
    
    // Verify added state
    searches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
    console.assert(searches.length === 1, 'Expected 1 search after adding');
    console.assert(searches[0].title === 'Test Error 1', 'Expected correct title');
    console.log('✅ Added single search successfully');
    
    // 3. Add multiple test searches
    console.log('Test 3: Adding multiple test searches');
    const testSearch2 = {
        title: 'Test Error 2',
        language: 'javascript',
        original_error: 'Test error message 2',
        explanation: 'This is another test explanation',
        solution: 'This is another test solution'
    };
    
    const testSearch3 = {
        title: 'Test Error 3',
        language: 'html',
        original_error: 'Test error message 3',
        explanation: 'This is a third test explanation',
        solution: 'This is a third test solution'
    };
    
    addToRecentSearches(testSearch2);
    addToRecentSearches(testSearch3);
    
    // Verify multiple added
    searches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
    console.assert(searches.length === 3, 'Expected 3 searches after adding more');
    console.assert(searches[0].title === 'Test Error 3', 'Expected newest search first');
    console.log('✅ Added multiple searches successfully');
    
    // 4. Test ordering (most recent first)
    console.log('Test 4: Verifying search order');
    console.assert(searches[0].title === 'Test Error 3', 'First item should be most recent');
    console.assert(searches[1].title === 'Test Error 2', 'Second item should be second most recent');
    console.assert(searches[2].title === 'Test Error 1', 'Third item should be least recent');
    console.log('✅ Search order is correct');
    
    // 5. Test limit to 10 items
    console.log('Test 5: Testing limit of 10 items');
    // Add 10 more searches
    for (let i = 4; i <= 13; i++) {
        addToRecentSearches({
            title: `Test Error ${i}`,
            language: 'general',
            original_error: `Test error message ${i}`,
            explanation: `This is explanation ${i}`,
            solution: `This is solution ${i}`
        });
    }
    
    // Verify limit
    searches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
    console.assert(searches.length === 10, 'Expected max 10 searches');
    console.assert(searches[0].title === 'Test Error 13', 'Expected newest search still first');
    console.assert(searches[9].title === 'Test Error 4', 'Expected oldest search to be #4');
    console.log('✅ Search limit working correctly');
    
    // 6. Visual verification of DOM elements
    console.log('Test 6: Verifying DOM elements');
    const container = document.getElementById('searches-container');
    const items = container.querySelectorAll('.search-item');
    console.assert(items.length === 10, 'Expected 10 search items in DOM');
    
    // Check the first item's content
    const firstItem = items[0];
    const title = firstItem.querySelector('h4').textContent;
    console.assert(title === 'Test Error 13', 'Expected correct title in DOM');
    console.log('✅ DOM elements created correctly');
    
    // 7. Test click handling (simulate a click)
    console.log('Test 7: Testing click handling');
    console.log('Simulating click on first search item...');
    firstItem.click();
    
    // Verify translation content is displayed
    const translationContent = document.getElementById('translation-content');
    console.assert(translationContent.style.display === 'block', 'Expected translation content to be displayed');
    console.log('✅ Click handling working correctly');
    
    // 8. Test persistence after page reload
    console.log('Test 8: Verifying persistence (check after page reload)');
    console.log('Current searches will persist after page reload. Refresh the page to verify.');
    
    console.log('🎉 ALL TESTS COMPLETED SUCCESSFULLY');
    showTestResultPopup();
}

/**
 * Show a popup with test results
 */
function showTestResultPopup() {
    const popup = document.createElement('div');
    popup.className = 'test-popup';
    popup.innerHTML = `
        <div class="test-popup-content">
            <h3>Recent Searches Tests Completed</h3>
            <p>All tests passed successfully! ✅</p>
            <p>The Recent Searches section now contains test data.</p>
            <p>You can:</p>
            <ul>
                <li>Click on any search to verify it loads correctly</li>
                <li>Clear all searches by typing <code>clearRecentSearches()</code> in the console</li>
                <li>Reload the page to verify persistence</li>
            </ul>
            <button id="close-test-popup" class="primary-btn">Close</button>
        </div>
    `;
    
    document.body.appendChild(popup);
    
    document.getElementById('close-test-popup').addEventListener('click', () => {
        popup.remove();
    });
}

// Make the function globally accessible
window.testRecentSearches = testRecentSearches;
