import json
import math

class Food_items():

    def __init__(self):
        # try if exist
            try :
                with open("items.txt","r") as file:
                    read_items = file.readlines()[0]
                    self.items = json.loads(read_items)
            except: # first load
                self.items = {"food_items":{}}

    def show_item(self):
        item = input('Enter name of item to display details:    ')
        if item in self.items['food_items'].keys():
            print('Item found')
            print(f"Name:{item}          amount:{self.items['food_items'][item]['amount']}         price: {self.items['food_items'][item]['price']}")
            return
        else:
            name = item
            # did u mean ?
            for letter in item:
                choose_list = []
                # check if similar names are in list
                for item_name in self.items['food_items'].keys():
                    if name in item_name: #jat in jatra
                        choose_list.append(item_name)
                if len(choose_list) > 0:
                    print('Not found, other choices are:')
                    for choose in choose_list:
                        print(choose)
                    return
                name = name[:-1]
        print('Nothing found')
        return

    def show_all_items(self):
        for key in self.items['food_items'].keys():
            print(f"Name:{key}          amount:{self.items['food_items'][key]['amount']}         price: {self.items['food_items'][key]['price']}")
        return

    def add_item(self,*args):
        if len(args) == 0:
            item_name = input('Name of item: ')
        else:
            print(args[0])
            item_name = args[0]

        if  item_name in self.items['food_items'].keys():
            print('This item already exist')
            return

        while True:
            try:
                item_amount = float(input('Amount of product:     '))
                break
            except:
                print('must be integer')

        while True:
            unit = input("unit p(piece)/kg(kilogram)/l(liter)")
            if unit == 'p' or unit == 'kg' or unit == 'l':
                break

        while True:
            try:
                item_price = float(input('price for one piece[kc]:    '))
                break
            except:
                print('must be integer')

        self.items['food_items'][item_name] = {'price':item_price,'amount':str(item_amount)+unit}
        with open('items.txt','w') as file:
            save_items = json.dumps(self.items)
            file.write(save_items)
        return

    def edit_item(self):
        item = input('Item you want to edit:    ')
        if item in self.items['food_items'].keys():
            print('Item found')
            while True:
                print(f"current values are name: {item} prince: {self.items['food_items'][item]['price']} amount: {self.items['food_items'][item]['amount']}")
                user_input = input('What do u want to edit ? type: name/price/amount .. or quit for return:  ')
                if user_input == 'name':
                    edit_name = input("new name:    ")
                    if edit_name in self.items['food_items']:
                        print('Name already exist')
                    else:
                        with open('items.txt','w') as file:
                            self.items['food_items'][edit_name] = {'price':self.items['food_items'][item]['price'],'amount':self.items['food_items'][item]['amount']}
                            self.items['food_items'].pop(item)
                            save_items = json.dumps(self.items)
                            file.write(save_items)
                        break

                elif user_input == 'price':
                    while True:
                        try:
                            edit_price = float(input("New price: "))
                            break
                        except:
                            print('must be integer')

                    with open('items.txt','w') as file:
                        self.items['food_items'][item]['price'] = edit_price
                        save_items = json.dumps(self.items)
                        file.write(save_items)
                    break

                elif user_input == 'amount':
                    while True:
                        try:
                            edit_amount = float(input('New amount: '))
                            break
                        except:
                            print('must be integer')
                    while True:
                        unit = input("unit p(piece)/kg(kilogram)/l(liter)")
                        if unit == 'p' or unit == 'kg' or unit == 'l':
                            break

                    with open('items.txt','w') as file:
                        self.items['food_items'][item]['amount'] = str(edit_amount)+unit
                        save_items = json.dumps(self.items)
                        file.write(save_items)

                elif user_input == 'quit':
                    break
        else:
            print('Item not found')
        return



    def delete_item(self):
        item_delete = input('Input name of the item you want to delete:     ')
        if item_delete in self.items['food_items']:
            self.items['food_items'].pop(item_delete)
            print('item deleted')
            with open('items.txt','w') as file:
                save_items = json.dumps(self.items)
                file.write(save_items)
        else:
            print('Product not found')
        return


