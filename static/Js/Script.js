const dvd = document.querySelector("#dado")
    const speed = 3;

    let x = 100, y = 100;
    let dx = speed, dy = speed;

    function moveDVD() {
        const dvdRect = dvd.getBoundingClientRect();
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;

        // Verificar colisões com as bordas
        if (x + dvdRect.width >= windowWidth || x <= 0) {
            dx *= -1; // Inverter direção horizontal
        }
        if (y + dvdRect.height >= windowHeight || y <= 0) {
            dy *= -1; // Inverter direção vertical
        }

        // Atualizar posição
        x += dx;
        y += dy;

        // Aplicar nova posição
        dvd.style.left = x + "px";
        dvd.style.top = y + "px";

        requestAnimationFrame(moveDVD);
    }

    // Iniciar animação
    moveDVD();