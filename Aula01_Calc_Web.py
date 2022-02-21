#execução de importação

from  flask  import  Flask , request , render_template
from  operacoes  import  adicao , subtracao , multiplicacao , divisao

 app  =  Flask ( __name__ )

 @aplicativo . _ rota ( "/" )
  índice def ():
    return  render_template ( 'index.html' )

 @aplicativo . _ route ( "/calcular" , métodos  = [ "GET" , "POST" ])
  def  calcular ():
    num1   =  int ( request . form [ "num1" ])
    num2   =  int ( request . form [ "num2" ])
    operação  =  pedido . formulário [ "operador" ]
    if  operacao  ==  "somar" :
        return  str ( adicao ( num1 , num2 ))
    elif  operacao  ==  "subtrair" :
        return  str ( subtracao ( num1 , num2 ))
    elif  operacao  ==  "multiplicar" :
        return  str ( multiplicação ( num1 , num2 ))
    mais :
        return  str ( divisão ( num1 , num2 ))


 if  __name__  ==  '__main__' :
    aplicativo . run ( host  =  'localhost' , port  =  5002 , debug  =  True )