import Resources

commands = Resources.db_commands

commands.add('name', 'phone') #Use this command to enter names and numbers of your contacts !pay attention to the formats of number
#use (55)119XXXXXXXX format for Brazil or (1)408XXXXXXX in EUA the THE COUNTRY CODE MUST BE IN PARENTHESES

commands.add_list() #Use this to upload multiple numbers at once, the template file is in assets

commands.remove_phone('phone')#Use this command to remove a contact by number

commands.remove_all_phones()#Use this to remove all contacts from the database

