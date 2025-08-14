<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Star Wars Login</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body, html { height: 100%; font-family: 'Orbitron', sans-serif; overflow: hidden; background: black; }

  /* Fundo com estrelas */
  .stars {
    position: fixed;
    width: 100%;
    height: 100%;
    background: black;
    overflow: hidden;
    z-index: -2;
  }
  .star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    animation: twinkle 5s linear infinite;
  }
  @keyframes twinkle {
    0% { opacity: 0.2; }
    50% { opacity: 1; }
    100% { opacity: 0.2; }
  }

  /* Sabres de luz animados */
  .lightsaber {
    position: absolute;
    width: 2px;
    height: 100px;
    background: linear-gradient(to top, red, transparent);
    opacity: 0.7;
    animation: moveSaber 3s linear infinite;
  }
  @keyframes moveSaber {
    0% { transform: translateX(0) translateY(0) rotate(0deg); opacity: 0.5; }
    50% { transform: translateX(300px) translateY(200px) rotate(45deg); opacity: 1; }
    100% { transform: translateX(-300px) translateY(-200px) rotate(-45deg); opacity: 0.5; }
  }

  /* Card de login futurista */
  .login-card {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(0,0,0,0.7);
    padding: 50px 40px;
    border-radius: 12px;
    box-shadow: 0 0 40px #00f6ff, 0 0 80px #ff00ff;
    text-align: center;
    width: 90%;
    max-width: 400px;
    color: #00f6ff;
    border: 1px solid rgba(0,255,255,0.5);
  }

  .login-card h2 {
    font-size: 2.5em;
    margin-bottom: 30px;
    text-shadow: 0 0 10px #00f6ff, 0 0 20px #ff00ff;
  }

  .login-card input {
    width: 100%;
    padding: 15px;
    margin: 10px 0;
    border-radius: 6px;
    border: 1px solid #00f6ff;
    font-size: 16px;
    background: rgba(0,0,0,0.2);
    color: #fff;
    text-shadow: 0 0 5px #00f6ff;
    transition: 0.3s;
  }
  .login-card input:focus {
    outline: none;
    box-shadow: 0 0 10px #ff00ff, 0 0 20px #00f6ff;
    border-color: #ff00ff;
  }

  .login-card button {
    width: 60%;
    padding: 15px;
    margin-top: 20px;
    font-size: 18px;
    color: #000;
    background: linear-gradient(90deg, #00f6ff, #ff00ff);
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    transition: 0.3s;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 0 20px #00f6ff, 0 0 40px #ff00ff;
  }
  .login-card button:hover {
    box-shadow: 0 0 40px #ff00ff, 0 0 80px #00f6ff;
  }

  .login-card p {
    margin-top: 15px;
    font-size: 14px;
    color: #aaa;
  }
  .login-card a {
    color: #00f6ff;
    text-decoration: none;
  }
  .login-card a:hover {
    text-decoration: underline;
  }
</style>
</head>
<body>

<div class="stars" id="stars"></div>

<!-- Sabres animados -->
<div class="lightsaber" style="left:10%; animation-delay: 0s;"></div>
<div class="lightsaber" style="left:50%; animation-delay: 1s;"></div>
<div class="lightsaber" style="left:80%; animation-delay: 2s;"></div>

<!-- Card de login -->
<div class="login-card">
  <h2>STAR LOGIN</h2>
  <form method="POST" action="./routers/LoginRouter.php?acao=validarLogin">
    <input type="text" name="nome" placeholder="Usuário" required>
    <input type="password" name="senha" placeholder="Senha" required>
    <button type="submit">Entrar</button>
  </form>
  <p><a href="#">Esqueci minha senha</a></p>
</div>

<script>
  // Cria estrelas dinamicamente
  const starsContainer = document.getElementById('stars');
  for(let i=0; i<200; i++){
    const star = document.createElement('div');
    star.classList.add('star');
    star.style.top = Math.random() * 100 + '%';
    star.style.left = Math.random() * 100 + '%';
    star.style.width = star.style.height = Math.random() * 3 + 'px';
    star.style.animationDuration = (Math.random() * 5 + 2) + 's';
    starsContainer.appendChild(star);
  }
</script>

</body>
</html>
