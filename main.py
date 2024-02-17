run_program = True

while run_program:
    table_number = int(input("Enter a table number:"))
    interval_start = int(input("Enter an interval start integer:"))
    interval_stop = int(input("Enter an interval stop integer:"))
    print('----------------------')
    print(f'Multiplication table of {table_number}')
    print('----------------------')
    for i in range(interval_start, interval_stop+1):
        print(f'{i:2} * {table_number:2} = {i * table_number:3}')
    print('')

    restart_prompt = True
    while restart_prompt:
        restart = input("Would you like to restart? (y/n): ")
        if restart.lower() == "y":
            restart_prompt = False
            run_program = True
        elif restart.lower() == "n":
            restart_prompt = False
            run_program = False
        else:
            restart_prompt = True
print("Terminated the program!")