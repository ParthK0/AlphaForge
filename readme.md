# AlphaForge

AlphaForge is a quantitative trading and research platform.

## Project Structure

```text
alphaforge/
├── backend/             # Python backend (FastAPI)
│   ├── agents/          # One file per agent (LLM/Logic)
│   ├── data/            # Data ingestion and processing scripts
│   ├── rag/             # Retrieval-Augmented Generation pipeline
│   ├── api/             # FastAPI routes and endpoints
│   └── main.py          # Entry point for the backend
├── frontend/            # Next.js application (Web UI)
├── backtester/          # Java-based high-performance backtester
├── .env                 # Environment variables and secrets
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Getting Started

### Backend Setup
1. Create a Python virtual environment inside the `backend/` directory:
   ```bash
   cd backend
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **Mac/Linux:** `source venv/bin/activate`
   - **Windows:** `venv\Scripts\activate`
3. Install dependencies from the root directory:
   ```bash
   pip install -r ../requirements.txt
   ```
4. Set up your `.env` file using `.env.example` as a template.
5. Initialize and verify the database and pgvector extension:
   ```bash
   python data/db_init.py
   ```
6. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## Features
- **FastAPI Backend**: High-performance API for trading logic.
- **LLM-Powered Agents**: Intelligent agents for market analysis.
- **RAG Integration**: Retrieval-Augmented Generation for specialized data processing.
- **Next.js Frontend**: Modern web interface for project management.
- **Java Backtester**: High-performance backtesting engine for trading strategies.

## Contributions
Feel free to open issues or submit pull requests to improve AlphaForge.
