const btn = document.getElementById('btn');
function menu(){
    const nav = document.getElementById('nav');
    nav.classList.toggle('ativo')

}
btn.addEventListener('click',menu)