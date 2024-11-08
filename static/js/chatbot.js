// Form submission
document.getElementById('chatForm').addEventListener('submit', function(e) {
    e.preventDefault();  

    // Obtain the user's input
    let question = document.getElementById('question').value; 
    document.getElementById('question').value = '';  // Clear the input field after capturing the value

    // Create a user chat bubble and append it to the chat window
    let userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble user-bubble';
    userBubble.innerHTML = question;
    document.getElementById('response').appendChild(userBubble);

    // Show typing indicator
    document.getElementById('typing-indicator').style.display = 'block';

    // Send the user's question to the server
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'question=' + encodeURIComponent(question)
    })
    .then(response => {
        if (!response.ok) {
            return Promise.reject('Request failed');
        }
        return response.text();
    })
    .then(data => {
        // Hide the typing indicator when the response is ready
        document.getElementById('typing-indicator').style.display = 'none';

        // Create a bot chat bubble for the response
        let botBubble = document.createElement('div');
        botBubble.className = 'chat-bubble bot-bubble';
        botBubble.innerHTML = data;

        // Append the bot's response to the chat window
        document.getElementById('response').appendChild(botBubble);

        // Scroll to the bottom of the chat to show the latest message
        document.getElementById('response').scrollTop = document.getElementById('response').scrollHeight;
    })
    .catch(error => {
        // If there's an error, display an error message.
        document.getElementById('response').innerHTML += 
            '<div class="alert alert-danger">There was an error: ' + error + '</div>';
    });
});
