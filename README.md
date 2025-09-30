# RAG Sample Project

A Retrieval-Augmented Generation (RAG) system that combines semantic search with Large Language Models to provide contextual responses about startup companies. This project demonstrates how to build a neural search engine using vector embeddings and integrate it with a local LLM for intelligent question-answering.

## Project Overview

This RAG system allows users to search through a database of startup companies and get AI-powered responses that provide relevant information based on the search context. The system uses:

- **Vector Database**: Qdrant for storing and searching startup embeddings
- **Embedding Model**: SentenceTransformers (all-MiniLM-L6-v2) for text vectorization
- **LLM Integration**: Ollama with Llama2 for response generation
- **API Backend**: FastAPI for serving the neural search API
- **Frontend**: Streamlit for the user interface

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend API   │    │   Vector DB     │
│  (Streamlit)    │◄──►│   (FastAPI)     │◄──►│   (Qdrant)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Local LLM     │
                       │   (Ollama)      │
                       └─────────────────┘
```

## Project Structure

```
rag_sample/
├── neural_search/           # Core neural search functionality
│   ├── app.py              # FastAPI application
│   ├── search_api.py       # Neural search implementation
│   └── llm_interaction.py  # LLM integration
├── frontend/               # Streamlit frontend
│   └── index.py           # Simple frontend demo
├── data/                  # Data storage
│   ├── startups_demo.json # Sample startup data
│   ├── startup_vectors.npy # Pre-computed vectors
│   └── qdrant_storage/    # Qdrant database files
├── notebooks/             # Jupyter notebooks for setup
│   ├── rag_setup.ipynb    # RAG system setup
│   ├── neural_search.ipynb # Neural search demo
│   └── load_vectordata.ipynb # Data loading utilities
├── .devcontainer/         # Development container config
└── requirements.txt       # Python dependencies
```

## Features

- **Semantic Search**: Find startups based on semantic similarity rather than keyword matching
- **Contextual AI Responses**: Get intelligent answers powered by LLM with relevant startup context
- **RESTful API**: Clean API endpoints for integration with other applications
- **Vector Storage**: Efficient vector storage and retrieval using Qdrant
- **Scalable Architecture**: Modular design supporting easy extension and modification

## Prerequisites

Before running this project, ensure you have the following installed:

### Required Services

1. **Qdrant Vector Database**
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

2. **Ollama with Llama2**
   ```bash
   # Install Ollama
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Pull Llama2 model
   ollama pull llama2
   
   # Run Ollama server
   ollama serve
   ```

### Python Environment

- Python 3.11+
- Dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rag_sample
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the vector database** (if not already done)
   
   Use the provided Jupyter notebooks to load data into Qdrant:
   ```bash
   jupyter notebook notebooks/rag_setup.ipynb
   ```

4. **Verify services are running**
   - Qdrant: http://localhost:6333
   - Ollama: http://localhost:11434

## Running the Application

### 1. Start the Backend API

```bash
cd neural_search
python app.py
```

The API will be available at `http://localhost:8000`

### 2. API Endpoints

- **Search Endpoint**: `GET /api/search?q=<your_query>`
  
  Example:
  ```bash
  curl "http://localhost:8000/api/search?q=healthcare startups"
  ```

  Response:
  ```json
  {
    "result": "Based on the healthcare startups in the context...",
    "context": [
      {
        "name": "CancerIQ",
        "description": "Predictive analytics to eliminate cancer...",
        "city": "Chicago"
      }
    ]
  }
  ```

### 3. Frontend Interface (Optional)

```bash
cd frontend
streamlit run index.py
```

Note: The current frontend is a basic demo. You can extend it to create a full search interface.

## Configuration

### Environment Variables

The application uses the following service endpoints (configurable in the code):

- **Qdrant**: `http://host.docker.internal:6333` (for Docker) or `http://localhost:6333`
- **Ollama**: `http://host.docker.internal:11434` (for Docker) or `http://localhost:11434`

### Model Configuration

- **Embedding Model**: `all-MiniLM-L6-v2` (SentenceTransformers)
- **LLM Model**: `llama2` (via Ollama)
- **Collection Name**: `startups`

## Development

### Using Dev Containers

This project includes a VS Code dev container configuration for easy development:

1. Open the project in VS Code
2. Install the "Dev Containers" extension
3. Click "Reopen in Container" when prompted

### Data Management

The project includes sample startup data in JSON format. To add more data:

1. Update `data/startups_demo.json` with new entries
2. Run the data loading notebook to update the vector database
3. Restart the API server

### Extending the System

- **Add new data sources**: Modify the data loading notebooks
- **Change embedding models**: Update `search_api.py`
- **Integrate different LLMs**: Modify `llm_interaction.py`
- **Enhance the frontend**: Extend `frontend/index.py`

## Troubleshooting

### Common Issues

1. **Qdrant Connection Error**
   ```
   Ensure Qdrant is running on port 6333
   docker ps | grep qdrant
   ```

2. **Ollama Connection Error**
   ```
   Verify Ollama service is running
   ollama list
   ```

3. **Model Loading Issues**
   ```
   Check if the Llama2 model is downloaded
   ollama pull llama2
   ```

4. **Port Conflicts**
   ```
   Make sure ports 6333, 8000, and 11434 are available
   ```

### Performance Optimization

- For production use, consider using GPU acceleration for the embedding model
- Implement caching for frequently searched queries
- Use a production-grade deployment for Qdrant and Ollama

## API Documentation

Once the FastAPI server is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Acknowledgments

- **Qdrant** for the vector database
- **SentenceTransformers** for the embedding models
- **Ollama** for local LLM serving
- **FastAPI** for the web framework
- **Streamlit** for the frontend framework

---

For questions or support, please open an issue in the repository.