alert('Boas vindas ao jogo do número secreto');
let numeroMaximo = 5000;
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1)
console.log(numeroSecreto);
let chute;
let tentativas = 1;


//enquanto o chute nao for igual o n.s 
    while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 e ${numeroMaximo}`);
    //se o chute for igual ao numero secreto
    if (chute == numeroSecreto) {
        break;
        
    } else {
        if (chute > numeroSecreto) {
            alert(`o número secreto é menor que ${chute}`);
        } else {
            alert(`o número secreto é maior que ${chute}`);
        }
        //tentativas = tentativas +1;
        tentativas++;
    }
}
//operador ternario 
let palavratentativa = tentativas > 1 ? 'tentativas' : 'tentativa'
alert(`Isso ai! você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavratentativa}.`);
// if(tentativas > 1 ) {
//    alert(`Isso ai! você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas.`);
// } else {
// alert(`Isso ai! você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativa.`);
// }