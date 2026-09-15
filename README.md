# virtual-diabetes-triage

Virtual Diabetes Clinic ML Service (MLOps Assignment) — a FastAPI service serving a scikit-learn regression model trained on the public `sklearn.datasets.load_diabetes` dataset, containerized with Docker and tested/linted via GitHub Actions CI/CD.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Train the model (writes app/model.pkl and app/metrics.json — not committed to git)
python app/train.py

# Run the API
uvicorn app.app:app --reload
```

## Endpoints

- `GET /health` — service status and model version.
- `POST /predict` — takes the 10 diabetes-dataset features (`age`, `sex`, `bmi`, `bp`, `s1`-`s6`) and returns a predicted disease-progression score.

## Tests & linting

```bash
pip install pytest flake8
python app/train.py   # tests import the app, which loads app/model.pkl at startup
pytest tests
flake8 app tests
```

## Docker

```bash
docker build -t virtual-diabetes-triage .
docker run -p 8000:8000 virtual-diabetes-triage
```

The image trains the model during the build, so it's self-contained.
