

"""
# Exercício de PYTHON
# Calculadora inteligente

8. Potência de um número
9. Raiz quadrada de um número
10. Par ou ímpar
11. Números primos
12. Tabuada
13. Fatorial de um número
14. Contagem crescente de 1 a 100
15. Contagem decrescente 100 & 1
16. Exponencial de um número
17. Radiciação
"""

primeiroNumero = int(input("indique um numero inteiro?"))

segundoNumero = int(input("indique um outro numero inteiro?"))
 
operacao = input("Digite qual a operação que deseja:\nAdicao, Subtracao, Multiplicacao , Divisao e o Modulo.\n"
+ "Digite qual a operação que deseja: Sucessor , Antecessor, Equacao1, Equacao2")


soma = primeiroNumero + segundoNumero
subtraccao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero
modulo =  primeiroNumero % segundoNumero

if (operacao == "adicao"):
    print(f"a soma entre %s + %s é =  %s " , primeiroNumero , segundoNumero ,soma)
elif (operacao == "subtraccao"):
    print(f"a soma entre %s - %s é =  %s " , primeiroNumero , segundoNumero ,subtraccao)
elif (operacao == "multiplicacao"):
    print(f"a soma entre %s * %s é =  %s " , primeiroNumero , segundoNumero ,multiplicacao)
elif (operacao == "divisao"):
    print(f"a soma entre %s / %s é =  %s " , primeiroNumero , segundoNumero ,divisao)
elif ("modulo"):
    print(f"a soma entre %s %% %s é =  %s " , primeiroNumero , segundoNumero ,modulo)
elif(operacao == "antecessor"):
    antecessor = print("Quer saber o antecessor do primeiro numero? ou segundo?")
 
 """   
 elif(antecessor.lower()):
                                case "primeiro":
                                    int antecessorPrimeiroNumero = primeiroNumero - 1;
                                    System.out.printf("o seu antecessor do %s é: %s ", primeiroNumero , antecessorPrimeiroNumero);
                                    break;
                                case "segundo":
                                    int antecessorSegundoNumero = segundoNumero - 1;
                                    System.out.printf("o seu antecessor do %s é: %s ", segundoNumero , antecessorSegundoNumero);
                                    break;
                                default:
                                    System.out.println("DESCULPA! mas este texto é invalido.");
                            }
                break;
"""
            case "sucessor":

                System.out.println("Quer saber o sucessor do primeiro numero? ou segundo?");
                String sucessor = input.next();

                switch (sucessor.toLowerCase()) {
                    case "primeiro":
                        int sucessorPrimeiroNumero = primeiroNumero + 1;
                        System.out.printf("o seu sucessor do %s é: %s ", primeiroNumero , sucessorPrimeiroNumero);
                        break;
                    case "segundo":
                        int sucessorSegundoNumero = segundoNumero + 1;
                        System.out.printf("o seu sucessor do %s é: %s ", segundoNumero , sucessorSegundoNumero);
                        break;
                    default:
                        System.out.println("DESCULPA! mas este texto é invalido.");
                }
                break;
            case "equacao1":

                    System.out.println("Equação do 1° grau é toda equação que pode ser expressa na forma ax+b=0, com ‘a’ diferente de zero ");

                    int valorDeXis = (  - ( segundoNumero / primeiroNumero) );

                    print(f"o resultado do calculo da equação do primeiro grau é: " + valorDeXis)

                break;
            case "equacao2":

            print(f"Equação do 2° grau é toda equação que pode ser expressa na forma ax+b=0, com 'a' diferente de zero ")

terceiroNumero = int(print(" %n indique o terceiro numero inteiro?"))
                
                #Fórmula de DELTA
                int(formulaDeDelta = ((segundoNumero*segundoNumero)-((4)*(primeiroNumero)*(terceiroNumero))))

                if(primeiroNumero!=0){

                    if (formulaDeDelta >= 0 ) {

                        // Fórmula de Bhaskara
                        double(xisUm = (((-segundoNumero) + Math.sqrt(formulaDeDelta))/((2)*(primeiroNumero))))
                        double(xisDois = (((-segundoNumero) - Math.sqrt(formulaDeDelta))/((2)*(primeiroNumero))))

                        print(f"Assim, as raízes da equação %s x2 %s x %s = 0 são x1 = %s e x2 = %s " , primeiroNumero , segundoNumero , terceiroNumero ,xisUm ,xisDois )

                    }
                    else
                        print("a equação não possui raízes reais")
                }
                print("numero invalido, !!ESTA OPERAÇÃO NÃO EXISTE!!!")
"""