# Units (1-9) - you already have this
dictA = {
    'i': '1', 'ii': '2', 'iii': '3', 'iv': '4', 'v': '5', 
    'vi': '6', 'vii': '7', 'viii': '8', 'ix': '9'
}

# Tens (10-90) 
dictB = {
    'x': '1',     # 10
    'xx': '2',    # 20
    'xxx': '3',   # 30
    'xl': '4',    # 40
    'l': '5',     # 50
    'lx': '6',    # 60
    'lxx': '7',   # 70
    'lxxx': '8',  # 80
    'xc': '9'     # 90
}

# Hundreds (100-900) 
dictC = {
    'c': '1',     # 100
    'cc': '2',    # 200
    'ccc': '3',   # 300
    'cd': '4',    # 400
    'd': '5',     # 500
    'dc': '6',    # 600
    'dcc': '7',   # 700
    'dccc': '8',  # 800
    'cm': '9'     # 900
}

# Thousands (1000-3000) - Roman numerals typically only go to MMM (3000) max 
dictD = {
    'm': '1',     # 1000
    'mm': '2',    # 2000
    'mmm': '3'    # 3000
}


print( "convert any number from 1 up to 3999 only !!")
print("DO NOT INCLUDE ANY NUNBER WITH ZEROES")
print( "were working on it , but for now just skip the zeroes")
num = input()
A = str(num)
n = len(A)



def looping(y,x):
    z = None
    
    for key , value  in x.items():
        
        if value == y:
            z = key
    
        
    
            
    return z
            
  
  
            
            
            
            
if n == 1:
      L1 =  looping(A[0], dictA)
      print(L1)
      
if n == 2:
        L1 = looping (A[1],dictA)
        
        L2 = looping (A[0], dictB)
        
        print(L2 + L1)
        

if n == 3:
        L1 = looping (A[2], dictA)
        L2 = looping (A[1], dictB)
        L3 = looping (A[0], dictC)
        
        print ( L3 + L2 + L1)
        
        
        
        
if n== 4:
        L1 = looping (A[3], dictA)
        L2 = looping (A[2], dictB)
        L3 = looping (A[1], dictC)
        L4 = looping (A[0], dictD)
        
        print ( L4 + L3 + L2 + L1)
        
    

        
        
        
        
            
            
        
            
            
            
            
            





            
         
         

        