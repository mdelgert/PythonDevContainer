To install **Flask**, follow these steps:

---

### ✅ **Step 1: (Optional but recommended) Create a virtual environment**
This helps isolate your project’s dependencies.

```bash
python3 -m venv venv
source venv/bin/activate      # On Linux/macOS
# OR
venv\Scripts\activate         # On Windows
```

---

### ✅ **Step 2: Install Flask using pip**

```bash
pip install flask
```

To confirm the installation:

```bash
python -m flask --version
```

You should see something like:

```
Python 3.x.x
Flask x.x.x
Werkzeug x.x.x
```

---

### ✅ **Step 3: Create a simple Flask app (hello.py)**

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

---

### ✅ **Step 4: Run the app**

Set the environment variable (if needed):

```bash
export FLASK_APP=hello.py        # On Linux/macOS
set FLASK_APP=hello.py           # On Windows (CMD)
$env:FLASK_APP = "hello.py"      # On Windows (PowerShell)
```

Then start the server:

```bash
flask run
```

By default, it will run on [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

Want help creating a starter template or auto-reloading with `debug=True`?