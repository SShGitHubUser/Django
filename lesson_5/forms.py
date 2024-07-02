from django import forms
from lesson_4.models import Product, User, Order, OrderItem


# Task 2. Login forms

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


# Task 3. Model forms

class ProductForm(forms.ModelForm):
    title = 'Product form'

    class Meta:
        model = Product
        fields = ['name', 'article', 'description', 'price', 'quantity']


class UserForm(forms.ModelForm):
    title = 'User form'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']
        ordering = ['first_name', 'last_name']


class OrderForm(forms.ModelForm):
    title = 'Order form'

    class Meta:
        model = Order
        fields = ['total_price', 'paid']  # 'order_date',


class OrderItemForm(forms.ModelForm):
    title = 'Order item form'

    class Meta:
        model = OrderItem
        fields = ['price', 'quantity', 'quantity']


# Task 4. Review form
class ReviewForm(forms.Form):
    photo = forms.ImageField(required=False)
    email = forms.EmailField(label='E-mail', required=False)
    description = forms.CharField(widget=forms.Textarea, label='Description', required=False)
    rating = forms.ChoiceField(
        choices=((1, "Good"), (2, "Normal"), (3, "Bad")), label='Rating', required=False)
    opinion = forms.BooleanField(label='Is your feedback positive?', required=False)
    phone = forms.CharField(max_length=12, min_length=10, label='Phone number', required=False)
