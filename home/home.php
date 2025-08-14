<?php
session_start();

if (isset($_SESSION["id_usuario"])) {
    header("Location: ../../index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>

<div class="btn_usuario">
    <form method="POST" action="./routers/home_routers.php?acao=cad_usuario">
        <div class="actions">
            <button class="btn" type="submit">Usuário</button>
        </div>
    </form>
</div>

<div class="btn_logout">
    <form method="POST" action="../../routers/home_routers.php?acao=logout">
        <div class="actions">
            <button class="btn" type="submit">Logout</button>
        </div>
    </form>
</div>

</body>
</html>
