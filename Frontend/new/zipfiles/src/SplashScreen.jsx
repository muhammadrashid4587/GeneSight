// SplashScreen.jsx
import React from 'react';
import './styles.css';

function SplashScreen() {
  return (
    <div className="splash-container">
      <h1 className="splash-title">GeneSight</h1>
      <p className="splash-subtitle">AI-driven Genomic Classifier</p>
      <div className="splash-loader" />
    </div>
  );
}

export default SplashScreen;
