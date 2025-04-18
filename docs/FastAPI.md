Below is a simple Python FastAPI application that serves a dark-themed webpage. The webpage is a single HTML file styled with Tailwind CSS for a clean, modern dark theme. The FastAPI backend handles the route to serve the webpage.

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dark Theme FastAPI Page</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-900 text-white min-h-screen flex flex-col items-center justify-center">
        <div class="max-w-2xl mx-auto p-6 bg-gray-800 rounded-lg shadow-lg">
            <h1 class="text-3xl font-bold mb-4 text-center">Welcome to FastAPI</h1>
            <p class="text-lg mb-6 text-gray-300 text-center">
                This is a simple dark-themed webpage served by FastAPI.
            </p>
            <div class="flex justify-center">
                <button class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded transition duration-300">
                    Click Me
                </button>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
```

To run this FastAPI application, you'll need to:

1. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

2. Save the code in a file named `main.py`.

3. Run the application using:
   ```bash
   uvicorn main:app --reload
   uvicorn demofastapi1:app --reload
   uvicorn demofastapi2:app --reload
   uvicorn demofastapi3:app --reload
   uvicorn api:app --reload
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000` to view the dark-themed webpage.

The webpage features:
- A dark background with light text for readability.
- A centered card-like container with a subtle shadow.
- A bold heading and descriptive text.
- A styled button with hover effects, all using Tailwind CSS for responsive design.

Let me know if you need additional features or modifications!