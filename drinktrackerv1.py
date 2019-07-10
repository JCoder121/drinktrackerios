#drinktracker program on iphone, optimized
#for vertical looking
#v1.1 published onto github
#v1.2 working on getting everything into the middle, editing button/label frames

import ui
import console

total = 0

def button_tapped(sender):
	global total
	mytext = console.input_alert('enter amount of water: ')
	amount = int(mytext)      
	total += amount
	sender.title = (str(total) + " oz today")
	
def reset_tap(sender):
	global total
	total=0
	add_button.title=("0 oz today")
	
w, h = ui.get_screen_size()
x_middle = w/2

view = ui.View(frame = (0,0,w,h))                            
view.name = 'Drink Tracker'                             
view.background_color = 'white'  

add_button = ui.Button(title='add water', flex = 'LRTB', font=('<System>',24))
add_button.frame = (0,0,w,h/2)
add_button.action = button_tapped                
add_button.center = (x_middle, h/2.25) 

goal_label = ui.Label(frame = (0, 0,w,h), font = ('<System>', 16), alignment = ui.ALIGN_CENTER)
goal_label.text = "1 gal = 128 oz"
goal_label.center=(x_middle,h/8)

reset_button=ui.Button(title='reset', font = ('<System>', 16))
reset_button.center = (x_middle, h/1.5)
reset_button.action=reset_tap

view.add_subview(reset_button)
view.add_subview(goal_label)
view.add_subview(add_button)                             
view.present('sheet')
