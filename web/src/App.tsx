import React from 'react';
import ChatInput from './components/ChatInput';
import 'antd/dist/reset.css';

const App: React.FC = () => {
  return (
    <div style={{ padding: 20 }}>
      <h1>聊天输入</h1>
      <ChatInput />
    </div>
  );
};

export default App;
