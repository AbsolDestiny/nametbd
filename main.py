import click


def clrscr():
    '''clears the screen'''
    click.clear()

def not_running(key):
    match key:
        case 'quit'|'exit':
            return True
        case _:
            return False


def main():
    
    print('\nYou can exit at any time by typing quit or exit.\n')
    
    running = True

    while running:
        
        continue_state = input('New/Load\n').lower()
        
        if not_running(continue_state) == True:
            running = False
            continue
        
        match continue_state:
            case 'new'|'new game':
                print('\nNew Game\n')
                new_load = 'new'
            case 'load'|'load game':
                print('\nLoading Game\n')
                new_load = 'load'
            case _:
                print('\nThis is not a valid argument!\n')
                continue
        
        clrscr()

        if new_load == 'new':
            player_name = input('\nWhat would you like to be called?')
        elif new_load == 'load':
            pass


if __name__=='__main__':
    main()
