document.querySelector('.chat-input button').addEventListener('click', async function() {
    const inputField = document.querySelector('.chat-input input');
    const userMessage = inputField.value;
    const messageId = document.getElementById('message_id').value; 

    if (userMessage.trim() !== "") {

        // Hiển thị tin nhắn người dùng lên UI
        const userMessageDiv = document.createElement('div');
        userMessageDiv.classList.add('chat-message', 'user-message');
        userMessageDiv.textContent = userMessage;
        document.querySelector('.chat-messages').appendChild(userMessageDiv);

        // Gửi yêu cầu đến backend Flask
        const response = await fetch('/api/ai_models/handle_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                input_data: userMessage,
                message_id: messageId
            })
        });


        const data = await response.json();

        const botMessageDiv = document.createElement('div');
        botMessageDiv.classList.add('chat-message', 'bot-message');

        botMessageDiv.innerHTML = marked.parse(data.prediction || "Sorry, I didn't understand that.");
        document.querySelector('.chat-messages').appendChild(botMessageDiv);

        window.location.reload(); 


        document.querySelector('.chat-messages').scrollTop = document.querySelector('.chat-messages').scrollHeight;



        inputField.value = '';
        inputField.focus();
    }
});

window.onload = function() {
    const chatMessages = document.querySelector('.chat-messages');
    const lastMessage = chatMessages.lastElementChild; 

    if (lastMessage) {
        lastMessage.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
};






