// Menu-lateral 
const body = document.querySelector('body')
const sidemenu = body.querySelector('.menu-lateral')
const toggle = body.querySelector('.toggle')
const modo = body.querySelector('.toggle-troca')
const textomodo = body.querySelector('.texto-modo')

    toggle.addEventListener('click', () => {
        sidemenu.classList.toggle('fechar')
    })

    modo.addEventListener('click', () => {
        body.classList.toggle('dark')

        if (body.classList.contains('dark')) {
            textomodo.innerText = "Modo Claro"
        }else {
            textomodo.innerText = "Modo Escuro"
        }
        
    })

