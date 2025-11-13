import tkinter as tk
from tkinter import ttk
import webbrowser
import url_shortener
import gui_utils
import menu_utils
from constants import *

# ==========================
#  Functional Definitions
# ==========================

def shorten(event=None):
    """Shorten the entered URL."""
    url = longurl_entry.get().strip()
    if not url:
        gui_utils.show_error_message("Error", "Please enter a URL.")
        return

    try:
        short_url = url_shortener.shorten_url(url)
        if short_url:
            shorturl_entry.delete(0, tk.END)
            shorturl_entry.insert(0, short_url)
    except Exception as e:
        gui_utils.show_error_message("Error", f"An error occurred: {e}")


def copy_url():
    """Copy shortened URL to clipboard."""
    shortened_url = shorturl_entry.get().strip()
    if shortened_url:
        root.clipboard_clear()
        root.clipboard_append(shortened_url)
        root.update()
        gui_utils.show_info_message("Success", "Shortened URL copied to clipboard.")
    else:
        gui_utils.show_warning_message("Warning", "No shortened URL found.")


def clear_entries():
    """Clear both URL input fields."""
    longurl_entry.delete(0, tk.END)
    shorturl_entry.delete(0, tk.END)


def about():
    """Display About dialog."""
    current_date = "15.05.2024"
    gui_utils.show_info_message(
        "About",
        f"{APP_NAME}\nVersion: {APP_VERSION}\nAuthor: {AUTHOR}\nLast Update: {current_date}",
    )


def open_readme():
    """Open the README file in GitHub."""
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/URL-shortener/blob/main/README.md"
    )


def welcome():
    """Open the project welcome page."""
    menu_utils.open_url_in_browser("https://github.com/storlak/URL-shortener")


def open_license():
    """Open the License file in GitHub."""
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/URL-shortener/blob/main/LICENSE"
    )


def quick_commands():
    """Display available keyboard shortcuts."""
    gui_utils.show_info_message(
        "Keyboard Shortcuts",
        f"Shorten URL: {SHORTEN_URL}\n"
        f"Copy Shortened URL: {COPY_URL}\n"
        f"Clear Clipboard: {CLEAR_URL}\n"
        f"Help: {HELP}",
    )


def help_section(event=None):
    """Open the Help page in browser."""
    menu_utils.open_url_in_browser(
        "https://github.com/storlak/URL-shortener/discussions"
    )


# ==========================
#  GUI Setup
# ==========================

root = tk.Tk()
root.title(APP_NAME)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg=BACKGROUND_COLOR)

# ==========================
#  Menu Bar
# ==========================

menubar = tk.Menu(root)
root.config(menu=menubar)

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Shorten URL", command=shorten, accelerator="Alt+S")
edit_menu.add_command(label="Copy Short URL", command=copy_url, accelerator="Alt+C")
edit_menu.add_command(label="Clear URL", command=clear_entries, accelerator="Alt+L")
menubar.add_cascade(label="Edit", menu=edit_menu)

# Tools Menu
tools_menu = tk.Menu(menubar, tearoff=0)
tools_menu.add_command(label="Quick Commands", command=quick_commands)
tools_menu.add_separator()
tools_menu.add_command(label="History")  # placeholder
menubar.add_cascade(label="Tools", menu=tools_menu)

# Help Menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Welcome", command=welcome)
help_menu.add_command(label="Help", command=help_section, accelerator="F1")
help_menu.add_command(label="Documentation", command=open_readme)
help_menu.add_separator()
help_menu.add_command(label="View Licence", command=open_license)
help_menu.add_separator()
help_menu.add_command(label="About URL Shortener", command=about)
menubar.add_cascade(label="Help", menu=help_menu)

# ==========================
#  Keyboard Shortcuts
# ==========================
root.bind("<Alt-s>", shorten)
root.bind("<Alt-c>", lambda e: copy_url())
root.bind("<Alt-l>", lambda e: clear_entries())
root.bind("<F1>", help_section)

# ==========================
#  Widgets
# ==========================

longurl_label = tk.Label(root, text="Enter a Long URL to Shorten", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
longurl_entry = tk.Entry(root, width=40)

shorten_button = tk.Button(root, text="Shorten URL", fg="black", bg="Turquoise", command=shorten)

separator = ttk.Separator(root, orient="horizontal")

shorturl_label = tk.Label(root, text="Shortened URL", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
shorturl_entry = tk.Entry(root, width=40)

copyurl_button = tk.Button(root, text="Copy", fg="black", bg="Turquoise", command=copy_url)

clear_button = tk.Button(root, text="Clear Clipboard", fg="black", bg="Turquoise", command=clear_entries)

bot_label = tk.Label(root, text=f"Version: {APP_VERSION} - {AUTHOR}", fg="black", bg="Turquoise")

# ==========================
#  Layout
# ==========================

widgets = [
    (longurl_label, {"pady": 5}),
    (longurl_entry, {}),
    (shorten_button, {"pady": 5}),
    (separator, {"fill": "x", "padx": 5, "pady": 5}),
    (shorturl_label, {"pady": 5}),
    (shorturl_entry, {}),
    (copyurl_button, {"pady": 5}),
    (clear_button, {"pady": 5}),
    (bot_label, {"side": "bottom", "fill": "x"})
]

for widget, opts in widgets:
    widget.pack(**opts)

# ==========================
#  Mainloop
# ==========================
root.mainloop()
