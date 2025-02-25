#fastapi
from fastapi import APIRouter, Query
from fastapi import Request
from fastapi.responses import ORJSONResponse
from typing import List

#os, datetime
import os
from datetime import datetime

#utils
from utils.findfiles import find_files


router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

@router.get("/files/file_search", response_model=List[dict])
async def root(fragment: str = Query(..., description="The fragment to search for")):
    """
    Endpoint to find files in the file system by a fragment of their path.
    Returns a list of files with their metadata.
    """
    if not fragment:
        return ORJSONResponse(status_code=400, content={"error": "No fragment provided"})
    results = []
    try:
        results = find_files(fragment, os.getcwd())   
        return ORJSONResponse(status_code=200, content=results)
    except Exception as e:
        return {"error": str(e)}, 500