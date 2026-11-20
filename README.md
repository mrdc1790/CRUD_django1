# Django Blog Example

Use Python 3.10 or later to create a virtual environment in this directory.

```sh
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` in PowerShell or
`source .venv/bin/activate` on macOS and Linux. Then install the dependencies.

```sh
python -m pip install -r requirements.txt
```

Set a fresh SQLite database path before running migrations. This command works in PowerShell.

```powershell
$env:DJANGO_DB_PATH = 'db.local.sqlite3'
```

On macOS or Linux, use `export DJANGO_DB_PATH=db.local.sqlite3`.

```sh
python manage.py migrate
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000) to view the blog. Run
`python manage.py test` to check the project. Set `DJANGO_SECRET_KEY` when
you need sessions to survive local server restarts.
