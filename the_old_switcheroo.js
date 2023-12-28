function vowel2index(str) {
    let count1 = 0;
    let regex = /[aeiou]/gi
    let strArr = [...str]
    let newStr = []
    strArr.forEach((char)=>{
      if(char.match(regex)){
        newStr.push(count1+1)
      }
      if(!char.match(regex)){
        newStr.push(char)
      }
      count1++
    });
    return newStr.join('')
  }

  console.log(vowel2index("this is my string"))
  console.log(vowel2index("Codewars is the best site in the world"))
  console.log(vowel2index("Tomorrow is going to be raining"))
  console.log(vowel2index(''))