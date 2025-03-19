def is_prime(num):
    count = 0
    for i in range(num):
        if num%(i+1)==0:
            count+=1
    if count == 2:
        return True
    else :
        return False

print(is_prime(1))
print(is_prime(2))
print(is_prime(67))
print(is_prime(108))
print(is_prime(23))