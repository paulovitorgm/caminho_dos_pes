function bloquear_caracteres_especiais(input) {
    const regex = /[!@#$%^&*()_+{}\[\]:;<>,.?~\/\\=-]/g;
    input.value = input.value.replace(regex, '');
}
function bloquear_numeros(input) {
    const regex = /[0-9]/g;
    input.value = input.value.replace(regex, '');
}
function receber_apenas_letras(input) {
    const regex = /[^a-zA-Z ]/g;
    input.value = input.value.replace(regex, '');
}
function receber_apenas_numeros(input){
     const regex = /[^0-9]/g;
        input.value = input.value.replace(regex, '')
}