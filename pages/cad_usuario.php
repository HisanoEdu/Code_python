<?php
require_once __DIR__ . '/../controllers/UsuarioController.php';

$objUsuario = new Usuario();

// Cadastrar usuário
if (isset($_POST['cadastrar'])) {
    $nome = $_POST['nome'] ?? '';
    $senha = $_POST['senha'] ?? '';

    $objUsuario->nome = $nome;
    $objUsuario->senha = password_hash($senha, PASSWORD_DEFAULT); // Criptografa a senha

    $res = $objUsuario->cadastrar();

    echo '<script>alert("' . ($res ? 'Cadastro realizado com sucesso!' : 'Falha no cadastro') . '")</script>';
}

// Editar usuário
if (isset($_POST['editar'])) {
    $id = $_POST['id'] ?? '';
    $nome = $_POST['nome'] ?? '';
    $senha = $_POST['senha'] ?? '';

    $objUsuario->id = $id;
    $objUsuario->nome = $nome;
    $objUsuario->senha = password_hash($senha, PASSWORD_DEFAULT); // Criptografa a senha

    $res = $objUsuario->atualizar();
    echo '<script>alert("' . ($res ? 'Editado com sucesso!' : 'Não foi editado') . '")</script>';
}

// Deletar usuário
if (isset($_GET['delete_id'])) {
    $id_user = $_GET['delete_id'];
    $objUsuario->deletar($id_user);
}

// Lista sempre que a página carrega (não precisa do botão "Listar")
$usuarios = $objUsuario->listar_todos();

?>
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciar Usuários</title>
    <script>
        function carregaDados(id, nome, senha) {
            document.getElementById('id').value = id;
            document.getElementById('nome').value = nome;
            document.getElementById('senha').value = senha;
            document.getElementById('submitButton').name = 'editar';
            document.getElementById('submitButton').innerText = 'Editar';
        }
    </script>
</head>

<body>
    <h2>Cadastro de Usuários</h2>
    <div>
        <form method="POST">
            <input type="hidden" id="id" name="id">
            <input type="text" id="nome" name="nome" placeholder="Nome" required>
            <input type="password" id="senha" name="senha" placeholder="Senha" required>
            <button type="submit" name="cadastrar" id="submitButton">Cadastrar</button>
        </form>
    </div>

    <?php if (!empty($usuarios)): ?>
        <h3>Usuários Cadastrados</h3>
        <table border="1" cellpadding="5">
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Senha (hash)</th>
                <th>Ações</th>
            </tr>
            <?php foreach ($usuarios as $usuario): ?>
                <tr>
                    <td><?= htmlspecialchars($usuario['id']) ?></td>
                    <td><?= htmlspecialchars($usuario['nome']) ?></td>
                    <td><?= htmlspecialchars($usuario['senha']) ?></td>
                    <td>
                        <a href="?delete_id=<?= $usuario['id'] ?>" onclick="return confirm('Tem certeza que deseja remover este usuário?')">
                            <img width="20" height="20" src="https://img.icons8.com/ios-glyphs/30/filled-trash.png" alt="Excluir">
                        </a>
                        <button type="button" onclick="carregaDados(
                            '<?= htmlspecialchars($usuario['id']) ?>',
                            '<?= htmlspecialchars($usuario['nome']) ?>',
                            ''
                        )">
                            <img src="https://img.icons8.com/ios-glyphs/30/edit--v1.png" alt="Editar">
                        </button>
                    </td>
                </tr>
            <?php endforeach; ?>
        </table>
    <?php else: ?>
        <p>Nenhum usuário cadastrado.</p>
    <?php endif; ?>
</body>

</html>
