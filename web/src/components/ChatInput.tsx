import React, { useState } from 'react';
import { Input, Button, message, Card } from 'antd';
import { chat } from '../api/chat';
import { applyLeave } from '../api/applyLeave';
import type { ApplyLeaveChatResponse } from '../types/AppllyLeave';

const ChatInput: React.FC = () => {
  const defaultText = '明天是2025年8月1日，帮我请个天的假，理由是因为要去参加一个重要的家庭聚会。';
  const [inputValue, setInputValue] = useState(defaultText);
  const [responseData, setResponseData] = useState('nothing'); // 用于存储响应数据

  const handleSend = async () => {
    if (inputValue.trim()) {
      try {
        const response: unknown = await chat(inputValue);

        setResponseData(JSON.stringify(response)); // 存储响应数据
        applyLeave(response as ApplyLeaveChatResponse)
        message.success('请求发送成功');
        console.log('请求响应:', response);
      } catch (error) {
        console.error('请求出错:', error);
        message.error('请求发送失败，请稍后重试');
      }
      setInputValue('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div>
      <Input.TextArea
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={handleKeyPress}
        rows={4}
        placeholder="请输入内容"
        style={{ marginBottom: 10 }}
      />
      <Button type="primary" onClick={handleSend}>发送</Button>
      <Card title="响应数据" style={{ marginTop: 16 }}>
        <pre>{responseData}</pre>
      </Card>
    </div>
  );
};

export default ChatInput;