"""
    WebApp FastAPI para Gestão de Vendas
    Este módulo é o ponto de entrada da aplicação, responsável por configurar o FastAPI, definir rotas básicas e incluir os roteadores das funcionalidades principais (usuários, vendas, clientes, produtos).
    Autor: Beny B. Reis II
    Data: 2026-04-02

"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

aplicacao = FastAPI(
    titulo="Gestor de Vendas",
    descricao="Sistema de gestão de vendas",
    versao="1.0.0"
)

origens_permitidas = [
    "http://localhost:2005",
    "http://127.0.0.1:2005",
]

aplicacao.add_middleware(
    CORSMiddleware,
    allow_origins=origens_permitidas,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@aplicacao.get("/", tags=["Raiz"])
async def raiz():
    """Rota de teste da aplicação"""
    return { 
        "mensagem": "Estás em Casa, Mestre", 
        "versao": f"{aplicacao.versao}"
    }



@aplicacao.get("/health", tags=["Health"])
async def verificar_saude():
    """Verifica se a aplicação está funcionando"""
    return {
        "status": "operacional",
        "ambiente": os.getenv("ENVIRONMENT", "desenvolvimento")
    }


# from rotas import usuarios, vendas, clientes, produtos
# aplicacao.include_router(usuarios.roteador)
# aplicacao.include_router(vendas.roteador)
# aplicacao.include_router(clientes.roteador)
# aplicacao.include_router(produtos.roteador)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:aplicacao",
        host="0.0.0.0",
        port=8000,
        reload=True
    )



# 2-5-14-25