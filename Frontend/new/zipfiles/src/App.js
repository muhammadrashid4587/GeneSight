// // // // App.js
// // // import React, { useState, useEffect } from 'react';
// // // import SplashScreen from './SplashScreen';
// // // import './styles.css';

// // // // Import your video from the assets folder
// // // import dnaVideo from './assets/dnaHologram.mp4';

// // // function App() {
// // //   // 1) Splash screen states
// // //   const [showSplash, setShowSplash] = useState(true);
// // //   const [fadeClass, setFadeClass] = useState('');

// // //   // 2) Page state (upload or results)
// // //   const [page, setPage] = useState('upload');

// // //   // Splash screen fade-out effect
// // //   useEffect(() => {
// // //     const timer = setTimeout(() => {
// // //       setFadeClass('fade-out');
// // //       setTimeout(() => {
// // //         setShowSplash(false);
// // //       }, 1000);
// // //     }, 3000);

// // //     return () => clearTimeout(timer);
// // //   }, []);

// // //   // Switch to 'results' page after file upload
// // //   const handleUpload = () => {
// // //     setPage('results');
// // //   };

// // //   return (
// // //     <div className="App">
// // //       {/* SPLASH SCREEN */}
// // //       {showSplash ? (
// // //         <div className={`splash-wrapper ${fadeClass}`}>
// // //           <SplashScreen />
// // //         </div>
// // //       ) : (
// // //         /* MAIN MENU PAGE */
// // //         <div className="main-menu">
// // //           <h1 className="main-title">GENESIGHT</h1>
// // //           <h2 className="subtitle">Upload Your Gene Expression Data</h2>
// // //           <p className="description">
// // //             Get a quick and explainable risk assessment for disease prediction.
// // //           </p>

// // //           {/* HOLOGRAM SECTION */}
// // //           <div className="hologram-container">
// // //             <video
// // //               autoPlay
// // //               loop
// // //               muted
// // //               playsInline
// // //               className="hologram-video"
// // //             >
// // //               <source src={dnaVideo} type="video/mp4" />
// // //               {/* Fallback text if video can't be played */}
// // //               Your browser does not support the video tag.
// // //             </video>
// // //           </div>

// // //           {/* CONTENT: either upload form or results */}
// // //           {page === 'upload' ? (
// // //             <div className="upload-section">
// // //               {/* "Select File" label as a clickable area for input */}
// // //               <label htmlFor="file-upload" className="file-label">
// // //                 Select File
// // //               </label>
// // //               <input
// // //                 id="file-upload"
// // //                 className="file-input"
// // //                 type="file"
// // //                 onChange={(e) =>
// // //                   console.log('File selected:', e.target.files[0])
// // //                 }
// // //               />
// // //               <button className="upload-button" onClick={handleUpload}>
// // //                 Upload Files Now
// // //               </button>
// // //             </div>
// // //           ) : (
// // //             <div className="results-section">
// // //               <h2>Analysis Results</h2>
// // //               <p>Your model predictions or data visualizations go here!</p>
// // //             </div>
// // //           )}
// // //         </div>
// // //       )}
// // //     </div>
// // //   );
// // // }

// // // export default App;


// // import React, { useState, useEffect } from 'react';
// // import SplashScreen from './SplashScreen';
// // import './styles.css';
// // import dnaVideo from './assets/dnaHologram.mp4';

// // function App() {
// //   // Splash screen and page states
// //   const [showSplash, setShowSplash] = useState(true);
// //   const [fadeClass, setFadeClass] = useState('');
// //   const [page, setPage] = useState('upload');

// //   // State to store the file selected by the user
// //   const [selectedFile, setSelectedFile] = useState(null);
// //   // State to store prediction results
// //   const [result, setResult] = useState(null);

// //   useEffect(() => {
// //     const timer = setTimeout(() => {
// //       setFadeClass('fade-out');
// //       setTimeout(() => {
// //         setShowSplash(false);
// //       }, 1000);
// //     }, 3000);
// //     return () => clearTimeout(timer);
// //   }, []);

