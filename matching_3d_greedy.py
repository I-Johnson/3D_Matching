# Greedy approximation for 3D matching problem

def greedy_approx(M):
    #sol = []
    count = 0
    selection = []
    for triple in M:
        overlap = False
        for choice in selection:
            if (triple[0] == choice[0] or
                triple[1] == choice[1] or
                triple[2] == choice[2]):
                overlap = True
                break
        if not overlap:
            #sol.append(1)
            count += 1
            selection.append(triple)
        #else:
            #sol.append(0)

    return count


# considerating sorting based on frequency

# arbitrarily prioritize x, y, then z? 
#all 6 permutations of x,y,z?

# other considerations of sorting
def freq_sort(M):
    return



def main():
    
     # X = ["golden", "bulldog", "lab"]
    # Y = ["siamese", "shorthair", "orange"]
    # Z = ["hamster", "capybara", "rat"]

    M = [("golden", "shorthair", "hamster"),
         ("golden", "siamese", "hamster"),
         ("bulldog", "shorthair", "capybara"),
         ("lab", "orange", "rat"),
         ("bulldog", "orange", "hamster")]
        

    #optimal solution will be [0,1,1,1,0]

    print(greedy_approx(M))
    
    
if __name__ == "__main__":
    main()