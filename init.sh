#!/bin/bash

# 確保腳本在遇到錯誤時退出
set -e
export ENV_FILE=.env.default

# 加載 .env 文件中的環境變數
if [[ -f "$ENV_FILE" ]]; then
    echo "Loading environment variables from $ENV_FILE file..."
    export $(grep -v '^#' $ENV_FILE | xargs)
else
    echo "Error: $ENV_FILE file not found!"
    exit 1
fi


# 啟動 docker
docker-compose down
docker-compose build
docker-compose up -d


# 待 Ollama 啟動後，載入 LLM model
echo "Waiting for the Ollama service to be ready..."
until docker exec -it ollama ollama list &> /dev/null; do
    sleep 1
done
echo "Service is ready."

if docker exec -it ollama ollama list | grep -q "$OLLAMA_MODEL"; then
    echo "Model '$OLLAMA_MODEL' already exists. Skipping model execution."
else
    echo "Model '$OLLAMA_MODEL' not found. Running model command..."
    docker exec -it ollama ollama run $OLLAMA_MODEL
fi


# 成功啟動後，顯示 logs
docker logs --follow opengpts-backend