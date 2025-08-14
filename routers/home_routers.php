<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $acao = $_GET['acao'] ?? ''; // Evita erro caso não exista "acao" na URL

    switch ($acao) {
        case 'cad_usuario':
            header('Location: ../pages/usuario/cad_usuario.php');
            exit();

        case 'logout':
            session_start();
            session_destroy();
            header('Location: ../../index.php');
            exit();

        default:
            echo "NOT FOUND";
            break;
    }
}


