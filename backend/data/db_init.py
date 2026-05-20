import os
import psycopg2
from dotenv import load_dotenv

def init_db():
    # Load env variables
    load_dotenv()
    
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("Error: DATABASE_URL not set in environment variables.")
        return False
        
    print("Connecting to the database...")
    try:
        conn = psycopg2.connect(db_url)
        conn.autocommit = True
        cur = conn.cursor()
        
        print("Ensuring pgvector extension is enabled...")
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        
        cur.execute("SELECT extversion FROM pg_extension WHERE extname = 'vector';")
        result = cur.fetchone()
        if result:
            print(f"Success: pgvector extension is active (version: {result[0]}).")
        else:
            print("Warning: pgvector extension was enabled but could not be verified.")
            
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error during database initialization: {e}")
        return False

if __name__ == "__main__":
    init_db()
