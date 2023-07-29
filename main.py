from fastapi import FastAPI,File,UploadFile,WebSocket ,Response, Body
import asyncio
from fastapi.responses import FileResponse 

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse  
import uvicorn
import os
import shutil
from pathlib import Path

app = FastAPI() 
origins = [
    
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


 


@app.post("/download-pdf")
def download_pdf(data=Body()): 
    print(data)
    pdf_directory =  "new_pro.pdf"
   

    pdf_path = Path(pdf_directory) 

    with open(pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()

    headers = {
            "Content-Disposition": f"attachment; filename=new_pro.pdf"
    }

    return Response(content=pdf_content, headers=headers, media_type="application/pdf")
