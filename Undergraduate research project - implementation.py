#dissertation - implementation of solution for the knapsack problem
#Ioannis Mizithras


#import libraries

import sys
import csv
from datetime import datetime

########################


#functions
def total_restriction_factor_picked():

    instruction_message = "\ninput the max weight of the container for the items"

    while True:
        print(instruction_message)
        user_input = input()
        if check_int(user_input):
            option = int(user_input)
            if option >= 0:
                return option
            else:
                print(invalid_input_error_message)
        else:
            print(invalid_input_error_message)

def check_int(s):
    if s != "":
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
    return s.isdigit()

def catalogue_picker(catalogue):
    
    catalogue_option_question = "How would you like to import a catalogue of items?\nEnter \'"+\
                              str(file_reading_option)+"\' for reading from the local file.\nEnter \'"+\
                              str(manual_catalogue_import_option)+"\' to import dataset manually.\nEnter \'"+terminate_script_option+"\' to exit the software"
    current_imported_catalogue_question = "Enter \"" + currently_imported_catalogue_option +"\" to use the currently imported dataset"
    while True:
        print(catalogue_option_question)
        if catalogue != []:
            print(current_imported_catalogue_question)
        user_input = input()
        if user_input == str(file_reading_option):
            return file_reading_option
        elif user_input == str(manual_catalogue_import_option):
            return manual_catalogue_import_option
        elif user_input == terminate_script_option:
            return terminate_script_option
        elif user_input == currently_imported_catalogue_option:
            return currently_imported_catalogue_option
        print(invalid_input_error_message)

def new_calculation():
    
    new_calculation_question_message = "Would you like to make another calculation?\nEnter \'"+new_calculation_option+"\' or \'"+terminate_script_option+"\'."
    while True:
        print(new_calculation_question_message)
        user_input = input()
        if user_input == new_calculation_option:
            return True
        elif user_input == terminate_script_option:
            return False
        print(invalid_input_error_message)

def local_catalogue_entry():

    catalogue = [[],[],[]]
    
    local_csv_file = open("item catalogue.csv", encoding = "utf8")
    local_catalogue_csv = csv.reader(local_csv_file)
    next(local_catalogue_csv)
    for row in local_catalogue_csv:
        catalogue[identification_position_in_list].append(row[identification_position_in_list])
        catalogue[value_positions_in_list].append(row[value_positions_in_list])
        catalogue[constrain_positions_in_list].append(row[constrain_positions_in_list])
    local_csv_file.close()
    return catalogue

def manual_catalogue_entry():
    
    initial_instructions_message = "Here you import the catalogue of items you require. You can choose from this catalogue for the calculation later"
    general_instructions_message = "type item identification OR type \""+ terminate_script_option + "\" to exit OR type \""+ completion_option + "\" to complete dataset input"
    value_catalogue_import_instructions_message = "type item value"
    constrain_catalogue_import_instructions_message = "type item weight"
    identification_duplicate_error_message = "!!! This identification has already been used !!!"
    catalogue_empty_error_message = "!!! You have not imported any data to the catalogue. !!!"
    catalogue = [[],[],[]]

    print(initial_instructions_message)
    while True:

        print(general_instructions_message)
        user_input = input()
        if user_input == terminate_script_option:
            return terminate_script_option
        elif user_input == completion_option:
            if catalogue != empty_catalogue:
                return catalogue
            else:
                print(catalogue_empty_error_message)
        else:
            if user_input in catalogue[identification_position_in_list]:
                print(identification_duplicate_error_message)
            else:
                catalogue[identification_position_in_list].append(user_input)
                while True:
                    print(value_catalogue_import_instructions_message)
                    user_input = input()
                    if user_input.isdigit():
                        catalogue[value_positions_in_list].append(int(user_input))
                        while True:
                            print(constrain_catalogue_import_instructions_message)
                            user_input = input()
                            if user_input.isdigit():
                                catalogue[constrain_positions_in_list].append(int(user_input))
                                break
                            else:
                                print(invalid_input_error_message)
                        break
                    
                    else:
                        print(invalid_input_error_message)
                       
