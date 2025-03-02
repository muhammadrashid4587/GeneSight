// src/components/UploadPage.js
import React from 'react';
import './styles.css';

function UploadPage({ onFileUpload }) {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      onFileUpload(file);  // Upload the file to App.js state
    }
  };

  return (
    <div className="container">
      <h1>Upload Files Here</h1>
      <input type="file" onChange={handleFileChange} />
    </div>
  );
}

export default UploadPage;
