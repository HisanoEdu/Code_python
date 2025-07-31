<?php

$host = "127.0.0.1";

$usuario = "root";

$senha = ""; // corrigido

$bd = "user";

$port = "3306";
 
// Desabilita warnings automáticos do mysqli

mysqli_report(MYSQLI_REPORT_OFF);
 
// Conecta ao banco

$con = @new mysqli($host, $usuario, $senha, $bd, $port);
 
// Verifica se houve erro na conexão

if ($con->connect_error) {

    echo "Erro na conexão: " . $con->connect_error;

} else {

    echo "Conexão realizada com sucesso!";

}

?>

 