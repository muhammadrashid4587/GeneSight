// api.js

// Function to send data for prediction to the backend
export const predict = async (fileData) => {
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ fileData }),
        });

        if (!response.ok) {
            throw new Error('Prediction failed');
        }

        const data = await response.json();
        return data; // Return the prediction result
    } catch (error) {
        console.error("Error making prediction:", error);
    }
};

// Function to fetch stats from the backend
export const getStats = async () => {
    try {
        const response = await fetch('/api/stats');

        if (!response.ok) {
            throw new Error('Failed to fetch stats');
        }

        const stats = await response.json();
        return stats; // Return the stats data
    } catch (error) {
        console.error("Error fetching stats:", error);
    }
};