def same_item_variables_checker(unckecked_catalogue):

    string_combiner = " / "
    approved_catalogue = [[],[],[]]
    approved_catalogue[0].append(unckecked_catalogue[0][0])
    approved_catalogue[1].append(unckecked_catalogue[1][0])
    approved_catalogue[2].append(unckecked_catalogue[2][0])

    for unckecked_catalogue_index in range(0,len(unckecked_catalogue[identification_position_in_list])): ###range should start at 1 cause we already appened one row
        match_found = False        
        for approved_catalogue_index in range(0,len(approved_catalogue[identification_position_in_list])):
            if unckecked_catalogue[value_positions_in_list][unckecked_catalogue_index] == approved_catalogue[value_positions_in_list][approved_catalogue_index] \
               and unckecked_catalogue[constrain_positions_in_list][unckecked_catalogue_index] == approved_catalogue[constrain_positions_in_list][approved_catalogue_index]:
                    if approved_catalogue[identification_position_in_list][approved_catalogue_index] != unckecked_catalogue[identification_position_in_list][unckecked_catalogue_index]:
                        approved_catalogue[identification_position_in_list][approved_catalogue_index] = approved_catalogue[identification_position_in_list][approved_catalogue_index] + string_combiner\
                                                                                                        + unckecked_catalogue[identification_position_in_list][unckecked_catalogue_index]
                    match_found = True
                    break
        if not match_found:
            approved_catalogue[identification_position_in_list].append(unckecked_catalogue[identification_position_in_list][unckecked_catalogue_index])
            approved_catalogue[value_positions_in_list].append(unckecked_catalogue[value_positions_in_list][unckecked_catalogue_index])
            approved_catalogue[constrain_positions_in_list].append(unckecked_catalogue[constrain_positions_in_list][unckecked_catalogue_index])

    return approved_catalogue

def display_2_collum_list(the_list):
    
    numbering = 0
    if the_list:
        for item in the_list[0]:
            print(str(numbering + 1) + ") "+ str(item) + " ----> "+ str(the_list[ammount_position_in_list][numbering]))
            numbering += 1
        
    return

def item_picker_from_catalogue(item_picker_catalogue):

    initial_instructions_message = "\nNow choose how many of each item you want to use for this calculation"
    general_instruction_message = "\ntype the id of the product ammount you want to modify OR type \""+ completion_option +"\" to proceed to calculation"
    modify_ammount_instruction_message = "\nType how many of this item you want to add. You can also use \"-\" to remove an ammount"
    empty_list_error = "you have not added any items for the calculation"
    items_picked = [[],[]]
    final_items_picked = [[],[]]
    
    for catalogue_i in item_picker_catalogue[identification_position_in_list]:
        items_picked[identification_position_in_list].append(catalogue_i)
        items_picked[ammount_position_in_list].append(0)
    print(initial_instructions_message)
    while True:
        display_2_collum_list(items_picked)
        print(general_instruction_message)
        user_input = input()
        if user_input == completion_option:
            break
        elif user_input.isdigit():
            if int(user_input) >= 1 and int(user_input) <= len(items_picked[0]):
                picked_item_list_position = int(user_input) - 1
                while True:              
                    print(modify_ammount_instruction_message)
                    user_input = input()
                    if check_int(user_input):
                        items_picked[1][picked_item_list_position] += int(user_input)
                        break
                    else:
                        print(invalid_input_error_message)                       
            else:
                print(invalid_input_error_message)
        else:
            print(invalid_input_error_message)
    for counter in range(0,len(items_picked[0])):
        if items_picked[ammount_position_in_list][counter] > 0:
            final_items_picked[identification_position_in_list].append(items_picked[identification_position_in_list][counter])
            final_items_picked[ammount_position_in_list].append(items_picked[ammount_position_in_list][counter])
     
    return final_items_picked

def catalogue_option_fetcher(catalogue,print_access):
    if catalogue_option == file_reading_option:
        catalogue = local_catalogue_entry()
        print_access = True
    elif catalogue_option == manual_catalogue_import_option:
        manual_catalogue_entry_reply = manual_catalogue_entry()
        if manual_catalogue_entry_reply != terminate_script_option:
            catalogue = manual_catalogue_entry_reply
            print_access = True
    elif catalogue_option == currently_imported_catalogue_option:
        print_access = True
    
    return catalogue,print_access

