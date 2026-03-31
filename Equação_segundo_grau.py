while True:
 a=float(input("digite o valor do termo a da equação:"))
 if a!=0:  
    b=float(input("digite o valor do termo b da equação, se não houver coloque 0:"))

    if b==0:
     c=float(input("digite o valor do termo c da equação:"))
    
     if c==0:
        print("O valor é da equação é: 0")
     else:
       x=-c/a
       if x < 0:
         print("Não existe raizes reais")
       else:
          x1=(-c/a)**0.5
          x2=-((-c/a)**0.5)      
          print(f"o valor é X1:{x1}")   
          print("o valor é X2:",x2)    
 
    else:
      c=float(input("digite o valor do termo c da equação:"))
      if c==0:
          delta=((b**2)-4*a*c)
          x1= (-b+(delta**0.5))/(2*a)
          x2= (-b-(delta**0.5))/(2*a)
          print("O valor do X1:", x1)
          print("O valor do X2:", x2)          

      else:
          delta=((b**2)-4*a*c)
          if delta<0:
             print("Delta é igual a:", delta)
             print("Não existem raízes reais")

          elif delta == 0:
             print("Delta é igual a:", delta)          
             print("existe só uma raiz real")
             x1= (-b+0)/(2*a)
             print("O valor é da equação é:", x1)

          else:
             print("Delta é igual a:", delta)
             print("existem duas raizes reais")
             x1= (-b+(delta**0.5))/(2*a)
             x2= (-b-(delta**0.5))/(2*a)
             print("O valor do X1:", x1)
             print("O valor do X2:", x2)



 else:
    print("Não aceito o termo a")

