#this is an example of the capabilites of pyhtml

from pyhtml import Body, div, Form, Button

body = Body(background_color="black", text_align="center")
body.h1("Hello, James", color="red",font_size="100px")

body.h3("Please check me out here!", font_size="20px;", color="green")
body.h3("Padding size", color="white")
body.a("http://jamespetullo.pythonanywhere.com/", text_decoration="none", color="yellow", text="ScholarScout")
body.strong("HELLO!!!!", color="orange")
body.ul(items=["Programming", "Python", "C++", "Java"], colors=["red", "blue", "yellow", "green"])
body.ul(items=["Programming", "Math", "Calculus", "Machine Learning"], colors=["red", "orange", "yellow", "green"])

new_div = div(classname="mydiv1", background_color="red", width="500px", height="200px", border_width="20px", border_color="red", margin="0 auto")
new_div.h1("From my first div", color="Orange")
new_div.a("http://jamespetullo.pythonanywhere.com/", color="blue", text="click here")
new_div1 = div(idname="seconddiv", background_color="blue", width="100px", height="200px;")

new_div2 = div(classname="supporter", background_color="green", width="200px", height="100px", border_radius="10px")
new_div2.load_div(div(idname="james1").load_div(div(idname="FUNNY"), div(idname="FUNNY2")), div(classname='Lilly'))
new_div.load_div(new_div1, new_div2)
div_body_code = body.div_package_children(new_div)

button = Button("mybutton")
button.button("PRESS", "mybutton", position="relative", onclick = "myFunction()", color="red", background_color="Blue", width="200px", height="40px", border_radius="10%")
button.mybutton(_webkit_transition_duration= "0.4s", transition_duration="0.4s") #create dict to fix
button.hover(background_color="red", transition_duration="4s")
style, header = button.get_mybutton()
body.upload_css(style)
body.upload_button(header)
script = """
    function myFunction()
    {
        alert('Hello world');
    }
"""
body.upload_script(script)
body.upload_div(div_body_code)
form = Form()
form.input("radio", "james", checked="James", values=["name", 'age', 'address'], items=["James", "17", "10 Sherwood Drive"])
form.input("checkbox", "james1", values=["name1", "name2", "name3"], items=["James", "Joe", "Lilly"])
form.input("password", "james", placeholder="enter your password")

form_code = form.render_form()
form_div = div(classname = "MYFORM", background_color="green", position="absolute", margin_left="20px")
form_div.upload_html(form_code)
div_body_code1 = body.div_package_children(form_div)
body.upload_div(div_body_code1)
body.render()

body.set_filename("pyhtml_generator1.html")
body.create_file(write_over=True)