class Recipes():

    def __init__(self):
        # try if exist
            try :
                with open("recipes.txt","r") as file:
                    read_recipes = file.readlines()[0]
                    self.recipes = json.loads(read_recipes)
            except: # first load
                self.recipes = {"recipes":{}}

    def show_recipe(self):
        name = input('Recipe you want to see:   ')
        if name in  self.recipes['recipes']:
            print(name)
            print(f"number of servs: {self.recipes['recipes'][name]['serving']}")
            for key in self.recipes['recipes'][name]['items']:
                print(f"{key}, val: {self.recipes['recipes'][name]['items'][key]}")
        else:
            print('Sorry, recipe not found')
        return


    def show_all_recipes(self):
        for key in self.recipes['recipes']:
            print(key)
        return


    def add_recipe(self):
        name = input('Name of the recipe:   ')
        while True:
            try:
                number_serving = float(input('How many servs is made by this recipe:  '))
                break
            except:
                print('must be integer')
        self.recipes['recipes'][name] = {'serving':number_serving,'items':{}}
        print('Add items required for recipe')
        while True:
            item_name = input('Name of item? ("complete" if the item list is complete):     ')
            if item_name == 'complete':
                with open('recipes.txt','w') as file:
                    save_items = json.dumps(self.recipes)
                    file.write(save_items)
                    break

            if item_name not in Food_items().items['food_items'].keys():
               print('Item is missing, please add item :')
               Food_items().add_item(item_name)

            while True:
                try:
                    value = float(input('how many is needed?:    '))
                    # add unitss
                    if 'kg' in Food_items().items['food_items'][item_name]['amount']:
                        self.recipes['recipes'][name]['items'][item_name] = str(value)+'kg'
                    if 'l' in Food_items().items['food_items'][item_name]['amount']:
                        self.recipes['recipes'][name]['items'][item_name] = str(value)+'l'
                    if 'p' in Food_items().items['food_items'][item_name]['amount']:
                        self.recipes['recipes'][name]['items'][item_name] = str(value)+'p'
                    break
                except:
                    print('must be integer')

        return


    def edit_recipe(self):
        recipe_input = input('Name of recipe you wish to edit?:   ')
        if recipe_input in self.recipes['recipes']:
            while True:
                action = input("'name' for change name, 'add' to add item to recipe 'del' to delete item from recipe 'serv' to change number of serving, 'leave' for leave ")
                if action == 'add':
                    add_item = input('What item do u want to add?:      ')
                    if add_item not in Food_items().items['food_items'].keys():
                       print('Item is missing, please add item :')
                       Food_items().add_item(add_item)
                    while True:
                        try:
                            # add unitss
                            add_value = float(input('how many of this item is needed ?'))
                            if 'kg' in Food_items().items['food_items'][add_item]['amount']:
                                self.recipes['recipes'][recipe_input]['items'][add_item] = str(add_value)+'kg'
                            if 'l' in Food_items().items['food_items'][add_item]['amount']:
                                self.recipes['recipes'][recipe_input]['items'][add_item] = str(add_value)+'l'
                            if 'p' in Food_items().items['food_items'][add_item]['amount']:
                                self.recipes['recipes'][recipe_input]['items'][add_item] = str(add_value)+'p'
                            break
                        except:
                            print('must be integer')

                    with open('recipes.txt','w') as file:
                        save_items = json.dumps(self.recipes)
                        file.write(save_items)

                elif action == 'del':
                    delete_item = input('What item do u want to delete?:    ')
                    if delete_item in self.recipes['recipes'][recipe_input]['items']:
                        self.recipes['recipes'][recipe_input]['items'].pop(delete_item)
                        with open('recipes.txt','w') as file:
                            save_items = json.dumps(self.recipes)
                            file.write(save_items)
                    else:
                        print('item not is not part of this recipe')

                elif action == 'serv':
                    while True:
                        try:
                            serv_edit = float(input('Select new number of serving:   '))
                            break
                        except:
                            print('must be integer')
                    self.recipes['recipes'][recipe_input]['serving'] = serv_edit
                    with open('recipes.txt','w') as file:
                        save_items = json.dumps(self.recipes)
                        file.write(save_items)

                elif action == 'name':
                    new_name = input('please select a new name:     ')
                    if new_name in self.recipes['recipes']:
                        print('name of recipe already exist')
                    else:
                        self.recipes['recipes'][new_name] = self.recipes['recipes'][recipe_input]
                        self.recipes['recipes'].pop(recipe_input)
                        print(self.recipes['recipes'])
                        with open('recipes.txt','w') as file:
                            save_items = json.dumps(self.recipes)
                            file.write(save_items)
                            break

                elif  action == 'leave':
                    return
        else:
            print('Sorry recipe not found')
        return


    def delete_recipe(self):
        delete_name = input('please enter name of recipe you want to delete: ')
        if delete_name in self.recipes['recipes']:
            self.recipes['recipes'].pop(delete_name)
            with open('recipes.txt','w') as file:
                save_items = json.dumps(self.recipes)
                file.write(save_items)
        else:
            print('sorry, not found')
        return


