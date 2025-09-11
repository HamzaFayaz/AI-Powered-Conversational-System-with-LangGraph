import { API_BASE_URL } from '../utils/constants';

class ApiService {
  async uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await fetch(`${API_BASE_URL}/api/upload-file`, {
      method: 'POST',
      body: formData,
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Upload failed');
    }
    
    return response.json();
  }
  
  async sendMessage(message, chatbotId, threadId = null) {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message,
        chatbot_id: chatbotId,
        thread_id: threadId,
      }),
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Chat request failed');
    }
    
    return response.json();
  }
  
  async getChatbotInfo(chatbotId) {
    const response = await fetch(`${API_BASE_URL}/api/chatbot/${chatbotId}`);
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to get chatbot info');
    }
    
    return response.json();
  }
  
  async checkHealth() {
    const response = await fetch(`${API_BASE_URL}/health/`);
    return response.json();
  }
}

export default new ApiService();