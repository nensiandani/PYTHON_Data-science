#wap dividing chunks

def divide_chunks(data,size):
    return[data[i:i+size]for i in range(0,len(data),size)]

data=[1,2,3,4,5,6,7,8,9]

chunks=divide_chunks(data,3)

print(chunks)
