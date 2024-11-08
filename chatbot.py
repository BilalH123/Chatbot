from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

def get_responses(user_input):
    user_input = user_input.lower()

    # Dictionary that has IT-related keywords linked together with specific responses.
    responses = {
    ("reset", "password", "login", "account"): (
        "To reset your password, simply click on 'Forgot Password' on the login screen and follow the instructions provided. "
        "If you continue to encounter issues, please reach out to an IT specialist for further assistance."
    ),
    ("wifi", "connect", "internet", "network"): (
        "To resolve Wi-Fi connection issues, ensure that Wi-Fi is enabled on your device and verify if other devices can connect. "
        "If the problem persists, try restarting your router. Should the issue continue, contact an IT specialist for support."
    ),
    ("software", "install", "download", "application"): (
        "If you're trying to install software, first confirm that you have the necessary permissions on your device. "
        "In case of errors or permission issues, please get in touch with an IT specialist for further help."
    ),
    ("slow", "performance", "lag", "freeze"): (
        "If your computer is running slowly, try restarting it and closing unnecessary applications. "
        "If performance does not improve, an IT specialist can help with a more in-depth analysis."
    ),
    ("email", "outlook", "inbox", "send"): (
        "For email troubleshooting, check your internet connection and make sure you're using the correct login credentials. "
        "If problems persist, try restarting your email application. If you're still having issues, an IT specialist can assist you."
    ),
    ("printer", "print", "scanner", "scan"): (
        "If you're having issues with printing or scanning, ensure the printer is powered on and properly connected to your device. "
        "If the problem remains, restart both the printer and your computer. For further assistance, please contact an IT specialist."
    ),
    ("vpn", "remote access", "work from home"): (
        "If you're experiencing VPN issues, verify that you have the correct credentials and that the VPN client is properly installed. "
        "If the problem persists, contact an IT specialist for configuration support."
    ),
    ("backup", "restore", "lost files", "recover"): (
        "To recover lost files, check if you have backups stored in cloud storage or on an external drive. "
        "If the files aren’t there, contact an IT specialist for assistance with advanced recovery options."
    ),
    ("hello", "hi", "hey", "whatsup"): (
        "Hi there! How can I assist you today? Feel free to ask any questions or share the issue you're facing."
    ),
    ("bluetooth", "pair", "connect", "device"): (
        "To connect a Bluetooth device, make sure Bluetooth is enabled on both the device and your computer. "
        "Ensure the device is in pairing mode and try reconnecting. If you continue to face issues, contact an IT specialist for help."
    ),
    ("camera", "webcam", "video", "picture"): (
        "If your camera isn't working, first check if it's enabled in your system settings. "
        "If it still doesn’t work, restart your computer or try updating the camera drivers. For further assistance, contact an IT specialist."
    ),
    ("storage", "space", "disk", "full"): (
        "If you're running out of storage, try deleting unnecessary files or moving them to an external drive or cloud storage. "
        "You can also check your system settings to see which files are taking up the most space. If you need help managing your storage, feel free to ask."
    ),
    ("update", "upgrade", "software", "patch"): (
        "To update your software, open the application and check for the 'Update' option in the settings or help menu. "
        "If the update doesn’t work or you encounter any errors, contact an IT specialist for assistance."
    ),
    ("security", "virus", "malware", "scan"): (
        "If you suspect a virus or malware, run a full system scan using your antivirus software. "
        "Ensure your antivirus is up to date and follow any recommended actions. If you need help with the scan, please reach out to an IT specialist."
    ),
    ("performance", "speed", "optimization", "boost"): (
        "To optimize your system's performance, consider closing unnecessary programs, clearing your browser cache, and disabling startup items. "
        "If your computer continues to lag, it might benefit from a professional tune-up or an upgrade to hardware."
    ),
    ("files", "lost", "missing", "recover"): (
        "If you’ve lost files, check your Recycle Bin or trash folder to see if they can be restored. "
        "If you’ve backed up your files, you can restore them from your backup. For further recovery options, contact an IT specialist."
    ),
    ("video", "playback", "audio", "sound"): (
        "If you're having trouble with video playback or no sound, check that your audio settings are correct and that the volume is turned up. "
        "You can also try restarting the video player or your computer. If the issue persists, contact an IT specialist for further help."
    ),
    ("remote", "desktop", "connection", "server"): (
        "If you're having trouble with remote desktop or server connection, ensure that you're using the correct server address and credentials. "
        "Make sure the server is online and your firewall settings allow the connection. If you still can't connect, reach out to an IT specialist."
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
