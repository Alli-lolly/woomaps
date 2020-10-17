current_states = [0,0,0,0,0] #dining_state, lib_state, guide_state,
#setting_state, building_state, unselect state = 0, select state = 1

#click, then change state
def state_update(need_update, current_states):
    if current_states[need_update] == 0:
        current_states[need_update] = 1
    else:
        current_states[need_update] = 0
    return current_states

#only run the selected option
def select_run(select, state):
    if select == 0: dining(state)
    elif select == 1: lib(state)
    elif select == 2: guide(state)
    elif select == 3: setting(state)
    elif select == 4: building(state)
    else: home_page()

def home_page()

#dining icon show dining color, other icons disappear
def dining_show_color()

#dining building show selected dining color
def building_show_dining_color()

def dining(current_states):
    #if select dining, select dining building
    if current_states[0] == 1:
        dining_show_color()
        building_show_dining_color()
    #if unselect dining, change building and icon to default mode
    else:
        home_page()

#lib icon show lib color, other icons disappear
def lib_show_color()

#lib building show selected lib color
def building_show_lib_color()

def lib(current_states):
    #if select lib, select lib building
    if current_states[1] == 1:
        lib_show_color()
        building_show_lib_color()
    #if unselect lib, change building and icon to default mode
    else:
        home_page()

#guide icon show guide color, other icons disappear
def guide_show_color()

#navigation system
def begin_guide()

def guide(current_states):
    #if select guide, begin guide
    if current_states[2] == 1:
        guide_show_color()
        begin_guide()
    #if unselct guide, close guide
    else:
        home_page()

#show setting menu
def setting_option()

#other options disppear besiedes setting
def show_setting()

def setting(current_states):
    #if select setting, show setting option
    if current_states[3] == 1:
        setting_option()
        show_setting()
    else:
        home_page()

#show a star on the building, show its name below the star
def building_star()

#pop up a box show bulding information
def building_show_info()

def building(current_states):
    #if select building, show building information
    if current_states[4] == 1:
        building_star()
        building_show_info()
    else:
        home_page()

def main():
    global current_states
    home_page()
    while 1==1:
        select = input("dining=0, lib=1, guide=2, setting=3, building=4: ")
        select = int(select)
        current_states = state_update(select, current_states)
        print(current_states)
        select_run(select, current_states)

main()
