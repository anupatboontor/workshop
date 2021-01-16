string = " Hello, World! "

print(string.upper()) # outout: "HELLO, WORLD! "
print(string.lower()) # output: "hello, world! "
print(string.strip()) # output: "Hello, World!" ตัดspaceตัวหน้าและตัวสุดท้าย
print(string.replace("H","J")) #output: Jello, World! ("เป็นตัวที่เราจะแทนที่","ตัวที่จะมาแทน")
print(string.split(",")) #output: ['Hello',' World! '] 
print(len(string)) # 15