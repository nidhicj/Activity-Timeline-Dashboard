# 🧠 API Data Aggregator Website

This is a full-stack application that performs daily aggregation of data from two external APIs. The system fetches JSON responses, merges them on a common `id` field, stores the result in a database, and displays it on a web interface.

---

## 📌 Features

- 🔄 Daily scheduled API calls
- 🧩 Aggregates JSON data based on `id`
- 🗃️ Stores merged results in a SQL database
- 🧾 Logs every step of the process
- 🌐 Displays the final data on a web frontend

---

## 🧱 Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| Frontend     | React.js             |
| Backend      | FastAPI (Python)     |
| Scheduler    | APScheduler / Celery |
| Database     | PostgreSQL / SQLite  |
| ORM          | SQLAlchemy           |
| Hosting      | Render / Vercel      |
| Logging      | Python `logging`     |
| Version Ctrl | Git + GitHub         |

---

## 🚦 How It Works

1. **Scheduled Job** runs at the end of the day
2. **API 1** and **API 2** are called
3. Responses are parsed and merged using `id`
4. Final result is saved in a database table
5. Logs are generated for all actions
6. **Frontend** displays the latest data

---

## 🗃️ Folder Structure

```bash
├── backend/
│   ├── main.py           # FastAPI app
│   ├── scheduler.py      # Scheduler logic
│   ├── aggregator.py     # Merging logic
│   ├── db/
│   │   ├── models.py     # DB Models
│   │   └── database.py   # DB Session
│   └── logs/
├── frontend/
│   ├── public/
│   └── src/
│       ├── App.js        # React main component
│       └── components/   # Table & UI components
├── README.md
├── requirements.txt
├── .env
```


## ⚙️ Setup Instructions
1. Clone the Repo

```
git clone https://github.com/your-username/api-data-aggregator.git
cd api-data-aggregator
```

2. Create a Python Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Set Up .env File
```
API1_URL=https://api1.example.com/data
API2_URL=https://api2.example.com/data
DATABASE_URL=postgresql://user:pass@localhost/dbname
```
5. Run the Backend Server
```
uvicorn backend.main:app --reload
```
6. Run the Frontend
```
cd frontend
npm install
npm start
```
## 🧪 Testing

To run unit tests:
```
pytest tests/
```
## 📅 Scheduler

The daily job runs using APScheduler (or Celery if configured), triggering at 11:59 PM server time.

## 📊 Future Enhancements

    Add user authentication

    Export data as CSV/Excel

    Build API health monitoring dashboard

    Display charts & insights

## 🧑‍💻 Contributing

Pull requests are welcome! Please fork the repo and submit a PR.

## 🛡️ License

MIT License