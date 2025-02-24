function appendMessage(message, fromUser = false) {
  const chatBox = document.getElementById("chat-box");
  const messageElement = document.createElement("div");
  messageElement.classList.add(fromUser ? "user-message" : "aurora-message");
  messageElement.textContent = message;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const userInput = document.getElementById("user-input");
  const message = userInput.value.trim();

  if (message) {
    appendMessage(message, true); // Enviar mensagem do usuário
    userInput.value = "";

    // Enviar mensagem para a API da Aurora
    try {
      const response = await fetch("http://127.0.0.1:10000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ pergunta: message }),
      });

      if (response.ok) {
        const data = await response.json();
        appendMessage(data.resposta); // Exibir a resposta da Aurora
      } else {
        appendMessage("Erro ao comunicar com a Aurora. Tente novamente.");
      }
    } catch (error) {
      appendMessage("Erro de conexão. Tente novamente.");
    }
  }
}
