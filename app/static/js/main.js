/**
 * Error Message Translator
 * Main JavaScript File
 * 
 * This file contains the client-side functionality for the Error Message Translator application.
 */

// DOM Elements
const errorInput = document.getElementById('error-message');
const languageSelect = document.getElementById('language-input');
const translateBtn = document.getElementById('translate-btn');
const clearBtn = document.getElementById('clear-btn');
const copyBtn = document.getElementById('copy-btn');
const resultPlaceholder = document.getElementById('result-placeholder');
const translationContent = document.getElementById('translation-result');
const outputLanguageSelect = document.getElementById('output-language-select');
const recentSearchesContainer = document.getElementById('searches-container');
const helpBtn = document.getElementById('help-btn');
const modal = document.getElementById('help-modal');
const modalClose = document.querySelector('.modal-close');
const toast = document.getElementById('toast');
const toastMessage = document.querySelector('.toast-message');
const toastClose = document.querySelector('.toast-close');
const themeToggle = document.getElementById('theme-toggle');
const howItWorksBtn = document.getElementById('how-it-works-btn');

// Constants
const MAX_RECENT_SEARCHES = 5;
const STORAGE_KEY = 'error_translator_recent_searches';
const THEME_STORAGE_KEY = 'error_translator_theme';

/**
 * Initialize the application
 */