def knapsack_solver(items_picked):

    W = total_restriction_factor_picked()

    item_name = []
    item_value = []
    item_weight = []
    for loop_per_item in range(0,len(items_picked[identification_position_in_list])):
        for y in range(0,len(catalogue[identification_position_in_list])):
            if catalogue[identification_position_in_list][y] == items_picked[identification_position_in_list][loop_per_item]:
                for loop_per_amount in range(0,items_picked[ammount_position_in_list][loop_per_item]):
                    item_name.append(catalogue[identification_position_in_list][y])
                    item_value.append(int(catalogue[value_positions_in_list][y]))
                    item_weight.append(int(catalogue[constrain_positions_in_list][y]))

    number_of_items = len(item_name)
    max_value = [[0 for x in range(W + 1)] for x in range(number_of_items + 1)]
    items_used = [["" for x in range(W + 1)] for x in range(number_of_items + 1)]

    for i in range(number_of_items + 1): 
        for w in range(W + 1):
            
            if i == 0 or w == 0: 
                max_value[i][w] = 0
                items_used[i][w] = empty_sting
            elif item_weight[i-1] <= w:
                if item_value[i-1] + max_value[i-1][w-item_weight[i-1]] > max_value[i-1][w]:
                    max_value[i][w] = item_value[i-1] + max_value[i-1][w-item_weight[i-1]]
                    if items_used[i-1][w-item_weight[i-1]] != empty_sting:
                        items_used[i][w] = items_used[i-1][w-item_weight[i-1]] + string_divider + item_name[i-1]
                    else:
                        items_used[i][w] = items_used[i-1][w-item_weight[i-1]] + item_name[i-1]
                else:
                    max_value[i][w] = max_value[i-1][w]
                    items_used[i][w] = items_used[i-1][w]
            else: 
                max_value[i][w] = max_value[i-1][w]
                items_used[i][w] = items_used[i-1][w]

    listed_items_used = items_used[number_of_items][W].split(string_divider)
    solution = [[],[]]

    for x in range(0,len(listed_items_used)):
        found = False
        for y in range(0,len(solution[identification_position_in_list])):
            if listed_items_used[x] == solution[identification_position_in_list][y]:
                solution[ammount_position_in_list][y] += 1
                found = True
                break
        if not found:
            solution[identification_position_in_list].append(listed_items_used[x])
            solution[ammount_position_in_list].append(1)

    return solution, max_value[number_of_items][W]

def solution_saving_in_file(solution):

    saved_knapsack_solutions_folder_path = "saved knapsack solutions\\"
    saved_file_header = "id                   ammount\n"
    spacer = " -----------> "

    time_now = datetime.now()
    date_string = time_now.strftime("%d-%m-%Y %H-%M-%S")
    file_save_path = saved_knapsack_solutions_folder_path + date_string +".txt"       
    with open(file_save_path, "x") as text_file:
        text_file.write(saved_file_header)
        counter = 0
        for row in solution[0]:
            text_file.write(solution[identification_position_in_list][counter])
            text_file.write(spacer)
            text_file.write(str(solution[ammount_position_in_list][counter]))         
            text_file.write('\n')
            counter += 1
        text_file.close()
        
    return

def knapsack_solution_printer(solution, max_value):

    file_save_code = "save"
    result_message = "\nThis is the optimal solution for your chosen items.\n"
    general_instruction_message = "\nPress \"Enter\" to continue or \""+ file_save_code + "\" to save solution in .txt file"
    max_value_message = "\nThe total value is "

    print(result_message)
    display_2_collum_list(solution)
    print(max_value_message + str(max_value))
    print(general_instruction_message)
    
    user_input = input()
    if user_input == file_save_code:
        solution_saving_in_file(solution)
        
    
    return
        
########################


#main body

catalogue = []
empty_catalogue = [[],[],[]]
file_reading_option = 1
manual_catalogue_import_option = 2
identification_position_in_list = 0
value_positions_in_list = 1
constrain_positions_in_list = 2
ammount_position_in_list = 1
string_divider = "-"
empty_sting = ""
new_calculation_option = "yes"
terminate_script_option = "exit"
currently_imported_catalogue_option = "existing"
completion_option = "done"
invalid_input_error_message = "\n!!! Your input was invalid. !!!"
greeting_message = "=====================================================\nWelcome to the knapsack problem solver 3000 and 1\n"
farewell_message = "\nMay you find peace in your endeavours"

print(greeting_message)

main_loop = True
while main_loop:

    print_access = False
    catalogue_option = catalogue_picker(catalogue)

    if catalogue_option == terminate_script_option:
        break
    else:
        catalogue,print_access = catalogue_option_fetcher(catalogue,print_access)     
        
    if print_access:
        catalogue = same_item_variables_checker(catalogue)
        items_picked = item_picker_from_catalogue(catalogue)
        knapsack_solution, max_value = knapsack_solver(items_picked)
        knapsack_solution_printer(knapsack_solution, max_value)

    main_loop = new_calculation()

user_input = input(farewell_message)
sys.exit()

########################


"""
NOTES:


"""

