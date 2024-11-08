from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

def get_responses(user_input):
    user_input = user_input.lower()

    # Dictionary that has IT-related keywords linked together with specific responses.
    responses = {
        ("reset", "password", "login", "account"): (
            "If you want to reset your password, click on 'Forgot Password' on the login screen and follow the steps provided. "
            "If this does not work, contact an IT specialist to help you with the issue."
        ),
        ("wifi", "connect", "internet", "network"): (
            "To troubleshoot Wi-Fi, make sure Wi-Fi is enabled on your device, and check if other devices can connect. "
            "If this does not resolve the issue, restart your router. If it still doesn't work, contact an IT specialist for assistance."
        ),
        ("software", "install", "download", "application"): (
            "If you need to install software, first check that you have the necessary permissions on your device. "
            "If you encounter any errors or lack permission, reach out to an IT specialist for further assistance."
        ),
        ("slow", "performance", "lag", "freeze"): (
            "If your computer is running slow, try restarting your device and closing any unnecessary applications. "
            "If performance doesn’t improve, consider reaching out to an IT specialist for a more detailed analysis."
        ),
        ("email", "outlook", "inbox", "send"): (
            "To troubleshoot email issues, check your internet connection and confirm you’re using the correct login credentials. "
            "If the issue persists, restart your email application. If it still doesn't work, contact an IT specialist for help."
        ),
        ("printer", "print", "scanner", "scan"): (
            "If you’re having trouble with printing or scanning, check that the printer is powered on and connected to your device. "
            "If the problem continues, restart both the printer and your computer. For further assistance, contact an IT specialist."
        ),
        ("vpn", "remote access", "work from home"): (
            "If you're having trouble with VPN, ensure you have the correct credentials and that the VPN client is properly installed. "
            "If you’re still unable to connect, contact an IT specialist for configuration support."
        ),
        ("backup", "restore", "lost files", "recover"): (
            "To recover lost files, check if you have backups stored in cloud storage or on an external drive. "
            "If the files aren’t there, contact an IT specialist for assistance with advanced recovery options."
        ),
        ("backup", "restore", "lost files", "recover"): (
            "To recover lost files, check if you have backups stored in cloud storage or on an external drive. "
            "If the files aren’t there, contact an IT specialist for assistance with advanced recovery options."
        ),
        ("hello","hi","hey","whatsup"): (            
            "Hi there, if you have any questions or queries, I'm here to help!"
        ),
    }

    # For Loop, that loops through each set of keywords and check if any are in the user's input
    for keywords, response in responses.items():
        if any(keyword in user_input for keyword in keywords):
            return response

    # Automatic response if none of the keywords are matched
    return (
        "I'm here to help with IT questions! Could you describe your issue in more detail? "
        "If it's about internet, software, password resets, or something else, just let me know."
    )



@app.route('/')
def index():
    return render_template('chatbot.html')

# Handle the AJAX request
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question'].lower()
    response = get_responses(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)
