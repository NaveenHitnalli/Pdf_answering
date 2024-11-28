import React, { useState } from 'react';
import axios from 'axios';

const QuestionForm = () => {
  const [question, setQuestion] = useState('');
  const [documentId, setDocumentId] = useState('');
  const [answer, setAnswer] = useState('');

  const handleAskQuestion = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/ask/', {
        question,
        document_id: documentId,
      });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error asking question:', error);
      alert('Error asking question');
    }
  };

  return (
    <form onSubmit={handleAskQuestion}>
      <input
        type="text"
        placeholder="Enter your question"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        required
      />
      <input
        type="number"
        placeholder="Document ID"
        value={documentId}
        onChange={(e) => setDocumentId(e.target.value)}
        required
      />
      <button type="submit">Ask Question</button>
      {answer && <p>Answer: {answer}</p>}
    </form>
  );
};

export default QuestionForm;