class My_shopping_list():
    def __init__(self):
        self.list = {}

    def show_list(self):
        list_price = 0
        for key in self.list:
            try:
                default_price = Food_items().items['food_items'][key]['price']
                amount = Food_items().items['food_items'][key]['amount']
            except:
                print(f"{key} is not foud in item list, add and try again")
                return
            # check what unit is it then make total price
            if amount[-1] == 'l':
                total_price = math.ceil(float(self.list[key][:-1]))*float(default_price)
                print(f"{key}  {math.ceil(float(self.list[key][:-1]))}l  {total_price}kč")
                list_price = list_price + int(total_price)

            elif amount[-1] == 'p':
                total_price = math.ceil(float(self.list[key][:-1]))*float(default_price)
                print(f"{key}  {math.ceil(float(self.list[key][:-1]))}p  {total_price}kč")
                list_price = list_price + int(total_price)

            elif amount[-2:] == 'kg':
                total_price = float(self.list[key][:-2])/float(amount[:-2])*int(default_price)
                print(f"{key}  {self.list[key]}  {total_price}kč")
                list_price = list_price + total_price
        else:
            print('-----------------------')
            print(f'total price for all items is : {list_price}')





    def add_recipe(self):
        add_recipe = input('select recipe you want to add:  ')

        if add_recipe in Recipes().recipes['recipes']:
            my_serv = input('select how many serves you want to make:   ')
            recipe_serv = Recipes().recipes['recipes'][add_recipe]['serving']
            items = Recipes().recipes['recipes'][add_recipe]['items']
            for item in items.keys():
                # how many of this item i need
                if items[item][-1] =='l':
                    need = float(items[item][:-1])/float(recipe_serv)*float(my_serv)

                    if item in self.list.keys(): # stack same items
                        need = float(self.list[item][:-1]) + need
                        self.list[item] =  f'{need}l'
                    else:
                        self.list[item] = f'{need}l'

                elif items[item][-1] =='p':
                    need = float(items[item][:-1])/float(recipe_serv)*float(my_serv)
                    if item in self.list.keys(): # stack same items
                        need = float(self.list[item][:-1]) + need
                        self.list[item] =  f'{need}p'
                    else:
                        self.list[item] = f'{need}p'

                elif items[item][-2:] == 'kg':
                    need = float(items[item][:-2])/float(recipe_serv)*float(my_serv)
                    if item in self.list.keys(): # stack same items
                        need = float(self.list[item][:-2]) + need
                        self.list[item] =  f'{need}kg'
                    else:
                        self.list[item] = f'{need}kg'

        else:
            print('recipe not found')
        return


    def new_list(self):
        self.list = {}
        return


if __name__ == '__main__':
    print('******************************************************************************')
    print('This app is for make your shopping list by just picking your favorite Recipes!')
    print('******************************************************************************')
    shop_list = My_shopping_list()
    while True:
        print('*********************************************')
        print("Write 'items' to edit your item list ")
        print("Write 'recipes' to edit your recipe list")
        print("Write 'list' to make your shopping list")
        print("Write 'quit' to close app")
        action = input()
        if action == 'items':
            while True:
                print('*********************************************')
                print("write 'add' to add item to your food list ")
                print("write 'delete' to delete item in your food list ")
                print("write 'edit' to edit item in your food list ")
                print("write 'show' to show detail info about item ")
                print("write 'show list' to show all items in your list ")
                print("write 'back' to return ")
                action = input()

                if action == 'add':
                    Food_items().add_item()
                elif action == 'delete':
                    Food_items().delete_item()
                elif action == 'edit':
                    Food_items().edit_item()
                elif action == 'show':
                    Food_items().show_item()
                elif action == 'show list':
                    Food_items().show_all_items()
                elif action == 'back':
                    break

        elif action == 'recipes':
            while True:
                print('*********************************************')
                print("write 'add' to add recipe to your recipe list ")
                print("write 'delete' to delete recipe in your recipe list ")
                print("write 'edit' to edit recipe in your recipe list ")
                print("write 'show' to show detail info about recipe ")
                print("write 'show list' to show all recipes in your recipe list ")
                print("write 'back' to return ")
                action = input()
                if action == 'add':
                    Recipes().add_recipe()
                elif action == 'delete':
                    Recipes().delete_recipe()
                    shop_list = My_shopping_list()
                elif action == 'edit':
                    Recipes().edit_recipe()
                    shop_list = My_shopping_list()
                elif action == 'show':
                    Recipes().show_recipe()
                elif action == 'show list':
                    Recipes().show_all_recipes()
                elif action == 'back':
                    break


        elif action == 'list':
            while True:
                print('*********************************************')
                print("write 'add' to add recipe to your list")
                print("write 'show' to show your shopping list")
                print("write 'reset' to reser your shopping list")
                print("write 'back' to return ")
                action = input()
                if action == 'add':
                    shop_list.add_recipe()
                elif action == 'show':
                    shop_list.show_list()
                elif action == 'reset':
                    shop_list.new_list()
                elif action == 'back':
                    break
        elif action == 'quit':
            break
