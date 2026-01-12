<template>
  <div class="container">
    <h1>🔍 Busca de Operadoras</h1>

    <input
      type="text"
      class="search-box"
      v-model="termo"
      @input="pesquisar"
      placeholder="Digite a Razão Social da operadora..."
    />

    <table v-if="resultados.length > 0">
      <thead>
        <tr>
          <th>Registro ANS</th>
          <th>Razão Social</th>
          <th>Modalidade</th>
          <th>Cidade/UF</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="op in resultados" :key="op.registro_operadora">
          <td>{{ op.registro_operadora }}</td>
          <td>{{ op.razao_social }}</td>
          <td>{{ op.modalidade }}</td>
          <td>{{ op.cidade }} / {{ op.uf }}</td>
        </tr>
      </tbody>
    </table>

    <div v-else-if="termo.length >= 3" class="no-results">
      Nenhum resultado encontrado para "{{ termo }}"
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      termo: "", // O que o usuário digita
      resultados: [], // A lista que vem do Python
    };
  },
  methods: {
    async pesquisar() {
      // Só faz a busca se o usuário digitar 3 ou mais caracteres
      if (this.termo.length < 3) {
        this.resultados = [];
        return;
      }

      try {
        const url = `http://127.0.0.1:8000/buscar?termoBusca=${this.termo}`;
        const response = await axios.get(url);
        this.resultados = response.data;
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    },
  },
};
</script>

<style>
/* ---------------- Configurações Gerais ---------------- */
body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f4f7f6;
  padding: 40px;
  color: #333;
}

/* ---------------- Container Principal ---------------- */
.container {
  max-width: 900px;
  margin: auto;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* ---------------- Título ---------------- */
h1 {
  color: #2c3e50;
  text-align: center;
}

/* ---------------- Caixa de Busca ---------------- */
.search-box {
  width: 100%;
  padding: 12px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box; /* Garante que o padding não aumente a largura */
}

/* ---------------- Tabela ---------------- */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th,
td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  font-size: 14px;
}

th {
  background-color: #3498db;
  color: white;
}

tr:hover {
  background-color: #f1f1f1;
}

/* ---------------- Mensagens de erro ou vazio ---------------- */
.no-results {
  text-align: center;
  color: #7f8c8d;
  margin-top: 20px;
}
</style>
