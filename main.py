from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fraud & Compliance Service"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/admin/login")
def login():
    return {"message": "Login successful"}

@app.get("/api/fraud-check/{user_id}")
def fraud_check(user_id: int):
    return {"user_id": user_id, "status": "clean"}