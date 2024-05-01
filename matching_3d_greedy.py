# Greedy approximation for 3D matching problem

def greedy_approx(M):
    sol = []
    selection = []
    for triple in M:
        overlap = False
        for choice in selection:
            if (triple[0] == choice[0] or
                triple[1] == choice[1] or
                triple[2] == choice[2]):
                overlap = True
        if overlap:
            sol.append(0)
        else:
            sol.append(1)
            selection.append(triple)
    
    return sol


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
        

    #solution will be [0,1,1,1,0]

    print(greedy_approx(M))
    
    
if __name__ == "__main__":
    main()