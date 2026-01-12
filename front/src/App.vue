<template>
  <div id="app" class="main-wrapper">
    <main class="main-content">
      <BuscaOperadoras />
    </main>

    <footer class="my-footer">
      <a
        href="https://www.flaticon.com/br/icones-gratis/saude"
        target="_blank"
        rel="noopener noreferrer"
      >
        Favicon criado por Freepik - Flaticon
      </a>
    </footer>
  </div>
</template>

<script>
import BuscaOperadoras from "./components/BuscaOperadoras.vue";

export default {
  name: "App",
  components: {
    BuscaOperadoras,
  },
};
</script>

<style>
/* ---------------- Estilização do Rodapé ---------------- */
.my-footer {
  background-color: #333;
  color: #ffffff;
  text-align: center;
  padding: 5px 0;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  font-size: 12px;
}

.my-footer a {
  color: #f1f1f1;
  text-decoration: none;
  transition: color 0.3s ease;
}

.my-footer a:hover {
  color: #3498db;
  text-decoration: underline;
}
</style>
