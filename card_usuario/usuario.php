<?php
require "Database.php";

class Usuario {
    public $id;
    public $nome;
    public $senha;
    public $usuario;

    public function cadastrar() {
        $db = new Database("user");

        $res = $db->insert([
            "nome" => $this->nome, 
            "senha" => $this->senha
        ]);

        return $res;
    }
}
?>

public function listar_todos(){
    $db = new Database ("user");
    $stmt = $db->list();

    $res = $stmt-> fetchALL (PDO::FETCH_ASSOC);

    return $res;
}

