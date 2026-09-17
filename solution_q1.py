def read_state(filename="input.txt"):
    with open(filename) as f:
        ml, cl, mr, cr, boat = [x.strip() for x in f.readline().split(",")]
    return (int(ml), int(cl), int(mr), int(cr), boat)

# General shi
def person_exists(state, side):
    if side == "R":
        return state[2] > 0 or state[3] > 0
        
    if side == "L":
        return state[0] > 0 or state[1] > 0

def all_possible_options(state, side):
    save_state = state.copy()
    one = 0 
    two = 0 
    three = 0
    four = 0
    
    if side == "R":
        one = 2
        two = 3 
        three = 0
        four = 1
    if side == "L":
        one = 0
        two = 1
        three = 2
        four = 3
        
    save_state[4] = "R" if save_state[4] == "L" else "L"
    
    states = []
        
    # i = 1
    new_state = save_state.copy()
    new_state[one] -= 1
    new_state[three] += 1
    states.append(tuple(new_state))

    new_state = save_state.copy()
    new_state[two] -= 1
    new_state[four] += 1
    states.append(tuple(new_state))
        
    # i = 2
    new_state = save_state.copy()
    new_state[one] -= 2
    new_state[three] += 2
    states.append(tuple(new_state))
        
    new_state = save_state.copy()
    new_state[two] -= 2
    new_state[four] += 2
    states.append(tuple(new_state))
        
    new_state = save_state.copy()
    new_state[one] -= 1
    new_state[three] += 1
    new_state[two] -= 1
    new_state[four] += 1
    states.append(tuple(new_state))
    
    return states    
    
# Prune
def is_valid_state(state):
    m_left, c_left, m_right, c_right, _ = state

    # 1. No negative passenger counts
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    #2. cannibals cannot outnumber missionaries
    if m_left > 0 and c_left > m_left:
        return False

    # 3. Cannibals cannot outnumber missionaries
    if m_right > 0 and c_right > m_right:
        return False

    return True

def prune_list(states):
    return [s for s in states if is_valid_state(s)]    
        
def valid_states(state):
    possible_states = set()
    
    if state[0] == 0 and state[1] == 0:
        return {}
        
    # All possible states moving 1 or 2, then prune those breaking the rules
    if(person_exists(state, state[4])):
        possible_states.update(prune_list(all_possible_options(state, boat)))
       
    return possible_states   
     

def dfs(start):
    # Create state space graph. What is each action available at each state?
    cur_state = start
    
     


def bfs(start):
    raise NotImplementedError


def report(title, result):
    path, cost, expansions = result
    print(f"The solution of {title} is:")
    print(f"Solution Path: {path}")
    print(f"Total cost = {cost}")
    print(f"Number of node expansions = {expansions}")
    print()


if __name__ == "__main__":
    start = read_state()
    report("Q1.1.a (DFS)", dfs(start))
    report("Q1.1.b (BFS)", bfs(start))
