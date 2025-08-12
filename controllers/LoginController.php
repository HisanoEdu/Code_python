<?php
require_once __DIR__ . '/../database/Database.php';


class LoginController
{
    private PDO $conn;

    public function __construct()
    {
        $db = new Database("user");
        $this->conn = $db->connect();
        $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }

    /**
     * Valida usuário e senha.
     * @param string $nome
     * @param string $senha
     * @return bool
     */
    public function validarSenha(string $nome, string $senha): bool
    {
        try {
            $sql = "SELECT id, senha FROM user WHERE nome = :nome";
            $stmt = $this->conn->prepare($sql);
            $stmt->execute(['nome' => $nome]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if (!$user) {
                return false; // Usuário não encontrado
            }

            // Verifica senha (hash armazenado no banco)
            if (!password_verify($senha, $user['senha'])) {
                return false;
            }

            // Login bem-sucedido: inicia sessão e armazena o ID
            session_start();
            $_SESSION['id_usuario'] = $user['id'];
            return true;

        } catch (PDOException $e) {
            error_log("Erro no login: " . $e->getMessage());
            return false;
        }
    }
}

    

