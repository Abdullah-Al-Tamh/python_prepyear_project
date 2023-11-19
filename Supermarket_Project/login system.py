def save_the_data_signup():
    global The_indicator
    The_SQL = sqlite3.connect('users.db')
    The_indicator = The_SQL.cursor()

    The_indicator.execute('''
            CREATE TABLE IF NOT EXISTS The_user (
            data_user TEXT NOT NULL,
            data_user_password TEXT NOT NULL)'''
                          )
    data_user = user_entre.get()
    data_user_password = password_enter.get()
    if data_user != '' and data_user_password != '':
        The_indicator.execute('SELECT data_user FROM The_user WHERE data_user=?', [data_user])
        The_indicator.execute('SELECT data_user_password FROM The_user WHERE data_user_password=?',
                              [data_user_password])
        if The_indicator.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists.')
        else:
            passwordENCODED = data_user_password.encode('utf-8')
            passwordHsh = bcrypt.hashpw(passwordENCODED, bcrypt.gensalt())
            The_indicator.execute('INSERT INTO The_user VALUES (?,?)', [data_user_password, passwordHsh])
            The_SQL.commit()
            messagebox.showinfo('Success', 'Account has been created.')
    else:
        messagebox.showerror('Error', 'Enter all data.')


def Data_for_Login():
    data_user = user_entre.get()
    data_user_password = password_enter.get()
    if data_user != '' and data_user_password != '':
        The_indicator.execute('SELECT data_user FROM The_user WHERE data_user=?', [data_user])
        The_indicator.execute('SELECT data_user_password FROM The_user WHERE data_user_password=?',
                              [data_user_password])
        The_result = The_indicator.fetchone()
        if The_result:
            if bcrypt.checkpw(data_user_password.encode('utf-8'), The_result[0]):
                messagebox.showinfo('Success', 'Your logged-in successfully.')
                self.pack_forget()
                The_controller_pages.get_page('Secondry_page').pack()
            else:
                messagebox.showerror('Error', 'Wrong password.')
        else:
            messagebox.showerror('Error', 'Wrong username.')
    else:
        messagebox.showerror('Error', 'Empty data')