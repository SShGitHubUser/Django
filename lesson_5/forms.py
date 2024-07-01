from django import forms
from lesson_4.models import Product, User, Order, OrderItem


class LoginForm(forms.Form):
    username = forms.CharField(label='User name', initial="User", required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, initial="Password", required=False)
    title = 'Simple login form'


class UserTypesLoginForm(forms.Form):
    username = forms.CharField(label='User name', initial="User", required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, initial="Password", required=False)
    user_type = forms.ChoiceField(label='User type', choices=[(1, 'student'), (2, 'teacher'), (3, 'admin')])
    title = 'User types login form'


class EmailLoginForm(forms.Form):
    email = forms.CharField(label='User e-mail', initial="e-mail", required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, initial="Password", required=False)
    title = 'E-mail login form'


class MemoryLoginForm(forms.Form):
    username = forms.CharField(label='User name', initial="User", required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, initial="Password", required=False)
    memory = forms.BooleanField(label='Remember user', required=False)
    title = 'User-remembering login form'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'status']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput()
        }
        labels = {
            'first_name': 'Name',
            'last_name': 'Surname',
            'email': 'E-mail'
        }
        help_texts = {
            'email': 'Enter a valid email address'
        }
        error_messages = {
            'email': {
                'invalid': 'Enter a valid email address'
            }
        }
        required_fields = ['first_name', 'last_name', 'email']
        field_order = ['first_name', 'last_name', 'email']
        readonly_fields = ['first_name', 'last_name']
        filter_fields = ['first_name', 'last_name']
        filtered_fields = ['first_name', 'last_name']
        ordering = ['first_name', 'last_name']
        searchable_fields = ['first_name', 'last_name']
        filter_horizontal = ['groups', 'user_permissions']
        filter_vertical = ['groups', 'user_permissions']
        radio_fields = {'gender': forms.RadioSelect}


class ReviewForm(forms.Form):
    photo = forms.ImageField()
    email = forms.EmailField(label='E-mail')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    rating = forms.ChoiceField(
        choices=((5, "Отлично"), (4, "Хорошо"), (3, "Нормально"), (2, "Плохо"), (1, "Очень плохо")), label='Рейтинг')
    opinion = forms.BooleanField(label='Отзыв положительный?')
    phone = forms.CharField(max_length=12, min_length=10, label='Телефонный номер')
