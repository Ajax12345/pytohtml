import re

class InvalidFileName(Exception):
    def __str__(self):
        return "Filname must end with '.html'"
class JS:
    def __init__(self, script):
        self.script = script

class CSS:
    def __init__(self, name):
        self.name = name
        self.full_style = []
        self.converter = {"_webkit_transition_duration":"-webkit-transition-duration"}


    def style(self, **kwargs):
        self.starter = '\n'.join([".{}".format(self.name)+" {"]+["{}:{};".format(re.sub('_', '-', tag), quality) for tag, quality in kwargs.items()]+['}'])
        self.full_style.append(self.starter)

    def hover_style(self, **kwargs):
        self.starter = '\n'.join([".{}:hover ".format(self.name)+"{"]+["{}:{};".format(re.sub('_', '-', tag), quality) for tag, quality in kwargs.items()]+['}'])
        self.full_style.append(self.starter)

class Button(CSS):
    def __init__(self, name, text=""):
        self.buttonname = name
        self.text = None
        CSS.__init__(self, self.buttonname)


    def button(self, text, classname, onclick="", width="auto", height="auto", border_radius = "auto", background_color="auto", color="auto", padding="auto", position = "auto", text_align='auto',text_decoration="auto", font_size="auto", margin="auto", margin_top="auto", margin_left="auto", margin_right="auto", margin_bottom="auto"):
        self.buttonname = classname
        self.header = "<button class='{}' onclick = '{}' style='border-radius:{};background-color:{};color:{};padding:{};position:{};text-align:{};text-decoration:{};font-size:{};margin:{};margin-top:{};margin-left:{};margin-right:{};margin-bottom:{};width:{};height:{};'>{}</button>\n\n".format(classname, onclick, border_radius, background_color, color, padding, position, text_align,text_decoration, font_size, margin, margin_top, margin_left, margin_right, margin_bottom, width, height,text)
        #classname, background_color, color, padding, position, text_align,text_decoration, font_size, margin, margin_top, margin_left, margin_right, margin_bottom
    def hover(self, **kwargs):
        self.hover_style(**kwargs)


    def __getattr__(self, name):
        if name.startswith("get_"):
            if name[4:] != self.buttonname:
                raise AttributeError("Incorrect button classname. Did you mean '{}'".format(self.buttonname))

            def wrapper(*args, **kwargs):
                return '\n'.join(self.full_style), self.header

            return wrapper
        else:
            def wrapper(**kwargs):

                self.style(**kwargs)

            return wrapper



