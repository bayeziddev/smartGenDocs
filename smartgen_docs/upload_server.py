import os
import shutil
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .core import Builder

app = FastAPI(title="SmartGen Docs Upload Manager")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DOCS_DIR = Path("docs")
ALLOWED_EXTENSIONS = {".md", ".markdown"}

@app.get("/", response_class=HTMLResponse)
async def upload_page():
    """Serve the upload interface."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SmartGen Docs - Upload Manager</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }
            .container {
                background: white;
                border-radius: 12px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                max-width: 600px;
                width: 100%;
                padding: 2rem;
            }
            h1 {
                color: #333;
                margin-bottom: 0.5rem;
                font-size: 1.8rem;
            }
            .subtitle {
                color: #666;
                margin-bottom: 2rem;
                font-size: 0.95rem;
            }
            .upload-zone {
                border: 2px dashed #667eea;
                border-radius: 8px;
                padding: 3rem 2rem;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                background: #f8f9ff;
            }
            .upload-zone:hover {
                border-color: #764ba2;
                background: #f0f2ff;
            }
            .upload-zone.dragover {
                border-color: #764ba2;
                background: #e8ebff;
            }
            .upload-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            .upload-text {
                color: #333;
                font-weight: 600;
                margin-bottom: 0.5rem;
            }
            .upload-hint {
                color: #999;
                font-size: 0.9rem;
            }
            #file-input {
                display: none;
            }
            .file-list {
                margin-top: 2rem;
            }
            .file-item {
                background: #f5f5f5;
                padding: 1rem;
                border-radius: 6px;
                margin-bottom: 0.5rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .file-name {
                color: #333;
                font-weight: 500;
            }
            .file-status {
                font-size: 0.85rem;
                color: #999;
            }
            .btn {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 6px;
                cursor: pointer;
                font-weight: 600;
                transition: all 0.3s ease;
                margin-top: 1rem;
                width: 100%;
            }
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
            }
            .success {
                background: #10b981;
                padding: 1rem;
                border-radius: 6px;
                color: white;
                margin-top: 1rem;
                display: none;
            }
            .error {
                background: #ef4444;
                padding: 1rem;
                border-radius: 6px;
                color: white;
                margin-top: 1rem;
                display: none;
            }
            .footer {
                margin-top: 2rem;
                padding-top: 2rem;
                border-top: 1px solid #eee;
                text-align: center;
                color: #999;
                font-size: 0.85rem;
            }
            .footer a {
                color: #667eea;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📚 SmartGen Docs Upload Manager</h1>
            <p class="subtitle">Drag and drop your Markdown files to add them to your documentation</p>
            
            <div class="upload-zone" id="upload-zone">
                <div class="upload-icon">📄</div>
                <div class="upload-text">Drag & Drop Files Here</div>
                <div class="upload-hint">or click to select files (.md, .markdown)</div>
                <input type="file" id="file-input" multiple accept=".md,.markdown">
            </div>
            
            <div class="file-list" id="file-list"></div>
            
            <div class="success" id="success-msg">✓ Files uploaded successfully!</div>
            <div class="error" id="error-msg">✗ Error uploading files</div>
            
            <div class="footer">
                <p>Built with ❤️ by <strong>Sayad Md Bayezid Hosan</strong></p>
                <p>For <a href="https://www.smartgentools.com" target="_blank">Smartgen Platform</a></p>
            </div>
        </div>

        <script>
            const uploadZone = document.getElementById('upload-zone');
            const fileInput = document.getElementById('file-input');
            const fileList = document.getElementById('file-list');
            const successMsg = document.getElementById('success-msg');
            const errorMsg = document.getElementById('error-msg');

            uploadZone.addEventListener('click', () => fileInput.click());

            uploadZone.addEventListener('dragover', (e) => {
                e.preventDefault();
                uploadZone.classList.add('dragover');
            });

            uploadZone.addEventListener('dragleave', () => {
                uploadZone.classList.remove('dragover');
            });

            uploadZone.addEventListener('drop', (e) => {
                e.preventDefault();
                uploadZone.classList.remove('dragover');
                handleFiles(e.dataTransfer.files);
            });

            fileInput.addEventListener('change', (e) => {
                handleFiles(e.target.files);
            });

            async function handleFiles(files) {
                fileList.innerHTML = '';
                successMsg.style.display = 'none';
                errorMsg.style.display = 'none';

                for (let file of files) {
                    if (!file.name.endsWith('.md') && !file.name.endsWith('.markdown')) {
                        errorMsg.textContent = '✗ Only .md and .markdown files are allowed';
                        errorMsg.style.display = 'block';
                        continue;
                    }

                    const fileItem = document.createElement('div');
                    fileItem.className = 'file-item';
                    fileItem.innerHTML = `
                        <span class="file-name">${file.name}</span>
                        <span class="file-status">Uploading...</span>
                    `;
                    fileList.appendChild(fileItem);

                    const formData = new FormData();
                    formData.append('file', file);

                    try {
                        const response = await fetch('/upload', {
                            method: 'POST',
                            body: formData
                        });

                        if (response.ok) {
                            fileItem.querySelector('.file-status').textContent = '✓ Uploaded';
                            fileItem.querySelector('.file-status').style.color = '#10b981';
                            successMsg.style.display = 'block';
                        } else {
                            fileItem.querySelector('.file-status').textContent = '✗ Failed';
                            fileItem.querySelector('.file-status').style.color = '#ef4444';
                            errorMsg.style.display = 'block';
                        }
                    } catch (error) {
                        fileItem.querySelector('.file-status').textContent = '✗ Error';
                        fileItem.querySelector('.file-status').style.color = '#ef4444';
                        errorMsg.style.display = 'block';
                    }
                }
            }
        </script>
    </body>
    </html>
    """

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Handle file uploads."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    # Check file extension
    if not any(file.filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise HTTPException(status_code=400, detail="Only .md and .markdown files are allowed")
    
    # Ensure docs directory exists
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save file
    file_path = DOCS_DIR / file.filename
    try:
        contents = await file.read()
        with open(file_path, 'wb') as f:
            f.write(contents)
        return JSONResponse({"message": f"File {file.filename} uploaded successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

@app.get("/files")
async def list_files():
    """List all uploaded documentation files."""
    if not DOCS_DIR.exists():
        return {"files": []}
    
    files = [f.name for f in DOCS_DIR.glob("*.md")]
    return {"files": files}

@app.delete("/files/{filename}")
async def delete_file(filename: str):
    """Delete a documentation file."""
    file_path = DOCS_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        file_path.unlink()
        return JSONResponse({"message": f"File {filename} deleted successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")

@app.post("/rebuild")
async def rebuild_site():
    """Rebuild the documentation site."""
    try:
        builder = Builder("smartgen.yml", "site")
        builder.build()
        return JSONResponse({"message": "Site rebuilt successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rebuilding site: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
