function vowelsAndConsonants(s) {
  let consonents = "";
  for (let i of s) {
    if ("aeiou".includes(i)) {
      console.log(i);
    } else {
      consonents += i + "\n";
    }
  }
  console.log(consonents);
}