class Containers:
    #TODO: add buttons, form, hover
    """
    currently supports:
    <strong>
    <h1> through <h6>
    <p>
    <a> with links
    <body>
    <ol>
    <ul>
    <div> with class and id



    """
    def __init__(self):
        self.filename = None
        self.filecontent = '\n<head>\n<script src="jquery-3.2.1.min.js"></script>\n</head>\n\n'
        self.divs = {0:['', '']}
        self.style = '<style>\n{style}\n</style>'
        self.src = ''
        self.script = '<script src ="{src}"></script>\n<script>{js_code}</script>\n'
        self.current_style = ''
        self.current_script = ''



        '''
    def h1(self, text, color="black", font_size="auto", width="auto", height="auto", text_align="auto", font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", font_weight="auto"):
        """in the format width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, text"""
        h1 = "<h1 style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>{}</h1>".format(width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight, text)

        self.filecontent += '\n'+h1

        '''
    def div(self, name, background_color="auto", border_radius="auto", display="auto", width="auto", height="auto", border="auto", box_shadow="auto",text_align="auto", padding="auto", position='auto', margin="auto", *location):
        top1 = "<div class='{}' style='background-color:{};border-radius:{};border:{};display:{};width:{};height:{};position:{};box-shadow:{};text-align:{};padding:{};margin:{};margin_top:{};margin_bottom:{};margin_left:{};margin_right:{};border-width:{};'>".format(background_color, border_radius, border, display, width, height, position, box_shadow, text-align,margin, martin_top, margin_bottom, margin_left, margin_right)
        if not location:
            self.divs[max(self.divs.keys())+1] = [top1, "</div>"]

        else:
            self.divs[location[0]]
        #background_color, border_radius, border, display, width, height, position, box_shadow, text-align,margin, martin_top, margin_bottom, margin_left, margin_right,

    def a(self, link="#", text="", color="black", font_size="auto", width="auto", height="auto", text_align="auto", font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", font_weight="auto", text_decoration="auto"):

        line = "<a href='{}' style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};text-decoration:{};'>{}</a>".format(link, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight, text_decoration, text)
        self.filecontent += '\n\n'+line





    def __getattr__(self, name):

        if re.findall('^h\d+$|^p\d+$|strong', name):
            def wrapper(text, color="black", font_size="auto", width="auto", height="auto", text_align="auto", font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", font_weight="auto"):

                line = "<{} style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>{}</{}>".format(name, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight, text, name)
                self.filecontent += '\n\n'+line
            return wrapper


        if name == "ol" or name == "ul":
            def wrapper(items = [], width="auto", color="auto", height="auto", font_weight="auto", text_align="auto", font_size="auto",font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", **elements):
                header = "<{} style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>".format(name, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight)
                bottom = "</{}>".format(name)
                full_listing = '\n\n'.join('<li style=color:{};front-size:{};font-family:{};font-weight:{}>{}</li>'.format(c, f, ff, fw, i) for c, f, ff, fw, i in zip(elements.get("colors", ["auto"]*len(items)), elements.get("font", ["auto"]*len(items)), elements.get("font-family", ['auto']*len(items)),  elements.get("font-weight", ['auto']*len(items)), items))
                self.filecontent += '\n'+header+'\n'+full_listing+'\n\n'+bottom
            return wrapper

        raise AttributeError("No HTML tag '{}'".format(name))

class Form(Containers):
    def __init__(self, input_value = None):
        Containers.__init__(self)
        self.input_value = input_value
        self.final_form = "<form action="" method='post'>\n{form_content}\n</form>\n\n\n<input type='submit' value='{value}'>\n"
        self.form = ''


    def input(self, input_type, name, placeholder='', checked="", values='', items=''):
        if input_type == "radio":
            form_vals = "\n<input type='radio' name = '{}' value='{}' checked>{}</br>\n".format(name, values[0], checked)+'\n'.join(["<input type='radio' name = '{}' value='{}'>{}</br>\n".format(name, the_value, the_item) for the_value, the_item in zip(values[1:], items[1:])]) if checked else '\n'.join(["<input type='radio' name = '{}' value='{}'>{}</br>".format(name, the_value, the_item) for the_value, the_item in zip(values, items)])
            self.form += form_vals

        elif input_type == "checkbox":
            if checked:
                header = '\n<input type="checkbox" name="{}" value="{}" checked="checked">{}<br>\n'.format(name, values, checked) if not isinstance(values, list) else '\n<input type="checkbox" name="{}" value="{}" checked="checked">{}<br>\n'.format(name, values[0], checked)+'\n'.join(['\n<input type="checkbox" name="{}" value="{}">{}<br>\n\n' for name, val, t in zip(names, values[1:], items)])
                self.form += header
            else:
                header = '\n<input type="checkbox" name="{}" value="{}">{}<br>\n'.format(name, values, items) if not isinstance(items, list) else '\n'.join(['<input type="checkbox" name="{}" value="{}">{}<br>\n'.format(name, value, t) for value, t in zip(values, items)])
                self.form += header
        else:
            form_vals = '\n<input type="{}" name="{}" placeholder="{}" />\n'.format(input_type, name, placeholder)
            self.form += form_vals

    def select(self, name, values, items):
        self.select_box = "<select name='{name}'>\n{data}\n</select>\n".format(name=name, data = '\n'.join(['<option value="{}">{}</option>\n'.format(i, c) for i, c in zip(values, items)]))

        self.form += self.select_box



    def render_form(self):
        self.final_form = self.final_form.format(form_content=self.form, value='' if not self.input_value else self.input_value)
        return self.final_form

    def __getattr__(self, name):

        if re.findall('^h\d+$|^p\d+$|strong', name):
            def wrapper(text, color="black", font_size="auto", width="auto", height="auto", text_align="auto", font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", font_weight="auto"):

                line = "<{} style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>{}</{}>".format(name, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight, text, name)
                self.form_header += '\n\n'+line
            return wrapper


        if name == "ol" or name == "ul":
            def wrapper(items = [], width="auto", color="auto", height="auto", font_weight="auto", text_align="auto", font_size="auto",font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", **elements):
                header = "<{} style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>".format(name, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight)
                bottom = "</{}>".format(name)
                full_listing = '\n\n'.join('<li style=color:{};front-size:{};font-family:{};font-weight:{}>{}</li>'.format(c, f, ff, fw, i) for c, f, ff, fw, i in zip(elements.get("colors", ["auto"]*len(items)), elements.get("font", ["auto"]*len(items)), elements.get("font-family", ['auto']*len(items)),  elements.get("font-weight", ['auto']*len(items)), items))
                self.form_header += '\n'+header+'\n'+full_listing+'\n\n'+bottom
            return wrapper

        raise AttributeError("No HTML tag '{}'".format(name))


class div:
    def __init__(self, classname=False, idname=False, background_color="auto", background_position="auto", position="auto", background_repeat="auto", border="auto", border_color="auto", border_style="auto", display="auto", the_float="auto", font="auto", font_family="auto", font_size="auto", font_style="auto", font_weight="auto", height="auto", width="auto", margin="auto", margin_left="auto", margin_top="auto", margin_right="auto", margin_bottom="auto", padding="auto", shadow="auto", text_align="auto", text_indent="auto", border_width="auto", border_radius = "auto"):
        if not (classname or idname):
            raise AttributeError("Please provide a div classname or id")
        self.name = classname if classname else idname
        self.isclass = True if classname else False
        self.child = None
        self.children = None

        self.filecontent = '<div {}="{}" style="position:{};background-color:{};background-position:{};background-repeat:{};border:{};border-color:{};border-style:{};display:{};float:{};font:{};font-family:{};font-size:{};font-style:{};font-weight:{};height:{};width:{};margin:{};margin-left:{};margin-top:{};margin-right:{};margin-bottom:{};padding:{};shadow:{};text-align:{};text-indent:{};border-width:{};border-radius:{}">\n\n'.format("class" if self.isclass else "id", self.name, position, background_color, background_position, background_repeat, border, border_color, border_style, display, the_float, font, font_family, font_size, font_style, font_weight, height, width, margin, margin_left, margin_top, margin_right, margin_bottom, padding, shadow, text_align, text_indent, border_width, border_radius)
        self.leaves = []



    def a(self, link="#", text="", color="black", font_size="auto", width="auto", height="auto", text_align="auto", font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", font_weight="auto", text_decoration="auto"):

        line = "<a href='{}' style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};text-decoration:{};'>{}</a>\n".format(link, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight, text_decoration, text)
        self.filecontent += '\n\n'+line

    def upload_html(self, code):
        self.filecontent += '\n'+code

    def __getattr__(self, name):

        if re.findall('^h\d+$|^p\d+$|strong', name):
            def wrapper(text, color="black", font_size="auto", width="auto", height="auto", text_align="auto", font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", font_weight="auto"):

                line = "<{} style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>{}</{}>".format(name, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight, text, name)
                self.filecontent += '\n\n'+line+'\n\n'
            return wrapper


        if name == "ol" or name == "ul":
            def wrapper(items = [], width="auto", color="auto", height="auto", font_weight="auto", text_align="auto", font_size="auto",font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", **elements):
                header = "<{} style='width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};color:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>".format(name, width, height, font_size, text_align, position, font_family, color, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight)
                bottom = "</{}>".format(name)
                full_listing = '\n\n'.join('<li style=color:{};front-size:{};font-family:{};font-weight:{}>{}</li>'.format(c, f, ff, fw, i) for c, f, ff, fw, i in zip(elements.get("colors", ["auto"]*len(items)), elements.get("font", ["auto"]*len(items)), elements.get("font-family", ['auto']*len(items)),  elements.get("font-weight", ['auto']*len(items)), items))
                self.filecontent += '\n'+header+'\n'+full_listing+'\n\n'+bottom
            return wrapper

        raise AttributeError("No HTML tag '{}'".format(name))

    def load_div(self, *div_instance):
        self.leaves.extend(div_instance)
        return self
    def render(self):
        return self.filecontent


class Body(Containers):
    #IDEA: allow user to pass style object
    def __init__(self, background_color="auto", font_size="auto", width="auto", height="auto", text_align="auto", font_family="auto", position="auto", margin="auto", margin_left="auto", margin_right="auto", margin_top="auto", margin_bottom="auto", font_weight="auto"):
        Containers.__init__(self)
        self.closing_brackets = []
        self.body_header = "<body style = 'background-color:{};width:{};height:{};font-size:{};text-align:{};position:{};font-family:{};margin:{};margin-left:{};margin-right:{};margin-bottom:{};margin-top:{};font-weight:{};'>".format(background_color, width, height, font_size, text_align, position, font_family, margin, margin_left, margin_right, margin_bottom, margin_top, font_weight)
        self.closing_brackets.append("</body>")
        self.filecontent += "\n"+self.body_header
        self.code_for_flattening = ''

    def upload_div(self, div_instance):
        self.filecontent += '\n\n'+div_instance

    def set_filename(self, name):
        if not name.endswith(".html"):
            raise InvalidFileName
        self.filename = name

    def create_file(self, write_over=False):
        f = open(self.filename, 'w' if write_over else 'a')
        f.write(self.filecontent)
        f.close()

    def flatten_tree(self, instance, code, count):

        if not instance.leaves:

            yield code+"\n</div>"*(count-1)

        for leaf in instance.leaves:


            new_code = self.flatten_tree(leaf, code+self.div_package(leaf, '', 1), count+1)
            for c in new_code:
                yield c


    def div_package(self, instance, code, count):

        if not instance.child:

            return code + instance.render()+ '\n</div>\n'*count

        return self.div_package(instance.child, code+instance.render(), count+1)

    def upload_css(self, style):
        self.current_style += '\n'+style+'\n'

    def upload_script(self, js):
        if js.endswith('.js'):
            self.src = js
        else:

            self.current_script += '\n'+js+'\n'

    def div_package_children(self, instance):
        top = instance.render()

        if instance.leaves:

            for leaf in instance.leaves:

                top += self.div_package_children(leaf)



        return top+'\n\n</div>\n'

    def upload_button(self, header):
        self.filecontent += '\n'+header+'\n'

    def upload_form(self, form):
        self.filecontent += '\n'+form

    def render(self):
        self.style = self.style.format(style=self.current_style)
        self.script = self.script.format(src = self.src, js_code = self.current_script)
        self.filecontent += '\n'+''.join(self.closing_brackets)
        self.filecontent = "<html>\n"+self.style+'\n' + self.filecontent
        self.filecontent += self.script
        self.filecontent += "\n</html>"
