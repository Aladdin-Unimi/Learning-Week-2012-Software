function checkpwd(input){
  if (CryptoJS.SHA1(input.pwd) == "b1b3773a05c0ed0176787a4f1574ff0075f7521e")
    return true;
  return false;
}
