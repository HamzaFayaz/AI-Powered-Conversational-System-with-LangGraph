export const API_BASE_URL = process.env.REACT_APP_API_URL || '';

export const FILE_TYPES = {
  ALLOWED: ['.pdf', '.txt'],
  MAX_SIZE: 10 * 1024 * 1024, // 10MB
};

export const MESSAGE_TYPES = {
  USER: 'user',
  BOT: 'bot',
  SYSTEM: 'system',
  ERROR: 'error',
};

export const PAGES = {
  UPLOAD: 'upload',
  CHAT: 'chat',
};