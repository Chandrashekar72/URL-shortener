import pyshorteners
import tkinter.messagebox as messagebox
import logging

# Configure basic logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def shorten_url(url: str) -> str | None:
    """
    Shortens a given URL using TinyURL via pyshorteners.

    Args:
        url (str): The original long URL.

    Returns:
        str | None: The shortened URL if successful, None otherwise.
    """
    if not url.strip():
        messagebox.showwarning("Warning", "Please enter a URL.")
        return None

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        return short_url

    except pyshorteners.exceptions.ShorteningErrorException as e:
        logging.error(f"ShorteningErrorException: {e}")
        messagebox.showerror(
            "Error",
            "Invalid URL. Please enter a valid URL to shorten.",
        )
    except pyshorteners.exceptions.ServiceException as e:
        logging.error(f"ServiceException: {e}")
        messagebox.showerror(
            "Error",
            "URL shortening service is currently unavailable. Please try again later.",
        )
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        messagebox.showerror(
            "Error",
            f"An unexpected error occurred: {str(e)}",
        )
    return None
