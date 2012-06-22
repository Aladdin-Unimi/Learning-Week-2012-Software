function checkpwd(input){
  for (var i=0; i<10000; i++)
  if (CryptoJS.SHA1(input.pwd+i) == "eebe0428ed68d0f4f3d9eaf9ed4cb143091d631c")
    return true;
  return false;
}
