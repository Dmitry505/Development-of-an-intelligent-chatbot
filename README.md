# Development-of-an-intelligent-chatbot

## Статус

На данный момент готов скилет раг. 
Модель выдаёт нормальные ответы за счёт достаточного мощьного llm, но сам rag работает плохо и больше мешает чем помогает

## Структура
```bash
Development-of-an-intelligent-chatbot/
│
├── notebooks/
│   └── preprocessing.ipynb         - Загрузка, предобработка, разбиение на чанки, векторизация, сохранение
│   └── response_generation.ipynb   - Получение вопроса, поиск нужных чанков, генерация ответа
│
├── data/
│   └── processed_data/             - Обработанные вектора из preprocessing.ipynb
│   └── standard_data/              - Книги для раг
```
## Теория

Общая информация находится в этой статье:  https://www.datacamp.com/tutorial/llama-3-1-rag#rdl

Исчрепывающая информация в библиотеке: https://python.langchain.com/docs/introduction/

## Необходимые инструменты

Для запуска понадобиться скачть Ollama: https://ollama.com/download

## Установка Ollama

советую прописывать комманду в PowerShell

 ```bash
    ollama pull llama3.1 
```

в дальнейшем, при работе, Ollama должна быть ззапущена

## Установка и запуск
1. Клонируйте репозиторий:

```bash
   git clone https://github.com/Dmitry505/Development-of-an-intelligent-chatbot
   cd Development-of-an-intelligent-chatbot/rag_skeleton
```
   
2. Установите зависимости:
Список не исчерпывающй

```bash
    pip install notebook
    pip install langchain
    pip install -qU langchain-ollama 
    pip install -qU langchain_community pypdf
```
