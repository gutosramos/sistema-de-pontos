document.getElementById('test-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Pega os valores do formulário
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
  
    // Cria uma nova linha na tabela
    const newRow = `<tr><td>${nome}</td><td>${email}</td></tr>`;
    
    // Insere a nova linha na tabela
    document.getElementById('table-body').insertAdjacentHTML('beforeend', newRow);
  
    // Limpa os campos do formulário
    document.getElementById('nome').value = '';
    document.getElementById('email').value = '';
  });
  