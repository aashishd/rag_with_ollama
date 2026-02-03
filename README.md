# LocalRAG - Privacy-First RAG Application

A desktop Retrieval-Augmented Generation (RAG) application that combines semantic search with local Large Language Models. Built for privacy-conscious users who want AI-powered search without data leaving their machine.

## 🎯 Project Status

**Current State:**
- ✅ Core RAG pipeline working
- ✅ Vector search with Qdrant
- ✅ Ollama integration for local LLM
- ✅ FastAPI backend
- ✅ Basic Streamlit frontend
- 📝 README and documentation (you're reading it!)
- 🔄 CI/CD pipeline configured

**What's Working:**
- Semantic search over documents using sentence embeddings
- Context-aware responses from local Llama2
- RESTful API endpoints
- Docker support for Qdrant

**What's Next:**
- Desktop UI (Electron/Tauri vs Streamlit)
- Plugin system for extensibility
- Obsidian connector (planned first plugin)

## 💼 Business Model

**Open-Core Model:**
- **Free Core**: Basic RAG functionality for everyone
- **Paid Plugins** ($10-25 each): Specialized connectors and features
- **First Plugin**: Obsidian Connector ($15 planned)

## 🚀 Quick Start

### Prerequisites

1. **Python 3.11+**
2. **Qdrant** (vector database)
3. **Ollama** (local LLM serving)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd rag_with_ollama

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start Qdrant (vector database)
docker run -p 6333:6333 qdrant/qdrant

# Start Ollama
ollama serve
ollama pull llama2
```

### Running the Application

```bash
# Terminal 1: Start the API
cd neural_search
python app.py

# Terminal 2: Start the frontend (optional)
cd frontend
streamlit run index.py

# API available at: http://localhost:8000
# Frontend available at: http://localhost:8501
# API Docs: http://localhost:8000/docs
```

### Testing the API

```bash
# Search for startups
curl "http://localhost:8000/api/search?q=healthcare startups"

# Response format:
{
  "result": "AI-generated response...",
  "context": [
    {"name": "StartupName", "description": "...", "city": "..."}
  ]
}
```

## 📁 Project Structure

```
rag_with_ollama/
├── neural_search/          # Core backend logic
│   ├── app.py            # FastAPI application
│   ├── search_api.py     # Vector search implementation
│   └── llm_interaction.py # LLM integration
├── frontend/              # User interface
│   └── index.py         # Streamlit demo
├── data/                  # Data storage
│   ├── startups_demo.json
│   └── qdrant_storage/
├── notebooks/             # Jupyter notebooks
│   ├── rag_setup.ipynb
│   └── neural_search.ipynb
├── .github/              # CI/CD configuration
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface                         │
│           (Streamlit / Future Desktop App)             │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                       │
│                    (Python/FastAPI)                      │
└─────────────────────┬───────────────────────────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│    Qdrant       │     │     Ollama      │
│  (Vector DB)    │     │   (Local LLM)   │
└─────────────────┘     └─────────────────┘
```

## 🔧 Configuration

### Environment Variables

```bash
# Qdrant connection
QDRANT_URL=http://localhost:6333

# Ollama connection
OLLAMA_URL=http://localhost:11434

# Model settings
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=llama2
```

### Changing Models

**Embedding Model** (in `neural_search/search_api.py`):
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')  # Change this line
```

**LLM Model** (in `neural_search/llm_interaction.py`):
```python
ollama pull llama2  # Or another model
model = "llama2"  # Change this variable
```

## 📦 Dependencies

Key packages:
- `fastapi` - Web framework
- `qdrant-client` - Vector database client
- `sentence-transformers` - Text embeddings
- `ollama` - Local LLM integration
- `streamlit` - Frontend framework
- `uvicorn` - ASGI server

Full list: `requirements.txt`

## 🐳 Docker Setup

### Development Container

1. Open in VS Code
2. Install "Dev Containers" extension
3. Click "Reopen in Container"

### Manual Docker Run

```bash
# Start Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Check logs
docker logs <container-id>
```

## 🧪 Testing

```bash
# Run pytest (if tests exist)
pytest

# Manual API testing
curl -X GET "http://localhost:8000/api/search?q=test"
```

## 📝 Data Management

### Adding Documents

1. Place documents in `data/` directory
2. Run the setup notebook: `notebooks/rag_setup.ipynb`
3. Restart the API server

### Sample Data

The `data/startups_demo.json` contains sample startup data for testing. Replace with your own documents for production use.

## 🔍 API Reference

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/search?q=<query>` | Search and get AI response |
| GET | `/health` | Health check |
| GET | `/docs` | Interactive API documentation |

### Search Response

```json
{
  "result": "AI-generated contextual answer",
  "context": [
    {
      "name": "Company Name",
      "description": "Company description...",
      "city": "Location"
    }
  ],
  "processing_time": "0.5s"
}
```

## 🚨 Troubleshooting

### Common Issues

**Qdrant Connection Failed:**
```bash
# Check if Qdrant is running
docker ps | grep qdrant

# Start Qdrant
docker run -p 6333:6333 qdrant/qdrant
```

**Ollama Not Responding:**
```bash
# Check Ollama status
ollama list

# Pull model again
ollama pull llama2

# Restart Ollama
killall ollama
ollama serve
```

**Port Conflicts:**
```bash
# Check what's using ports
lsof -i :6333  # Qdrant
lsof -i :8000  # FastAPI
lsof -i :8501  # Streamlit
```

**Model Loading Errors:**
```bash
# Reinstall sentence-transformers
pip uninstall sentence-transformers
pip install sentence-transformers
```

### Performance Tips

- Use GPU acceleration for embeddings (CUDA)
- Limit document batch size for large datasets
- Implement caching for frequent queries
- Consider Qdrant on-disk storage for large collections

## 🚀 Deployment

### Production Considerations

1. **Security**: Disable debug mode in production
2. **Scaling**: Use Qdrant in cluster mode for large datasets
3. **Monitoring**: Add logging and metrics
4. **Backup**: Regular Qdrant snapshots

### Docker Compose (Future)

```yaml
# Coming soon: docker-compose.yml
services:
  qdrant:
    image: qdrant/qdrant
  ollama:
    image: ollama/ollama
  api:
    build: .
```

## 📈 Roadmap

- [ ] Desktop app (Tauri/Electron)
- [ ] Plugin system architecture
- [ ] Obsidian connector plugin
- [ ] Plugin marketplace
- [ ] User authentication
- [ ] Multi-document RAG
- [ ] Web search integration
- [ ] Voice input/output

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Add tests
5. Submit PR

## 📄 License

[Add your license here]

## 🙏 Acknowledgments

- [Qdrant](https://qdrant.tech/) - Vector database
- [SentenceTransformers](https://www.sentence-transformers.org/) - Embeddings
- [Ollama](https://ollama.com/) - Local LLM serving
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Streamlit](https://streamlit.io/) - Frontend framework

## 📞 Support

- Open an issue for bugs
- Start a discussion for questions
- Submit PRs for improvements

---

**Built with ❤️ for privacy-conscious AI enthusiasts**
