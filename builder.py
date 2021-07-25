top = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar :
    	title : "Decimal to Binary"

    MDLabel:
        #text: "Content"
        #halign: "center"
'''


input_ = """

MDTextField:
    hint_text : "Enter Decimal Number"
    icon_right : "numeric"
    icon_right_color : app.theme_cls.primary_color
    halign: "left"
    size_hint_x : None
    width : 250
    pos_hint : {"center_x":0.5,"center_y":0.5}
    
"""