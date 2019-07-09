
Jeffrey Chen <j.chen14641@gmail.com>
4:21 PM (1 minute ago)
to me

#drinktracker program on iphone, optimized
#for vertical looking
#v1.0 published onto github

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
	
def reset_tap(sender):
	global total
	total=0
	add_button.title=("0 oz today")

view = ui.load_view()                            
view.name = 'Drink Tracker'                             
view.background_color = 'white'  

add_button = ui.Button(title='add water', flex = 'LRTB', font=('<System>',24))
add_button.frame = (0,0,150,110)
add_button.action = button_tapped                
add_button.center = (view.width * 0.5, view.height * 0.45) 

goal_label = ui.Label(frame = (125, 30,125, 140), font = ('<System>', 16), alignment = ui.ALIGN_CENTER)
goal_label.text = "1 gal = 128 oz"

reset_button=ui.Button(title='reset', font = ('<System>', 16))
reset_button.center = (view.width*.75, view.height*2.5)
#reset_button.frame = (0,50,150,160)
reset_button.action=reset_tap

view.add_subview(reset_button)
view.add_subview(goal_label)
view.add_subview(add_button)                             
view.present('sheet')
