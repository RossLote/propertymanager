from django import forms

def isinstanceany(obj, *args):
    return any([isinstance(obj, arg) for arg in args])

def isinstanceall(obj, *args):
    return all([isinstance(obj, arg) for arg in args])


class BS3Form(forms.Form):
    """
    Bootstrap 3 requires a "form-control" class on every input.
    """
    def __init__(self, *args, **kwargs):
        super(BS3Form, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not isinstanceany(
                field.widget,
                forms.CheckboxInput,
                forms.RadioSelect
            ):
                if field.widget.attrs.has_key('class'):
                    new_class = '%s form-control' % field.widget.attrs['class']
                else:
                    new_class = 'form-control'
                field.widget.attrs['class'] = new_class


class BS3ModelForm(forms.ModelForm):
    """
    Bootstrap 3 requires a "form-control" class on every input.
    """
    def __init__(self, *args, **kwargs):
        super(BS3ModelForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not isinstanceany(
                field.widget,
                forms.CheckboxInput,
                forms.RadioSelect
            ):
                if field.widget.attrs.has_key('class'):
                    new_class = '%s form-control' % field.widget.attrs['class']
                else:
                    new_class = 'form-control'
                field.widget.attrs['class'] = new_class