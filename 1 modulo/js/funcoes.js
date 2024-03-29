function somar(){
    const n1 = Number(document.getElementById('n1').value)
    const n2 = Number(document.getElementById('n2').value)

    const soma = n1 + n1
    document.getElementById('resultado').innerHTML = 'A soma dos números é: ' + soma
}