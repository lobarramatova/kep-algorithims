# Algorithim
# 1. max_1 ni topish
# 2. sonlarni ichidan max_1 ni o'chirish
# 3. qolgan sonlar ichidan max ni topish
def max_2(*args):
    sonlar = list(args)
    max_s = max(sonlar)
    sonlar.remove(max_s)
    return max(sonlar)