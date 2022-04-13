def run():
    # square = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         square.append(i**2)
    
    #square = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    square = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print(square)

if __name__=='__main__':
    run()