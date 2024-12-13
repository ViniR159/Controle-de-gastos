# Controle de Gastos - API Flask

Este projeto consiste em uma API desenvolvida em Python utilizando Flask e SQLAlchemy para gerenciar despesas. A aplicação oferece um CRUD (Create, Read, Update, Delete) completo e utiliza SQLite como banco de dados.

## Funcionalidades
- **Create**: Adicione novos gastos.
- **Read**: Liste todos os gastos ou filtre por ID.
- **Update**: Atualize informações de um gasto.
- **Delete**: Remova um gasto do banco de dados.

## Tecnologias Utilizadas
- **Python**
- **Flask**
- **SQLAlchemy**
- **SQLite**

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- Virtualenv (opcional, mas recomendado)

### Passos para Configuração
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Crie um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script principal:
   ```bash
   python app.py
   ```

5. Acesse a API no navegador ou em um cliente HTTP (como Postman):
   ```
   http://127.0.0.1:5000
   ```

## Rotas Disponíveis

### **GET /gastos**
Lista todos os gastos cadastrados.

#### Exemplo de resposta:
```json
[
  {
    "id": 1,
    "nome": "Almoço",
    "data": "2024-12-13",
    "valor": 25.50
  },
  {
    "id": 2,
    "nome": "Combustível",
    "data": "2024-12-12",
    "valor": 100.00
  }
]
```

### **GET /gasto/<int:Id>**
Filtra um gasto específico pelo ID.

#### Exemplo de resposta:
```json
{
  "id": 1,
  "nome": "Almoço",
  "data": "2024-12-13",
  "valor": 25.50
}
```

### **POST /gastos**
(Crie o endpoint caso não exista) Adiciona um novo gasto ao banco de dados.

### **PUT /gasto/<int:Id>**
(Crie o endpoint caso não exista) Atualiza informações de um gasto específico.

### **DELETE /gasto/<int:Id>**
Remove um gasto pelo ID.

## Melhorias Futuras
- Implementar autenticação com Flask-JWT.
- Adicionar validação de entradas.
- Desenvolver uma interface gráfica ou site para consumir a API.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou submeter um pull request.

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.


![image](https://github.com/user-attachments/assets/acf76f99-5340-46cf-ac79-f08f0acc9749)
