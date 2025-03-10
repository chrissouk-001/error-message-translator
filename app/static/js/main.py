"""
Python wrapper for JavaScript functions to make testing possible.
This module provides Python implementations of JavaScript functions in main.js
for testing purposes only.
"""


def getPrismLanguageClass(language):
    """
    Python implementation of the JavaScript getPrismLanguageClass function.

    Args:
        language (str): The language to get the Prism class for

    Returns:
        str: The corresponding Prism language class
    """
    language_map = {
        "python": "language-python",
        "javascript": "language-javascript",
        "html": "language-markup",
        "css": "language-css",
        "java": "language-java",
    }
    return language_map.get(language, "language-none")


def createShareButton(document, translationHeader):
    """
    Python implementation of the JavaScript createShareButton function.

    Args:
        document: Mock document object with createElement and getElementById methods
        translationHeader: The translation header element to add the button to

    Returns:
        None
    """
    if not translationHeader:
        return

    # Create a container for the share button that will float right
    shareContainer = document.createElement("div")
    shareContainer.className = "share-container"
    shareContainer.style["marginLeft"] = "auto"

    # Create the share button
    shareButton = document.createElement("button")
    shareButton.className = "share-btn"
    shareButton.innerHTML = '<i class="fas fa-share-alt"></i> Share'
    shareButton.title = "Share this error translation"
    shareButton.addEventListener("click", lambda: None)  # Mock click handler

    # Add the button to the container
    shareContainer.appendChild(shareButton)

    # Add the container to the translation header before the language badge
    translationHeader.insertBefore(shareContainer, document.getElementById("language-badge"))


def shareTranslation(errorInput, languageSelect, window, URL):
    """
    Python implementation of the JavaScript shareTranslation function.

    Args:
        errorInput: Mock input element with error message
        languageSelect: Mock select element with language value
        window: Mock window object with location
        URL: Mock URL constructor

    Returns:
        str: The generated share URL
    """
    errorMessage = (
        errorInput.value.strip() if hasattr(errorInput.value, "strip") else errorInput.value
    )
    if not errorMessage:
        return None

    # Create a URL with the error message and language
    language = languageSelect.value
    url = URL(window.location.href)

    # Set error parameter (in a real app this would be URL encoded)
    url.searchParams.set("error", errorMessage)

    if language != "auto":
        url.searchParams.set("lang", language)
    else:
        url.searchParams.delete("lang")

    # Create a shareable link
    shareableUrl = url.toString()
    return shareableUrl


def copyShareLinkToClipboard(url):
    """
    Python implementation of the JavaScript copyShareLinkToClipboard function.

    Args:
        url (str): The URL to copy to clipboard

    Returns:
        bool: Whether the operation was successful
    """
    # In a real app, this would use the clipboard API
    # For testing, we just return True
    return True
