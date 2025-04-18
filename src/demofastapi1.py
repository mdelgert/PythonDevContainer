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