@app.get("/happy", status_code=200)
def happy():
    return ":)"