function initApp() {
    console.log('Initializing application...');
    
    // Check if we're on the right port
    checkPort();
    
    // Initialize the theme
    initTheme();
    
    // Initialize the output language selector
    initializeOutputLanguage();
    
    // Fetch the programming languages
    fetchLanguages();
    
    // Setup research notice to disappear on user interaction
    setupResearchNotice();
    
    // Load recent searches
    loadRecentSearches();
    
    // Add event listeners
    const copyCodeBtn = document.getElementById('copy-code-btn');
    const copyResultBtn = document.getElementById('copy-result-btn');
    
    if (helpBtn && modal) {
        helpBtn.addEventListener('click', function() {
            console.log('How It Works button clicked');
            modal.classList.add('show');
        });
        
        if (modalClose) {
            modalClose.addEventListener('click', function() {
                modal.classList.remove('show');
            });
        }
        
        // Also close when clicked outside
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                modal.classList.remove('show');
            }
        });
    }
    
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
        console.log('Theme toggle event listener attached');
    }
    
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
function initTheme() {
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
 * Initialize the output language selector
 */
function initializeOutputLanguage() {
    const outputLanguageSelector = document.getElementById('output-language');
    if (outputLanguageSelector) {
        // Set default language
        outputLanguageSelector.value = 'en';
        
        // Add event listener for language change
        outputLanguageSelector.addEventListener('change', function() {
            // You can add functionality here to handle language changes
            // For example, retranslate the current error message
            if (document.getElementById('error-input').value.trim()) {
                translateError();
            }
        });
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
    const themeToggle = document.getElementById('theme-toggle');
    if (!themeToggle) return;
    
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
        const codeExample = document.getElementById('code-example');
        if (window.Prism && codeExample && codeExample.textContent.trim()) {
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
    
    // Debug element existence
    console.log('Debug - Elements check:', {
        errorInput: !!errorInput,
        errorInputValue: errorInput ? errorInput.value : 'undefined',
        translateBtn: !!translateBtn,
        loadingOverlay: !!document.getElementById('loading-overlay'),
        languageSelect: !!languageSelect,
        selectedLanguage: languageSelect ? languageSelect.value : 'undefined'
    });
    
    const errorMessage = errorInput.value.trim();
    if (!errorMessage) {
        showError('Please enter an error message to translate.');
        return;
    }
    
    console.log('Error message to translate:', errorMessage);
    
    // Show loading overlay
    showLoading(true);
    
    try {
        // Get selected language, ensure it's a valid value
        let language = 'auto';
        if (languageSelect && languageSelect.value) {
            language = languageSelect.value;
        }
        console.log('Selected language:', language);
        
        // Build the API URL
        let apiUrl = '/api/translate';
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            apiUrl = 'http://localhost:5001/api/translate';
        }
        
        console.log('API URL:', apiUrl);
        
        // Make the API request
        console.log('Making API request with language:', language);
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                error_message: errorMessage,
                language: language,
                output_language: 'en'  // Always English
            })
        });
        
        console.log('API response received, status:', response.status);
        
        if (!response.ok) {
            const errorText = await response.text();
            console.error('API error response:', errorText);
            throw new Error(`Server error: ${response.status}`);
        }
        
        // Parse the response
        console.log('Parsing response as JSON...');
        const result = await response.json();
        console.log('Translation result:', result);
        
        // Display the translation
        displayTranslation(result);
        
        // Update language selector to match the detected language
        if (language === 'auto' && result.language && languageSelect) {
            console.log('Auto-detected language:', result.language);
            // Only update the UI, don't trigger another translation
            const options = Array.from(languageSelect.options);
            const foundOption = options.find(option => option.value === result.language);
            if (foundOption) {
                // No need to change the selection as it should stay as auto
                console.log('Language detected:', result.language);
            }
        }
        
        // Set the language badge
        const languageBadge = document.getElementById('language-badge');
        if (languageBadge && result.language) {
            languageBadge.textContent = capitalizeFirstLetter(result.language);
            languageBadge.dataset.language = result.language;
            console.log('Updated language badge to:', result.language);
        }
        
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
function displayTranslation(translation) {
    console.log('Displaying translation:', translation);
    
    // Hide placeholder and show result
    if (resultPlaceholder) resultPlaceholder.style.display = 'none';
    if (translationContent) {
        translationContent.style.display = 'block';
        translationContent.classList.remove('hidden');
    }
    
    // Get error text - handle both possible field names
    const errorText = translation.error || translation.original_error || '';
    
    // Update error title
    const errorTitle = document.getElementById('error-title');
    if (errorTitle) {
        const title = translation.title || (translation.language ? `${translation.language} Error` : 'Error Translation');
        errorTitle.textContent = title;
        console.log('Set error title to:', title);
    }
    
    // Set original error text
    const originalError = document.getElementById('original-error');
    if (originalError) {
        originalError.textContent = errorText;
        console.log('Set original error to:', errorText.substring(0, 50) + (errorText.length > 50 ? '...' : ''));
    }
    
    // Set explanation
    const explanation = document.getElementById('explanation-text') || document.getElementById('explanation');
    if (explanation) {
        explanation.textContent = translation.explanation || 'No explanation available';
        console.log('Updated explanation with:', translation.explanation);
    } else {
        console.error('Could not find explanation element with ID "explanation" or "explanation-text"');
    }
    
    // Set solution
    const solution = document.getElementById('solution-text') || document.getElementById('solution');
    if (solution) {
        solution.textContent = translation.solution || 'No solution available';
        console.log('Updated solution with:', translation.solution);
    } else {
        console.error('Could not find solution element with ID "solution" or "solution-text"');
    }
    
    // Set language badge
    const languageBadge = document.getElementById('language-badge');
    if (languageBadge && translation.language) {
        const capitalized = capitalizeFirstLetter(translation.language);
        languageBadge.textContent = capitalized;
        languageBadge.dataset.language = translation.language;
        console.log('Set language badge to:', capitalized);
    }
    
    // Set difficulty badge
    const difficultyBadge = document.getElementById('difficulty-badge');
    if (difficultyBadge && translation.difficulty) {
        const capitalized = capitalizeFirstLetter(translation.difficulty);
        difficultyBadge.textContent = capitalized;
        difficultyBadge.dataset.difficulty = translation.difficulty;
        console.log('Set difficulty badge to:', capitalized);
    }
    
    // Set code example if available
    const codeExampleSection = document.getElementById('code-example-section');
    const codeExample = document.getElementById('code-example');
    if (codeExampleSection && codeExample && translation.code_example) {
        codeExample.textContent = translation.code_example;
        codeExampleSection.classList.remove('hidden');
        
        // Apply syntax highlighting
        if (translation.language && typeof Prism !== 'undefined') {
            const prismLanguage = getPrismLanguageClass(translation.language);
            codeExample.className = `language-${prismLanguage}`;
            Prism.highlightElement(codeExample);
            console.log(`Applied syntax highlighting with language: ${prismLanguage}`);
        }
    } else if (codeExampleSection) {
        codeExampleSection.classList.add('hidden');
    }
    
    // Make sure the result is visible
    if (translationContent) {
        translationContent.scrollIntoView({ behavior: 'smooth' });
    }
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
        case 'java':
            return 'java';
        case 'ruby':
            return 'ruby';
        default:
            return 'none';
    }
}

/**
 * Show or hide the loading overlay
 * @param {boolean} show - Whether to show the loading overlay
 */
function showLoading(show) {
    const loadingOverlay = document.getElementById('loading-overlay');
    if (loadingOverlay) {
        loadingOverlay.style.display = show ? 'flex' : 'none';
    } else {
        console.error('Loading overlay element not found!');
    }
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

/**
 * Diagnose potential issues with the application
 */
function diagnoseAppIssues() {
    console.log('Running app diagnostics...');
    
    // Check essential DOM elements
    const elements = {
        'error-message': document.getElementById('error-message'),
        'language-input': document.getElementById('language-input'),
        'translate-btn': document.getElementById('translate-btn'),
        'translation-result': document.getElementById('translation-result'),
        'result-placeholder': document.getElementById('result-placeholder'),
        'loading-overlay': document.getElementById('loading-overlay'),
        'help-btn': document.getElementById('help-btn'),
        'help-modal': document.getElementById('help-modal'),
        'theme-toggle': document.getElementById('theme-toggle')
    };
    
    let hasIssues = false;
    
    // Log status of all elements
    for (const [id, element] of Object.entries(elements)) {
        if (!element) {
            console.error(`MISSING ELEMENT: ${id} not found in the DOM`);
            hasIssues = true;
        } else {
            console.log(`✓ Found element: ${id}`);
        }
    }
    
    // Fix the translate button if it exists
    if (elements['translate-btn']) {
        // Force add both event listeners and attributes
        elements['translate-btn'].addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Translate button clicked via event listener');
            translateError();
        });
        
        elements['translate-btn'].onclick = function(e) {
            e.preventDefault();
            console.log('Translate button clicked via onclick property');
            translateError();
            return false;
        };
        
        console.log('Fixed translate button event handlers');
    }
    
    if (hasIssues) {
        console.warn('Application has some missing elements. Some features may not work properly.');
    } else {
        console.log('All essential elements found. App should function correctly.');
    }
    
    // Return elements object for further use
    return elements;
}

