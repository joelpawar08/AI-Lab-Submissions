def tower_of_hanoi(n,source,target,auxiliary):
    if n == 1 :
        print(f"Move disk 1 from {source} to {target}")
        print(f"******************************************")
        return
    tower_of_hanoi(n-1,source,auxiliary,target)
    print(f"Move  disk {n} from {source} to {target} ")
    print(f"******************************************")
    tower_of_hanoi(n-1,auxiliary,target,source)

while True:  
    try:
        num_disks=int(input("enter the number of disks\n")) 
        if num_disks > 0:
            print("valid input") 
            break
        else :
            print("invalid input")
    except ValueError:
        print("enter numerical value only")

tower_of_hanoi(num_disks,'A','B','C')
print("End of Excecutions")

