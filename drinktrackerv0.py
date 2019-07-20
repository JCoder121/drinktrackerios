#drinktracker program on iphone 
#v 0.1 test see if it actually can work via xcode
#7/8/19

import ui
import console

testvar = 0
total = 0

def button_tapped(sender):
	global total
	mytext = console.input_alert('enter amount of water: ')
	amount = int(mytext)      
	total += amount
	sender.title = (str(total) + " oz today")

view = ui.load_view()                            
view.name = 'Drink Tracker'                             
view.background_color = 'white'                      
button = ui.Button(title='add water', flex = 'LRTB', font=('<System>',24))
button.frame = (0,0,150,110)
button.action = button_tapped                
button.center = (view.width * 0.5, view.height * 0.45) 

goal_button = ui.Button(title = '1 gal = 128 oz', font = ('<System>', 16))
goal_button.center = (view.width * 0.5, view.height * 0.2)

view.add_subview(goal_button)
view.add_subview(button)                             
view.present('sheet')
