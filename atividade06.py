def idade_valida(idade): 
     if isinstance(idade, int) and 0 <= idade <= 150:  
        return True  
     return False 

    