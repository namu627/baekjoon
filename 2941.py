word=input()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia: #크로아티아 알파벳 하나씩 보면서 
        word=word.replace(i,'?') #입력된 단어에 있으면 ?로 바꿔놓기. 특히 'dz='와'z='는 겹칠가능성이 있어서 'dz='를 앞에 둬야 똑바로 실행됨
print(len(word))