// Isso é um comentario

// Inicio do meu codigo
const btn = document.querySelectorAll('.butao')

btn[0].addEventListener('click',clicou)
btn[1].addEventListener('click',clicou)
btn[3].addEventListener('click',mudarCorFundo)

function clicou (){
        alert("Você clicou aqui")
}
function mudarCorFundo(){
    let color1 = (Math.random(255)*100).toFixed(0);
    let color2 =  (Math.random(255)*100).toFixed(0);
    let color3 = (Math.random(255)*100).toFixed(0);
    
    let cor = 'rgb('+color1+','+color2+','+color3+')'
    
    document.querySelector('body').style.backgroundColor = cor
}

function soma(num1, num2){
    const resultado = num1 + num2
    return resultado
}

function produto(num1, num2){
    const resultado = num1 * num2
    return resultado
}

function divisao(){}
function subtracao(){}
function modulo(){}
function potenciacao(){}


console.log('Soma:', soma(48946,48451))
console.log('Produto:', produto(48946,48451))