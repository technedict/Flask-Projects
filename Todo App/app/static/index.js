const element = document.querySelector('.message');
const elemp = document.getElementById('message')

/* console.log(elemp.innerHTML.trim()) */

if (element.innerHTML.trim() === ''){
    element.classList.add('hide')
}
if (elemp.innerHTML.trim() === 'This field is required.'){
    elemp.innerHTML = "Input cannot be empty"
}
setTimeout(function(){
    element.classList.add('animate__animated', 'animate__fadeOutUp');
}, 5000)

