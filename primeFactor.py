import math
def primtenyezok(n): 
      
    # Ha a szám osztható kettővel:
    while n % 2 == 0: 
        print(2), 
        n = n / 2

    # Léptessünk végig az összes páratlan számon N gyökéig
    # Csak I ≤ négyzetgyök N-ig szükséges próbálkozni, mivel ha addíg nem talál osztót, akkor a szám prím.
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: # ha N osztható I-vel

            print(i)
            n = n / i 
              
    print(int(n)) 

primtenyezok(350)