// //   const handleFileChange = (e) => {
// //     if (e.target.files.length > 0) {
// //       setSelectedFile(e.target.files[0]);
// //     }
// //   };

// //   const handleUpload = async () => {
// //     if (!selectedFile) {
// //       alert("Please select a file first.");
// //       return;
// //     }
// //     // Create a FormData object and append the file
// //     const formData = new FormData();
// //     formData.append("file", selectedFile);

// //     try {
// //       const response = await fetch("http://127.0.0.1:8000/predict", {
// //         method: "POST",
// //         body: formData
// //       });
// //       const data = await response.json();
// //       console.log("Prediction result:", data);
// //       setResult(data);
// //       setPage("results");
// //     } catch (error) {
// //       console.error("Error uploading file:", error);
// //     }
// //   };

// //   return (
// //     <div className="App">
// //       {showSplash ? (
// //         <div className={`splash-wrapper ${fadeClass}`}>
// //           <SplashScreen />
// //         </div>
// //       ) : (
// //         <div className="main-menu">
// //           <h1 className="main-title">GENESIGHT</h1>
// //           <h2 className="subtitle">Upload Your Gene Expression Data</h2>
// //           <p className="description">
// //             Get a quick and explainable risk assessment for disease prediction.
// //           </p>

// //           {/* Hologram Section */}
// //           <div className="hologram-container">
// //             <video autoPlay loop muted playsInline className="hologram-video">
// //               <source src={dnaVideo} type="video/mp4" />
// //               Your browser does not support the video tag.
// //             </video>
// //           </div>

// //           {page === 'upload' ? (
// //             <div className="upload-section">
// //               <label htmlFor="file-upload" className="file-label">
// //                 Select File
// //               </label>
// //               <input
// //                 id="file-upload"
// //                 className="file-input"
// //                 type="file"
// //                 onChange={handleFileChange}
// //               />
// //               <button className="upload-button" onClick={handleUpload}>
// //                 Upload Files Now
// //               </button>
// //             </div>
// //           ) : (
// //             <div className="results-section">
// //               <h2>Analysis Results</h2>
// //               {result ? (
// //                 <>
// //                   <p>Risk Score: {result.riskScore}</p>
// //                   <ul>
// //                     {result.topFeatures.map((feat, idx) => (
// //                       <li key={idx}>
// //                         {feat.gene}: {feat.importance.toFixed(2)}
// //                       </li>
// //                     ))}
// //                   </ul>
// //                 </>
// //               ) : (
// //                 <p>No results available.</p>
// //               )}
// //             </div>
// //           )}
// //         </div>
// //       )}
// //     </div>
// //   );
// // }

// // export default App;


// import React, { useState, useEffect } from 'react';
// import SplashScreen from './SplashScreen';
// import './styles.css';
// import dnaVideo from './assets/dnaHologram.mp4';

// function App() {
//   // Splash screen and page states
//   const [showSplash, setShowSplash] = useState(true);
//   const [fadeClass, setFadeClass] = useState('');
//   const [page, setPage] = useState('upload');

