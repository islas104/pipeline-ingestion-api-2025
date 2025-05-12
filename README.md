# 🌾 Unlock Practice Validation API

This FastAPI application ingests, validates, and generates reports based on agricultural practice submissions.

## 📦 Project Structure

PipelineIngestion2025/
├── src/
│ ├── data/ # Input CSVs
│ ├── database.py # SQLAlchemy DB session
│ ├── models/ # SQLAlchemy ORM models
│ ├── routes/ # Modular routes (e.g., data_checks)
│ └── services/ # Business logic & report generation
├── .env # DB and app config
├── main.py # FastAPI app entry point
├── requirements.txt # Python dependencies


## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://your-repo-url.git
cd PipelineIngestion2025
```

2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up your .env file
```bash
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/dbname
```

5. Run the application
```bash
uvicorn main:app --reload --env-file .env
```

## Endpoints Summary

| Endpoint                        | Method | Description                              |
| ------------------------------- | ------ | ---------------------------------------- |
| `/`                             | GET    | Health check                             |
| `/upload/enrollment-date/`      | POST   | Upload enrollment date CSV               |
| `/report/other-responses/`      | GET    | Report on “Other” responses              |
| `/report/field-summary/`        | GET    | Summary report on irrigation & tillage   |
| `/report/farmer-field-mapping/` | GET    | Mapping report for farmers and fields    |
| `/validation/data-checks/`      | GET    | Run hardcoded validation checks          |
| `/validation/checks/`           | GET    | View list of available validation checks |


## Author
- Islas Ahmed Nawaz
- Unlock Project – Practice Data Validation

