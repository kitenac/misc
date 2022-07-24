'''
Cesar V3 - здесь только закодирование на английском.
 1)особенность - каждое слово имеет свой ключ(сдвиг) = длине слова. Словом считается непрерывная строка анг.букв.
 2)Регистр сохраняется
'''

alph = 'abcdefghijklmnopqrstuvwxyz' # 26 символов в алфавите 
module = len(alph)

#-------------Function for saving register
def mask(text):
 mask_ = []
 for ch in text:    
  if alph[0].upper()<=ch<=alph[-1].upper():
    mask_.append(0x1)      # Верхний регистр 
  else:
   mask_.append(0x0)      # Нижний регистр заданного алфавита и ост. символы('.', ',' ...)
  
 return mask_         #список, элементы которого весят по биту
   
#------------Funtion for restoring register 
def unmask(decoded, mask):
 cased = ''
 for i in range(len(mask)):
  if mask[i] == 0x1:    # Верхний регистр:
    cased += decoded[i].upper()
  else:             # Нижний регистр и остальные символы
    cased += decoded[i]
  
 return cased         #Строка с исходным регистром символов

#---------Rotation function
def ROT(ch, trans):
    global alph, module
    ord_sh_in_alpf = alph.find(ch)                        #Номер шифрованной буквы в алфавите
    ord_decod_in_alpf =  (ord_sh_in_alpf-trans) % module  #Номер расшифрованной 
                                                          # Остаток(% - mod)- для зацикливания,
                                                          #  чтоб за границы алфавита не уйти.
    return alph[ord_decod_in_alpf]                                                      


key, flg = 0, 0
decoded = ''

text = input("Type text to encode:\n")
case_mask = mask(text) # Сохраняем регистр букв битовой маской
text = text.lower() 

for i in range(len(text)):
  if text[i] in alph:
     if flg == 0:
       a = i
     key += 1
     flg = 1
  else:
     if flg == 1: # if we came here right after alphebetic symbol
       b = i-1 
       for ch in text[a:b+1]:
        decoded += ROT(ch, -1*key) #-1 gives encode mode(turns transposition to right side)
     
     decoded += text[i]
     key = 0
     flg = 0
     
if flg == 1: # if we came here right after alphebetic symbol
    b = i
    for ch in text[a:b+1]:
       decoded += ROT(ch, -1*key)   
print(f"Encoded text:\n{unmask(decoded, case_mask)}")
