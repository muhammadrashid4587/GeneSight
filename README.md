
# 🧬 GeneSight: AI-Driven Genomic Mutation Classifier

GeneSight is a precision medicine tool that classifies genetic mutations using machine learning and clinical metadata. Built for clinicians and researchers, it helps identify and assess potentially pathogenic variants based on sequence features, annotation data, and phenotype correlations.

---

## 🚀 Project Vision

To empower personalized medicine by providing:

- ✅ Accurate mutation classification (e.g. missense, nonsense, silent)
- 🔍 Risk scores for pathogenicity
- 📊 Interactive mutation explorer UI
- 🧠 AI insights trained on clinical metadata

---

## 🧪 Tech Stack

| Layer        | Tech Used                            |
|--------------|--------------------------------------|
| Frontend     | React + Vite + Tailwind              |
| Backend      | FastAPI                              |
| ML/AI Engine | Scikit-learn, XGBoost, Pandas        |
| Visualization| Plotly + Chart.js                    |
| Deployment   | Docker + GitHub Actions              |

---

## 🧰 Features

- Mutation input (manual, file upload)
- ML-based classification
- Risk scoring & probability confidence
- CSV report generation
- (Future) Integration with patient EHR data
- (Future) FDA/CLIA-compliant audit mode

---

## 📂 Project Structure

```
GeneSight/
│
├── backend/              # FastAPI server & ML models
│   ├── models/           # Trained classifiers & pipelines
│   ├── api/              # Routes & endpoints
│   └── utils/            # Feature extraction & preprocessing
│
├── frontend/             # React + Vite UI
│   └── src/
│       ├── components/
│       └── pages/
│
├── data/                 # Test samples & metadata files
├── docker-compose.yml    # Service orchestration
└── .env.example          # Environment variables
```

---

## 🧪 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/genesight.git
cd genesight
```

### 2. Setup Environment Variables
```bash
cp .env.example .env
```

### 3. Launch with Docker
```bash
docker-compose up --build
```

### 4. Local Access
- Frontend: `http://localhost:5173`
- Backend API: `http://localhost:8000/docs`

---

## 🎯 Use Case Example

Upload a `.vcf` file or manually enter mutation data. GeneSight will:

1. Classify the mutation type (missense, nonsense, etc.)
2. Generate a risk score (0–1 scale)
3. Provide explainable features via SHAP

---

## 📄 License

MIT License — see LICENSE file for details.

---

## 🤝 Contributing

- Fork the repo
- Create a new branch
- Make your changes
- Submit a pull request

---

## 👨‍🔬 Author

**Muhammad Rashid**  
GitHub: [@muhammadrashid4587](https://github.com/muhammadrashid4587)

---

## 🌱 Future Plans

- Multi-class ensemble models
- Clinical-grade validations
- Secure EHR integration
- Research paper publication under CSL

