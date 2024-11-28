import React from 'react';
import UploadForm from './components/UploadForm';
import QuestionForm from './components/QuestionForm';

function App() {
  return (
    <div>
      <h1>PDF Question App</h1> {/* Removed the space before the closing tag */}
      <UploadForm />
      <QuestionForm />
    </div>
  );
}

export default App;