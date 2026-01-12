from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas
import uvicorn

app = FastAPI()
# permite que o front acesse o backend sem problemas de permissão
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar o CSV
df_operadoras = pandas.read_csv("Relatorio_cadop.csv", sep=";", encoding="utf-8-sig")

# Padronização de colunas
df_operadoras.columns = df_operadoras.columns.str.strip().str.lower()

@app.get("/buscar")
def buscar_operadoras(termoBusca: str = Query("", description="Termo de busca para Razão Social")):
    if not termoBusca:
        return []
    # Realiza o filtro de busca
    mask = df_operadoras['razao_social'].str.contains(termoBusca, case=False, na=False)
    # Seleciona apenas as linhas com resultados, remove NaNs e limita a 20 resultados
    resultados = df_operadoras[mask].head(20).fillna("Não Informado")
    # Devolve um json padrão
    return resultados.to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)