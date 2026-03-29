
# PMFBY Claim Reconciliation Tool

## Problem Statement

In India's **Pradhan Mantri Fasal Bima Yojana (PMFBY)** crop insurance scheme, thousands of valid farmer claims are blocked every year due to minor data mismatches between:
- **Paper receipts** (fertilizer bills, handwritten records submitted at the field level)
- **PMFBY portal entries** (digitally entered by insurance agents)

Example: A farmer's receipt shows `Area: 0.50 ha`, but the portal recorded `0.45 ha`. This small discrepancy — often a data-entry error — causes claim rejection, leaving farmers without compensation.

## Solution

A lightweight web app that:
1. Simulates loading a paper receipt
2. Fetches the corresponding PMFBY portal record
3. Automatically compares all fields
4. Highlights mismatches clearly
5. Generates a reconciliation report for human review

---

## Features

- 📄 Receipt extraction simulation (mock data)
- 🌐 Portal data retrieval (mock API)
- ⚖️ Automatic field-level comparison
- 🔴 Visual mismatch highlighting
- 📋 Report generation
- Clean, modern dashboard UI

---

## Project Structure

```
project-root/
├── backend/
│   └── app.py          # Flask server (all routes)
├── frontend/
│   └── index.html      # Full UI (Tailwind CSS)
├── requirements.txt
└── README.md
```

---

## Setup & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Flask server

```bash
python backend/app.py
```

### 3. Open in browser

```
http://127.0.0.1:5000
```

---

## API Routes

| Method | Route              | Description                        |
|--------|--------------------|------------------------------------|
| GET    | `/`                | Serves the frontend dashboard      |
| GET    | `/get_data`        | Returns mock receipt + portal data |
| POST   | `/compare`         | Compares data, returns status      |
| POST   | `/generate_report` | Returns plain-text audit report    |

---

## Mock Data Used

```json
{
  "receipt": { "farmer": "Ravi Kumar", "area": 0.50, "crop": "Rice" },
  "portal":  { "farmer": "Ravi Kumar", "area": 0.45, "crop": "Rice" }
}
```

Area difference: `0.05 ha` → exceeds `0.01 ha` threshold → **MISMATCH**

---

## Tech Stack

- **Backend**: Python 3 + Flask (single file)
- **Frontend**: HTML5 + Tailwind CSS CDN (single file)
- **Data**: Hardcoded JSON (no database)
- **Auth**: None (demo prototype)
=======
# pmfby-claim-reconciliation
PMFBY Claim Reconciliation Tool - GenAI Hackathon Project
>>>>>>> 0079fb7f407ca90a6a1dd55182ddbc60c5c461de