//   // State to store the file selected by the user
//   const [selectedFile, setSelectedFile] = useState(null);
//   // State to store prediction results
//   const [result, setResult] = useState(null);
//   // Loading state
//   const [isLoading, setIsLoading] = useState(false);
//   // Error state
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     const timer = setTimeout(() => {
//       setFadeClass('fade-out');
//       setTimeout(() => {
//         setShowSplash(false);
//       }, 1000);
//     }, 3000);
//     return () => clearTimeout(timer);
//   }, []);

//   const handleFileChange = (e) => {
//     if (e.target.files.length > 0) {
//       setSelectedFile(e.target.files[0]);
//       setError(null); // Clear any previous errors
//     }
//   };

//   const handleUpload = async () => {
//     if (!selectedFile) {
//       setError("Please select a file first.");
//       return;
//     }
    
//     // Set loading state
//     setIsLoading(true);
//     setError(null);
    
//     // Create a FormData object and append the file
//     const formData = new FormData();
//     formData.append("file", selectedFile);

//     try {
//       // Make sure this URL matches your FastAPI server
//       const response = await fetch("http://127.0.0.1:8000/predict", {
//         method: "POST",
//         body: formData
//       });
      
//       if (!response.ok) {
//         throw new Error(`Server returned ${response.status}: ${response.statusText}`);
//       }
      
//       const data = await response.json();
//       console.log("Prediction result:", data);
      
//       // Make sure the data matches the expected format
//       if (data.riskScore === undefined || !Array.isArray(data.topFeatures)) {
//         throw new Error("Unexpected response format from server");
//       }
      
//       setResult(data);
//       setPage("results");
//     } catch (error) {
//       console.error("Error uploading file:", error);
//       setError(`Error: ${error.message || "Failed to process data"}`);
//     } finally {
//       setIsLoading(false);
//     }
//   };

//   // Function to determine risk level color
//   const getRiskColor = (score) => {
//     if (score >= 0.7) return "high-risk";
//     if (score >= 0.4) return "medium-risk";
//     return "low-risk";
//   };

//   // Go back to upload page
//   const handleBack = () => {
//     setPage('upload');
//     setResult(null);
//     setSelectedFile(null);
//   };

//   return (
//     <div className="App">
//       {showSplash ? (
//         <div className={`splash-wrapper ${fadeClass}`}>
//           <SplashScreen />
//         </div>
//       ) : (
//         <div className="main-menu">
//           <h1 className="main-title">GENESIGHT</h1>
//           <h2 className="subtitle">
//             {page === 'upload' ? 'Upload Your Gene Expression Data' : 'Genetic Disease Risk Analysis'}
//           </h2>
//           <p className="description">
//             {page === 'upload' 
//               ? 'Get a quick and explainable risk assessment for disease prediction.'
//               : 'Analysis based on your genetic expression markers.'}
//           </p>

//           {/* Hologram Section */}
//           <div className="hologram-container">
//             <video autoPlay loop muted playsInline className="hologram-video">
//               <source src={dnaVideo} type="video/mp4" />
//               Your browser does not support the video tag.
//             </video>
//           </div>

//           {page === 'upload' ? (
//             <div className="upload-section">
//               <label htmlFor="file-upload" className="file-label">
//                 Select Gene Expression File
//               </label>
//               <input
//                 id="file-upload"
//                 className="file-input"
//                 type="file"
//                 accept=".csv,.txt"
//                 onChange={handleFileChange}
//               />
//               {selectedFile && (
//                 <p className="file-selected">Selected: {selectedFile.name}</p>
//               )}
//               {error && <p className="error-message">{error}</p>}
//               <button 
//                 className={`upload-button ${isLoading ? 'loading' : ''}`} 
//                 onClick={handleUpload}
//                 disabled={isLoading || !selectedFile}
//               >
//                 {isLoading ? 'Processing...' : 'Analyze Genetic Data'}
//               </button>
//             </div>
//           ) : (
//             <div className="results-section">
//               <h2>Genetic Risk Analysis</h2>
//               {result ? (
//                 <div className="results-container">
//                   <div className={`risk-score ${getRiskColor(result.riskScore)}`}>
//                     <h3>Risk Score</h3>
//                     <div className="score-value">{(result.riskScore * 100).toFixed(1)}%</div>
//                     <p className="risk-level">
//                       {result.riskScore >= 0.7 ? 'High Risk' : 
//                        result.riskScore >= 0.4 ? 'Medium Risk' : 'Low Risk'}
//                     </p>
//                   </div>
                  
//                   <div className="top-features">
//                     <h3>Key Genetic Markers</h3>
//                     <ul className="feature-list">
//                       {result.topFeatures.map((feat, idx) => (
//                         <li key={idx} className="feature-item">
//                           <span className="gene-name">{feat.gene}</span>
//                           <div className="importance-bar-container">
//                             <div 
//                               className="importance-bar" 
//                               style={{width: `${Math.min(feat.importance * 100, 100)}%`}}
//                             ></div>
//                           </div>
//                           <span className="importance-value">{feat.importance.toFixed(2)}</span>
//                         </li>
//                       ))}
//                     </ul>
//                   </div>
                  
//                   <button className="back-button" onClick={handleBack}>
//                     Analyze Another Sample
//                   </button>
//                 </div>
//               ) : (
//                 <p>Loading results...</p>
//               )}
//             </div>
//           )}
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;



import React, { useState, useEffect } from 'react';
import SplashScreen from './SplashScreen';
import './styles.css';
import dnaVideo from './assets/dnaHologram.mp4';

function App() {
  // Splash screen and page states
  const [showSplash, setShowSplash] = useState(true);
  const [fadeClass, setFadeClass] = useState('');
  const [page, setPage] = useState('upload');

  // State to store the file selected by the user
  const [selectedFile, setSelectedFile] = useState(null);
  // State to store prediction results
  const [result, setResult] = useState(null);
  // Loading state
  const [isLoading, setIsLoading] = useState(false);
  // Error state
  const [error, setError] = useState(null);

  useEffect(() => {
    const timer = setTimeout(() => {
      setFadeClass('fade-out');
      setTimeout(() => {
        setShowSplash(false);
      }, 1000);
    }, 3000);
    return () => clearTimeout(timer);
  }, []);

  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setSelectedFile(e.target.files[0]);
      setError(null); // Clear any previous errors
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError("Please select a file first.");
      return;
    }
    
    // Set loading state
    setIsLoading(true);
    setError(null);
    
    // Create a FormData object and append the file
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      // Make sure this URL matches your FastAPI server
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData
      });
      
      if (!response.ok) {
        throw new Error(`Server returned ${response.status}: ${response.statusText}`);
      }
      
      const data = await response.json();
      console.log("Prediction result:", data);
      
      // Validate the response data structure
      validateResultData(data);
      
      setResult(data);
      setPage("results");
    } catch (error) {
      console.error("Error uploading file:", error);
      setError(`Error: ${error.message || "Failed to process data"}`);
      setPage("upload"); // Stay on upload page on error
    } finally {
      setIsLoading(false);
    }
  };

  // Function to validate the response data structure
  const validateResultData = (data) => {
    if (!data) {
      throw new Error("No data received from server");
    }
    
    if (typeof data.riskScore !== 'number') {
      throw new Error("Invalid risk score format in response");
    }
    
    if (!Array.isArray(data.topFeatures)) {
      throw new Error("Invalid top features format in response");
    }
    
    // Check each feature has the required structure
    data.topFeatures.forEach((feature, index) => {
      if (!feature.gene || typeof feature.importance !== 'number') {
        throw new Error(`Invalid feature data at index ${index}`);
      }
    });
  };

  // Function to safely render numeric values
  const safeNumberDisplay = (value, decimals = 1) => {
    if (value === undefined || value === null || isNaN(value)) {
      return "N/A";
    }
    return typeof value === 'number' ? value.toFixed(decimals) : "N/A";
  };

  // Function to determine risk level color
  const getRiskColor = (score) => {
    if (!score && score !== 0) return "unknown-risk";
    if (score >= 0.7) return "high-risk";
    if (score >= 0.4) return "medium-risk";
    return "low-risk";
  };

  // Function to get risk level text
  const getRiskLevelText = (score) => {
    if (!score && score !== 0) return "Unknown Risk";
    if (score >= 0.7) return "High Risk";
    if (score >= 0.4) return "Medium Risk";
    return "Low Risk";
  };

  // Go back to upload page
  const handleBack = () => {
    setPage('upload');
    setResult(null);
    setSelectedFile(null);
    setError(null);
  };

  // Retry connection to server
  const handleRetry = () => {
    if (selectedFile) {
      handleUpload();
    } else {
      setError("Please select a file first.");
    }
  };

  return (
    <div className="App">
      {showSplash ? (
        <div className={`splash-wrapper ${fadeClass}`}>
          <SplashScreen />
        </div>
      ) : (
        <div className="main-menu">
          <h1 className="main-title">GENESIGHT</h1>
          <h2 className="subtitle">
            {page === 'upload' ? 'Upload Your Gene Expression Data' : 'Genetic Disease Risk Analysis'}
          </h2>
          <p className="description">
            {page === 'upload' 
              ? 'Get a quick and explainable risk assessment for disease prediction.'
              : 'Analysis based on your genetic expression markers.'}
          </p>

          {/* Hologram Section - with error handling for video load */}
          <div className="hologram-container">
            <video 
              autoPlay 
              loop 
              muted 
              playsInline 
              className="hologram-video"
              onError={(e) => console.error("Video failed to load:", e)}
            >
              <source src={dnaVideo} type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          </div>

          {page === 'upload' ? (
            <div className="upload-section">
              <label htmlFor="file-upload" className="file-label">
                Select Gene Expression File
              </label>
              <input
                id="file-upload"
                className="file-input"
                type="file"
                accept=".csv,.txt"
                onChange={handleFileChange}
              />
              {selectedFile && (
                <p className="file-selected">Selected: {selectedFile.name}</p>
              )}
              {error && (
                <div className="error-container">
                  <p className="error-message">{error}</p>
                  <button className="retry-button" onClick={handleRetry}>
                    Retry
                  </button>
                </div>
              )}
              <button 
                className={`upload-button ${isLoading ? 'loading' : ''}`} 
                onClick={handleUpload}
                disabled={isLoading || !selectedFile}
              >
                {isLoading ? 'Processing...' : 'Analyze Genetic Data'}
              </button>
            </div>
          ) : (
            <div className="results-section">
              <h2>Genetic Risk Analysis</h2>
              {result ? (
                <div className="results-container">
                  <div className={`risk-score ${getRiskColor(result.riskScore)}`}>
                    <h3>Risk Score</h3>
                    <div className="score-value">
                      {typeof result.riskScore === 'number'
                        ? `${(result.riskScore * 100).toFixed(1)}%`
                        : "N/A"}
                    </div>
                    <p className="risk-level">
                      {getRiskLevelText(result.riskScore)}
                    </p>
                  </div>
                  
                  <div className="top-features">
                    <h3>Key Genetic Markers</h3>
                    {Array.isArray(result.topFeatures) && result.topFeatures.length > 0 ? (
                      <ul className="feature-list">
                        {result.topFeatures.map((feat, idx) => (
                          <li key={idx} className="feature-item">
                            <span className="gene-name">{feat.gene || "Unknown Gene"}</span>
                            <div className="importance-bar-container">
                              <div 
                                className="importance-bar" 
                                style={{
                                  width: typeof feat.importance === 'number'
                                    ? `${Math.min(feat.importance * 100, 100)}%`
                                    : '0%'
                                }}
                              ></div>
                            </div>
                            <span className="importance-value">
                              {safeNumberDisplay(feat.importance, 2)}
                            </span>
                          </li>
                        ))}
                      </ul>
                    ) : (
                      <p className="no-features">No genetic markers available</p>
                    )}
                  </div>
                  
                  <button className="back-button" onClick={handleBack}>
                    Analyze Another Sample
                  </button>
                </div>
              ) : (
                <div className="loading-results">
                  <p>Preparing results...</p>
                  <button className="back-button" onClick={handleBack}>
                    Back to Upload
                  </button>
                </div>
              )}
            </div>
          )}
          
          {/* Footer with version info */}
          <div className="app-footer">
            <p>GeneSight v1.0.0 | AI-Powered Genetic Analysis</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;