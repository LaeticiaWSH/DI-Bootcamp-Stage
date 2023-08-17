let sentence = "The movie is not that bad , I like it."
let wordNot = sentence.indexOf("not")
console.log(wordNot)
let wordBad = sentence.indexOf("bad")
console.log(wordBad)

if (wordNot < wordBad && wordBad != -1 && wordNot != -1){
    txt = sentence.replace("bad","good")
    txt2 = txt.replace("not","")
    txt3 = txt2.replace("that","")
    text = txt3.replace(/\s+/g,' ')

    console.log(text)
} else if (wordNot > wordBad){
    console.log(sentence)
} else if (wordNot < 0 || wordBad < 0)
    console.log(sentence)

