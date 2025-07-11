import React, { useState } from 'react';

const ChatWindow: React.FC = () => {
  // 用于存储用户输入的消息
  const [inputMessage, setInputMessage] = useState('');
  // 用于存储聊天消息列表
  const [messages, setMessages] = useState<string[]>([]);

  // 处理输入框内容变化
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputMessage(e.target.value);
  };

  // 处理提交消息
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputMessage.trim()) {
      setMessages([...messages, inputMessage]);
      setInputMessage('');
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', fontFamily: 'Arial, sans-serif' }}>
      <div style={{ height: '400px', border: '1px solid #ccc', overflowY: 'auto', padding: '10px', marginBottom: '10px' }}>
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: '8px' }}>
            {msg}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputMessage}
          onChange={handleInputChange}
          placeholder="请输入消息..."
          style={{ width: '80%', padding: '8px', boxSizing: 'border-box' }}
        />
        <button type="submit" style={{ width: '18%', padding: '8px', marginLeft: '2%' }}>
          发送
        </button>
      </form>
    </div>
  );
};

const App: React.FC = () => {
  return <ChatWindow />;
};

export default App;