// Initialize the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    
    // Initialize the application
    initApp();
    
    // Run diagnostics
    const elements = diagnoseAppIssues();
    
    // Double-check translate button specifically
    const translateBtn = document.getElementById('translate-btn');
    if (translateBtn) {
        console.log('Found translate button, ensuring event listeners are attached');
        translateBtn.addEventListener('click', translateError);
        
        // Add a backup direct onclick handler
        translateBtn.setAttribute('onclick', 'translateError(); return false;');
        
        // Ensure the button is visible and clickable
        translateBtn.style.pointerEvents = 'auto';
        translateBtn.style.cursor = 'pointer';
        translateBtn.disabled = false;
        
        console.log('Translate button ready for use');
    } else {
        console.error('Translate button not found!');
    }

    // Explicitly add event listeners for the help button and theme toggle again
    // This ensures they work even if there were issues during initApp()
    const helpBtn = document.getElementById('help-btn');
    const modal = document.getElementById('help-modal');
    const modalClose = document.querySelector('.modal-close');
    const themeToggle = document.getElementById('theme-toggle');
    
    console.log('Help button found:', !!helpBtn);
    console.log('Modal found:', !!modal);
    console.log('Theme toggle found:', !!themeToggle);
    
    if (helpBtn && modal) {
        helpBtn.addEventListener('click', function() {
            console.log('How It Works button clicked (direct)');
            modal.classList.add('show');
            // Ensure the modal is visible by forcing display style
            modal.style.display = 'flex';
        });
        
        if (modalClose) {
            modalClose.addEventListener('click', function() {
                console.log('Modal close clicked');
                modal.classList.remove('show');
                // Ensure the modal is hidden
                setTimeout(() => modal.style.display = 'none', 50);
            });
        }
        
        // Also close when clicked outside
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                console.log('Clicked outside modal');
                modal.classList.remove('show');
                // Ensure the modal is hidden
                setTimeout(() => modal.style.display = 'none', 50);
            }
        });
    }
    
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            console.log('Theme toggle clicked (direct)');
            // Get current theme
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
            console.log('Current theme:', currentTheme);
            
            // Toggle theme
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            console.log('New theme:', newTheme);
            
            // Update DOM and save preference
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem(THEME_STORAGE_KEY, newTheme);
            
            // Update theme icon
            updateThemeIcon(newTheme);
            
            // Update Prism theme if syntax highlighting is present
            updateCodeTheme(newTheme);
        });
    }
});

/**
 * Clear all recent searches (for testing purposes)
 */
function clearRecentSearches() {
    localStorage.removeItem('recentSearches');
    loadRecentSearches();
    console.log('Recent searches cleared');
}

/**
 * Improve accessibility by managing focus and keyboard navigation
 * @param {HTMLElement} element - The element to focus
 */
function focusElement(element) {
    if (!element) return;
    
    // Set focus to the element
    element.focus();
    
    // Ensure it has proper tabindex if it's not naturally focusable
    if (!['a', 'button', 'input', 'select', 'textarea'].includes(element.tagName.toLowerCase())) {
        if (!element.hasAttribute('tabindex')) {
            element.setAttribute('tabindex', '-1');
        }
    }
    
    // Announce to screen readers via aria-live region
    const announcer = document.getElementById('a11y-announcer');
    if (announcer) {
        announcer.textContent = `Focused on ${element.getAttribute('aria-label') || element.textContent || 'element'}`;
    }
    
    console.log('Focused element:', element);
}

// Add keyboard shortcuts for common actions
document.addEventListener('keydown', function(event) {
    // Alt+T for translate (Windows/Linux) or Option+T (Mac)
    if ((event.altKey || event.metaKey) && event.key === 't') {
        event.preventDefault();
        translateError();
    }
    
    // Alt+C for clear (Windows/Linux) or Option+C (Mac)
    if ((event.altKey || event.metaKey) && event.key === 'c') {
        event.preventDefault();
        clearInput();
    }
    
    // Escape key closes any modal or overlay
    if (event.key === 'Escape') {
        const loadingOverlay = document.getElementById('loading-overlay');
        if (loadingOverlay && loadingOverlay.style.display === 'flex') {
            showLoading(false);
        }
    }
});
