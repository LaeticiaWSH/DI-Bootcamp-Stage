let letters = document.getElementById('letters')
letters.addEventListener('input',function(){
    const check = letters.value.replace(/[^a-zA-Z]/g,"")
    letters.value = check
})