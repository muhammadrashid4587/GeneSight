import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import Papa from 'papaparse';  // Import Papaparse for CSV parsing
import { predict, getStats } from './api';  // Assuming you have an API file
import './Dashboard.css'; // Import the CSS file
import './styles.css'; // Import the additional CSS file

const Dashboard = () => {
    const [stats, setStats] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [geneData, setGeneData] = useState([]); // Store gene importance data

    // Fetch stats every 10 seconds
    useEffect(() => {
        const fetchStats = async () => {
            const statsData = await getStats();
            console.log("Stats data:", statsData); // Log stats data
            setStats(statsData);
        };

        fetchStats();
        const intervalId = setInterval(fetchStats, 10000);

        return () => clearInterval(intervalId); // Cleanup interval on component unmount
    }, []);

    // Handle file upload and prediction
    const handleFileUpload = async (event) => {
        const fileData = event.target.files[0];
        if (!fileData) {
            console.error("No file uploaded");
            return;
        }

        // Read the file and parse CSV
        const text = await fileData.text();

        // Parse CSV with PapaParse
        Papa.parse(text, {
            complete: async (result) => {
                console.log("Parsed CSV data:", result.data); // Log parsed CSV data

                // Send parsed data to predict function
                const predictionResult = await predict(result.data);
                console.log("Prediction result:", predictionResult); // Log prediction result

                setPrediction(predictionResult);
                setGeneData(predictionResult.geneImportance); // Set gene importance for the chart
            },
            header: true,  // Assuming first row is headers
            skipEmptyLines: true,  // Skip empty lines
        });
    };

    return (
        <div>
            <h2>Profiles Analyzed: {stats ? stats.analyzed : 'Loading...'}</h2>
            <h2>Prediction: {prediction ? prediction.result : 'No prediction yet'}</h2>

            <input type="file" onChange={handleFileUpload} />

            {/* Container for the chart */}
            <div className="chart-container">
                {/* Bar Chart for Gene Importance */}
                <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={geneData}>
                        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" /> {/* Lighter grid color */}
                        <XAxis dataKey="gene" tick={{ fill: '#6c757d' }} /> {/* X axis text color */}
                        <YAxis tick={{ fill: '#6c757d' }} /> {/* Y axis text color */}
                        <Tooltip contentStyle={{ backgroundColor: '#f8f9fa', borderColor: '#ddd' }} /> {/* Tooltip styling */}
                        <Legend verticalAlign="top" height={36} /> {/* Legend customization */}
                        <Bar dataKey="importance" fill="#008000" radius={[10, 10, 0, 0]} />
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
};

export default Dashboard;

