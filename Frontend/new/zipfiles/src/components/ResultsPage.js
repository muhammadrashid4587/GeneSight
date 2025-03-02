// src/components/ResultsPage.js
import React from 'react';
import './styles.css';

function ResultsPage({ file }) {
  return (
    <div className="container">
      <h1>Here's what we found:</h1>
      <p>{file ? `Uploaded File: ${file.name}` : 'No file uploaded.'}</p>
    </div>
  );
}

export default ResultsPage;
