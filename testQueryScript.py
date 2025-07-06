import subprocess

def run_sqlite_query():
    ssh_command = [
        "ssh",
        "knxpi@192.168.0.7",
        "sqlite3 /path/to/database.db 'SELECT * FROM tablename LIMIT 10;'"
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(ssh_command, capture_output=True, text=True, check=True)
        print("Query result:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running command:", e)
        print("stderr:", e.stderr)

if __name__ == "__main__":
    run_sqlite_query()