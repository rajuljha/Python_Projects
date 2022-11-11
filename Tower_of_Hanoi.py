'''
Description of Tower of Hanoi

Tower of Hanoi is a mathematical game, which has three rules.
All the disks have different sizes.

The goal is to move all the disks from on tower (rod) to another one with the following 3 rules.

    You can only move one disk at the time.
    You can only take the top disk and place on top of another tower (rod).
    You cannot place a bigger disk on top of a smaller disk.
'''
def move(towers , from_tower_no , dest_tower_no):
    disc = towers[from_tower_no].pop()
    towers[dest_tower_no].append(disc)
    return towers
  
def print_towers(towers):
    for i in range(3,0,-1):
        for tower in towers:
            if len(tower) >= i:
                print(tower[i-1],end =' ')
            else:
                print('|',end =' ')
        print()
    print('-----')
    
def solve_tower_of_hanoi(towers, n, start_tower, dest_tower, aux_tower):
    if n == 0:
        return
    #Move subproblem of n-1 disks from start_tower to aux_tower.
    solve_tower_of_hanoi(towers, n-1, start_tower, aux_tower,dest_tower)
    
    #Move disk n to dest_tower.
    move(towers, start_tower , dest_tower)
    print_towers(towers)
    
    #Move subproblem of n-1 from aux_tower to dest_tower.
    solve_tower_of_hanoi(towers, n-1, aux_tower, dest_tower, start_tower)
    
towers = [[3,2,1],[],[]]
print_towers(towers)
solve_tower_of_hanoi(towers,3,0,2,1)
