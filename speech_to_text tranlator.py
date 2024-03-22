import tkinter as tk
from tkinter import ttk
import threading
import speech_recognition as sr
# Language codes for different languages
language_codes = {
    'Telugu': 'te-IN',
    'Tamil': 'ta-IN',
    'English': 'en-US',
    'Hindi': 'hi-IN',
    'Kannada': 'kn-IN',
    'Malayalam': 'ml-IN'
}


def perform_speech_to_text():
    language = language_codes[language_var.get()]

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Please speak something...")
        audio_data = recognizer.listen(source)

    try:
        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio_data, language=language)
        result_text.set("You said: " + text)
    except sr.UnknownValueError:
        result_text.set("Could not understand audio")
    except sr.RequestError as e:
        result_text.set("Could not request results; {0}".format(e))


def speech_to_text():
    # Run speech-to-text in a separate thread to keep the GUI responsive
    threading.Thread(target=perform_speech_to_text).start()


# GUI setup
root = tk.Tk()
root.title("Speech to Text Translator")
root.geometry("500x500")  # Set window size

# Set the background color to sky blue
root.configure(bg='green')

# Create a style
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14), background='sky blue')
style.configure('TButton', font=('Arial', 14))

# Language selection dropdown
ttk.Label(root, text="Select Language:", style='TLabel').pack(pady=10)
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=list(language_codes.keys()),
                                 font=('Arial', 12))
language_dropdown.pack(pady=10)
language_dropdown.set('English')

# Result label
result_text = tk.StringVar()
ttk.Label(root, textvariable=result_text, style='TLabel').pack(pady=10)

# Button to trigger speech-to-text conversion
convert_button = ttk.Button(root, text="Convert", command=speech_to_text, style='TButton')
convert_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()


