import multiprocessing


flag = 0
array = []

def count():
        global flag  
        global array 
        print(array)
        flag += 1  
        array.append(flag)
        

def gl_mass(n):
     for i in range(n):
        count()
        

def main():
        ns = [100, 1000, 123, 213, 234, 653, 352, 234, 542, 122]
        with multiprocessing.Pool(processes=10) as pool:
                results = pool.map(gl_mass, ns)
        print(array)

if __name__ == '__main__':
      main()

