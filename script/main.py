from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

from models import benchmarkInput
from query import Benchmark

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/benchmark/")
def extract_tests(request: benchmarkInput):
    test= Benchmark()
    test.metric_from_benchmark(request.web_benchmark)
    resulting_tests = test.call_fdp_for_test_information(request.creator)
    return(resulting_tests)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)