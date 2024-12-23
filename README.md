# Development-of-an-intelligent-chatbot

## Описание
Данный проект представляет собой разработку интеллектуального чат-бота, который способен взаимодействовать с пользователями, отвечая на их вопросы по SQL. 
Чат-бот использует современные технологии обработки естественного языка (NLP) и машинного обучения для обеспечения высококачественного общения.

## Структура 
```bash
Development-of-an-intelligent-chatbot/
├── back/ - back
├
├── web/ - web
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

Исчерпывающая информация в библиотеке: https://python.langchain.com/docs/introduction/

## Необходимые инструменты

Для запуска понадобиться скачать Ollama: https://ollama.com/download

## Установка Ollama

советую прописывать команду в PowerShell

 ```bash
    ollama pull llama3.1 
```

в дальнейшем, при работе, Ollama должна быть запущена

## Установка и запуск
1. Клонируйте репозиторий:

```bash
   git clone https://github.com/Dmitry505/Development-of-an-intelligent-chatbot
   cd Development-of-an-intelligent-chatbot/rag_skeleton
```
   
2. Установите зависимости:
(Список не исчерпывающий)

```bash
    pip install notebook
    pip install langchain
    pip install -qU langchain-ollama 
    pip install -qU langchain_community pypdf
```
