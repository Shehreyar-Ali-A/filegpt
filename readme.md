# FileGPT Project

## About
FileGPT Project is a clone of ChatPDF where users can upload PDF or JPG files and ask an AI model questions about the content of the files.

## Frontend Libraries:
- **Next.js (v14)**: Framework for server-rendered React applications.
- **Tailwind CSS**: Utility-first CSS framework.
- **Clerk SDK for Next.js**: Integration library for user authentication in Next.js. Handles user authentication.
- **Vercel AI SDK**: SDK for interacting with backend endpoints for AI response generation. Handles interaction with AI model.

## Backend Libraries:
- **Django**: Web framework for building APIs in Python.
- **Poetry**: Dependency management tool for Python projects. Manages project dependencies.
- **PostgreSQL**: Relational database management system.
- **Neon DB**: Hosted and managed PostgreSQL database.
- **Pinecone DB**: Vector database for storing embeddings.
- **PyPDF2**: Library for PDF processing in Python. Handles PDF processing.
- **Tesseract**: OCR engine for text recognition. Handles image processing.
- **OpenAI's GPT-3.5-turbo model**: Language model for generating responses.
- **Langchain library**: Library for natural language processing tasks.


## Docker
Both the frontend and backend are containerized using separate Dockerfiles. A Docker Compose YAML file is provided to spin up both containers for local development.

## Hosting
The frontend is hosted on a managed deployment platform called Railway, while the backend is deployed on an Amazon EC2 instance.



## Getting Started
- Clone this repository.

    ```git clone https://github.com/Shehreyar-Ali-A/filegpt.git```

- Set up third party services
    1. Clerk

    - Create an account in [here](https://clerk.com/)
    - Copy the keys displayed and paste it into the frontend's .env file :

    ```Bash
    NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY= key_here
    CLERK_SECRET_KEY= key_here
    ```

    2.  **NEON DB** (To get DATABASE_URL for .env file)

    - Create an account [here](https://neon.tech/)
    - Create a project
    - Copy the URL shown and paste it into `DATABASE_URL` in .env file

    ```Bash
        PGHOST= host_here
        PGDATABASE= database_name_here
        PGUSER= username_here
        PGPASSWORD= password_here
    ```


    3. **Pinecone DB Setup**

    - Go to [Pinecone](https://www.pinecone.io/) > Create an account
    - Create new project > Create a new Index
    - Configure your Index
        - Dimensions : 1536
    - Click `Create Index`
    - Create API Key and paste keys in `.env` file:
    - _PINECONE_ENVIRONMENT value is of the format REGION-ENVIRONMENT_

    ```Bash
    PINECONE_API_KEY= pinecone_api_key
    PINECONE_DB_INDEX= pinecone_db_index
    ```

    4. **OPENAI API**

    - Go to [OpenAI API](https://openai.com/blog/openai-api)
    - Menu > API > Overview
    - Click `For Developers` > `Embeddings`
    - Login if not yet done
    - Go to `API Keys` and create a new Secret Key
    - Copy and paste API key into `.env` file

    ```Bash
    OPENAI_API_KEY=your_api_key
    ```

- Make sure you have Docker installed on your system.
- Run `docker-compose up` command to spin up both containers.
- The frontend runs on port 3030, and the backend runs on port 8080.

Note: You need to have the keys for the respective third-party apps to run the project locally.
