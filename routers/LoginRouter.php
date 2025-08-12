<?php

require_once __DIR__ . '/../controllers/LoginController.php';

$LoginController = new LoginController();

if ($_SERVER['REQUEST_METHOD'] == 'POST'){

    $acao = $_GET['acao'] ;

    switch ($acao) {
        case 'validarLogin':

             echo "<script>console.log('Validando o Usuario' );</script>";
            $output = $LoginController->validarSenha($_POST['nome'] , $_POST['senha'] );        
            $output ?
                header('Location: ../pages/cad_usuario.php'):
                header('Location: ../index.php');
                echo "<script>console.log(' Usuario validado: " . $output . "' );</script>";
            break;

        default:
            echo 'NOT FOUND';
            break;
    }
}


