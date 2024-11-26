from fasthtml import FastHTML, serve

# Initialize the app
app = FastHTML()

@app.route("/")
async def homepage(request):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastHTML Web App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                text-align: center;
                max-width: 600px;
                padding: 20px;
                background: #fff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            h1 {
                color: #0056d8;
            }
            p {
                font-size: 1.2em;
                margin: 10px 0;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #0056d8;
                color: #fff;
                text-decoration: none;
                border-radius: 4px;
                transition: background-color 0.3s ease;
            }
            a:hover {
                background-color: #003a94;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to FastHTML App</h1>
            <p>FastHTML is a Python framework for building HTML web apps quickly and efficiently.</p>
            <a href="https://fastht.ml/" target="_blank">Learn More</a>
        </div>
    </body>
    </html>
    """

# Run the app using serve()
if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=8000)
