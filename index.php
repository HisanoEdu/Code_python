<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    </head>

    <body>
        <form method="POST" action="./routers/LoginRouter.php?acao=validarLogin">
            <div>
                <input type="text" name="nome" placeholder="nome">
                <input type="text" name="senha" placeholder="senha">
                <Button type="submit">Logar</Button>
            </div>
        </form>
    </body>
    
