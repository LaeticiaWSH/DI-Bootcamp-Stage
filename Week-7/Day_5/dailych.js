function anagram(a,b){
    a = a.replace(/\s/g, '').toLowerCase()
    b = b.replace(/\s/g, '').toLowerCase()

    const c = a.split('').sort().join('')
    const d = b.split('').sort().join('')

    if (c === d){
        return `${a} is an anagram of ${b}`
    }else{
        return `${a} is not an anagram of ${b}`
    }

}
console.log(anagram("Astronomer","Moon starer"))
console.log(anagram("School master", "The classroom"))
console.log(anagram("The Morse Code", "Here come dots"))
console.log(anagram("Apple", "pale"))





