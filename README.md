# ✉️ Email Assistant

Interact with your email using voice commands with the Email Assistant Python script. This project utilizes the `smtplib`, `speech_recognition`, and `pyttsx3` libraries to enable voice-controlled email functionalities.

## Introduction

The Email Assistant project is a Python script that allows you to send emails using voice commands. It integrates with the `smtplib` library for email sending, `speech_recognition` for voice recognition, and `pyttsx3` for text-to-speech functionality.

## Features

- **Voice-Controlled Email:** Interact with your email using voice commands.
- **Dynamic Contacts:** Maintain a dynamic contact list for easy email sending.
- **Subject and Message Control:** Dictate the subject and message content for each email.
- **Speech Feedback:** Get audio feedback on your interactions with the assistant.

## Prerequisites

Ensure you have Python installed on your system.

## Installation

1. Clone the GitHub repository:

    ```bash
    git clone https://github.com/codeterrayt/EmailAssistant.git
    cd EmailAssistant
    ```

2. Install the required libraries:

    ```bash
    pip install smtplib email message speech_recognition pyttsx3
    ```

3. Open `main.py` in a text editor and configure the following variables:
    - `server_login_mail`: Your email address for SMTP login.
    - `server_login_password`: Your email password for SMTP login.
    - Update the `contact` dictionary with your contacts.

4. Save the changes.

5. Run the script:

    ```bash
    python main.py
    ```

6. The assistant will greet you, and you can start giving voice commands.

## Usage

1. The assistant will prompt you with "Listening..." indicating it's ready to receive voice commands.

2. Speak your command, e.g., "Assistant, write an email."

3. The assistant will guide you through the process of specifying the recipient, subject, and message.

4. The email will be sent, and the assistant will provide audio feedback.

## Development

Feel free to explore and modify the code to suit your specific needs. Customize the contact list, improve voice command handling, or add additional features.

## Acknowledgments

This project utilizes the `smtplib`, `speech_recognition`, and `pyttsx3` libraries. Explore the [smtplib Documentation](https://docs.python.org/3/library/smtplib.html), [speech_recognition Documentation](https://pypi.org/project/SpeechRecognition/), and [pyttsx3 Documentation](https://pypi.org/project/pyttsx3/) for more information.

📢 Happy Emailing with Voice Commands! 🎤
