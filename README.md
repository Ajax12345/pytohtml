# pytohtml

## Description

Pytohtml allows developers to quickly, efficiently, and easily create custon HTML pages. Through pyhtml, web design is as simple as calling short class methods.

### Demo
```
body = Body(background_color="#FF8C74", text_align="center")
body.h1("Welcome to my website!", color="blue",font_size="50px")
hobbies = div(classname = "Hobbies", background_color="green", text_align="center", border_radius="10%", width="200px;", height="400xp;")
hobbies.p1("My interests:")
hobbies.ul(items=["Python programming", "C++", "Calculus"], colors = ["yellow", "blue", "red"])
body.upload_div(body.div_package_children(hobbies))
body.render()
body.set_filename("website.html")
body.create_file()
```
### Result
   ![Python Wikipedia Infobox](https://github.com/Ajax12345/pytohtml/blob/master/pythtml/Screen%20Shot%202017-11-15%20at%207.38.20%20PM.png?raw=true)
## Table of Contents

1. Description.
2. Installation.
3. Usage.
4. Bug Reporting.
5. Contributing.
6. Author and Contact.

## Installation

Comming to PyPi shortly

## Usage

### Basic HTML Generation

#### Body Content Creation

To create the main html container, create a body object. `Body` supports most css styling elements, which can be passed to the class constructor:

```
body = pyhtml.Body(background_color="blue", text_align="center")
```
Currently, PyToHtml supports h1-h6 headers and p1- onward paragraph tags. To create a header or paragraph, call the appropriate method:

```
body.h1("Welcome", color="red", font_size="50px")
body.h2("New Website")
body.p2("First content created by PyTOHtml", color="green")
```
### Divs

As of 11/17/17, PyToHtml only supports the div block element. However, spans etc. will be introduced shortly.
To create a div, create a class object:
```
div_content = div(classname="new_div", background_color="green", width="200px", height="100px", margin_left="100px")
```
PyToHtml also supports div id naming:
```
div_content = div(idname ="new_div", background_color="green", width="200px", height="100px", margin_left="100px")
```





