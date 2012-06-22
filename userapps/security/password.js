function main( input ) {
  if (checkpwd(input))
    output("La password " + input.pwd + " è giusta!");
  else
    output("La password " + input.pwd + " è sbagliata.... ;-(");
}

