# define a function
# for transcription
def transcript(x) :
    
  # convert string into list
  l = list(x)  
  
  for i in range(len(x)):
  
      if(l[i]=='c'):
          l[i]='G'
  
      elif(l[i]=='G'):
          l[i]='c'
  
      elif (l[i] == 'A'):
          l[i] = 'T'
  
      elif (l[i] == 'U'):
          l[i] = 'A'
  
      else:
          print('Invalid Input')                      
            
  print("Translated RNA : ",end="")      
  for char in l:
      print(char,end="")
  
# Driver code
if __name__ == "__main__":
    
  x = "GCTAA"
  # function calling
  transcript(x)