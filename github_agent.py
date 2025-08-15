from __future__ import annotations as _annotations

import asyncio
import os
from dataclasses import dataclass
from typing import Any, List, Dict
import tempfile
from pathlib import Path
from dotenv import load_dotenv
import shutil
import time
import re
import json

import httpx
import logfire
from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai import Agent
from devtools import debug

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Definindo o modelo e o provedor
model_name = "gemini-1.5-flash"  # ou outro modelo disponível
provider = GoogleProvider(api_key=GOOGLE_API_KEY)

# Inicializando o modelo
model = GoogleModel(model_name, provider=provider)

# Criando o agente
agent = Agent(model)
