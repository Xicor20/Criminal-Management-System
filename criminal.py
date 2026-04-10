from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('CRIME MANAGEMENT SYSTEM')

        #variables
        self.case_id = StringVar()
        self.criminal_no = StringVar()
        self.crimetype = StringVar()
        self.name = StringVar()
        self.alias = StringVar()
        self.fathersname = StringVar()
        self.dateofarrest = StringVar()
        self.dateofcrime = StringVar()
        self.birthmark = StringVar()
        self.nationality = StringVar()
        self.occupation = StringVar()
        self.age = StringVar()
        self.gender = StringVar()
        self.wanted = StringVar()

        #Heading
        label_title = Label(self.root,text = 'CRIME MANAGEMENT SYSTEM',font = ('Times New Roman',40,'bold'),bg ='black',fg ='gold')
        label_title.place(x=0,y=0,width =1920,height = 70)

        #crimelogo
        img_logo = Image.open('images/logo.png')
        img_logo = img_logo.resize((100,100),Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image = self.photo_logo)
        self.logo.place(x=490,y=5,width =60,height =60)

        #header frame
        img_frame = Frame(self.root,bd = 2,relief =RIDGE,bg ='white')
        img_frame.place(x=0,y=70,width = 1920,height =180)
        #1st frame img
        img1 =Image.open('images/headimg3.jpg')
        img1 = img1.resize((640,180),Image.ANTIALIAS)
        self.photo1 =ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image = self.photo1)
        self.img_1.place(x=0,y=0,width=640 ,height=180)

        #2nd frame img
        img2 = Image.open('images/headimg2.jpg')
        img2 = img2.resize((640, 180), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=1280, y=0, width=640, height=180)
        #3rd frame img
        img3 = Image.open('images/headimg1.jpeg')
        img3 = img3.resize((640, 180), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=640, y=0, width=640, height=180)

        #main_frame
        main_frame = Frame(self.root,bd = 2,relief =RIDGE,bg ='white')
        main_frame.place (x=10,y=250,width =1890,height =720)

        #upper_frame
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text = 'Criminal Details',font = ('Times New Roman',12,'bold'),bg='white',fg ='red')
        upper_frame.place(x=10, y=10, width=1860, height=300)

        #labels and entry

        # ROW1 #

        #case id
        caseid= Label(upper_frame,text = 'Case ID:',font =('Arial',12,'bold'),bg = 'white')
        caseid.grid(row = 0,column =0,padx =2,sticky = W)

        case_entry = ttk.Entry(upper_frame,textvariable = self.case_id, width =22,font =('Arial',12,'bold'))
        case_entry.grid(row = 0,column =1,padx =2,sticky = W)

        #criminal no.
        lbl_criminal_no = Label(upper_frame,font =('Arial',12,'bold'),text = 'Criminal no:',bg= 'White')
        lbl_criminal_no.grid(row = 0,column =2,padx =2,sticky = W)

        txt_criminal = ttk.Entry(upper_frame,textvariable = self.criminal_no,width=22, font=('Arial', 12, 'bold'))
        txt_criminal.grid(row = 0,column =3,padx =2,sticky = W)

        #Type of crime
        t_crime = Label(upper_frame,font =('Arial',12,'bold'),text = 'Type of Crime:',bg= 'White')
        t_crime.grid(row=0, column=4, padx=2, sticky=W)

        txt_type = ttk.Entry(upper_frame,textvariable = self.crimetype ,width=22, font=('Arial', 12, 'bold'))
        txt_type.grid(row = 0,column =5,padx =2,sticky = W)

        #ROW 2#

        #Criminal Name
        name =Label(upper_frame,font =('Arial',12,'bold'),text = 'Name of Criminal:',bg= 'White')
        name.grid(row=1, column=0, padx=2,pady =7, sticky=W)

        txt_name = ttk.Entry(upper_frame,textvariable = self.name ,width=22, font=('Arial', 12, 'bold'))
        txt_name.grid(row=1, column=1, padx=2,pady =7, sticky=W)

        #Fathers Name
        f_name =Label(upper_frame,font =('Arial',12,'bold'),text = 'Fathers Name:',bg= 'White')
        f_name.grid(row=1, column=4, padx=2, sticky=W)

        txt_fname = ttk.Entry(upper_frame,textvariable = self.fathersname,width=22, font=('Arial', 12, 'bold'))
        txt_fname.grid(row=1, column=5, padx=2, sticky=W)

        # aliases
        lbl_aliases = Label(upper_frame, font=('Arial', 12, 'bold'), text='Aliases:', bg='White')
        lbl_aliases.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_aliases = ttk.Entry(upper_frame,textvariable = self.alias,width=22, font=('Arial', 12, 'bold'))
        txt_aliases.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        #ROW 4#

        # age
        age = Label(upper_frame, font=('Arial', 12, 'bold'), text='Age:', bg='White')
        age.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_age = ttk.Entry(upper_frame,textvariable = self.age ,width=22, font=('Arial', 12, 'bold'))
        txt_age.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # Nationality
        nationality = Label(upper_frame,   font=('Arial', 12, 'bold'), text='Nationality:', bg='White')
        nationality.grid(row=3, column=2, padx=2, sticky=W)

        txt_nationality = ttk.Entry(upper_frame,textvariable = self.nationality ,width=22, font=('Arial', 12, 'bold'))
        txt_nationality.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        #occupation
        occupation = Label(upper_frame,font =('Arial',12,'bold'),text = 'Occupation:',bg= 'White')
        occupation.grid(row = 3,column =4,padx =2,pady = 7,sticky = W)

        txt_occu = ttk.Entry(upper_frame,textvariable = self.occupation ,width =22,font =('Arial',12,'bold'))
        txt_occu.grid(row = 3,column =5,padx =2,pady = 7,sticky = W)

        #ROW 3#

        #Date of arrest
        d_o_arrest =Label(upper_frame,font =('Arial',12,'bold'),text = 'Date of Arrest:',bg= 'White')
        d_o_arrest.grid(row = 2,column =0,padx =2,pady = 7,sticky = W)

        txt_doa = ttk.Entry(upper_frame,textvariable = self.dateofarrest, width =22,font =('Arial',12,'bold'))
        txt_doa.grid(row = 2,column =1,padx =2,pady = 7,sticky = W)

        #date of crime
        d_o_crime = Label(upper_frame,font =('Arial',12,'bold'),text = 'Date of Crime:',bg= 'White')
        d_o_crime.grid(row = 2,column =2,padx =2,pady = 7,sticky = W)

        txt_doc =ttk.Entry(upper_frame,textvariable = self.dateofcrime,width =22,font =('Arial',12,'bold'))
        txt_doc.grid(row = 2,column =3,padx =2,pady = 7,sticky = W)

        #Birthmarks

        birthmarks = Label(upper_frame,font =('Arial',12,'bold'),text = 'Birthmarks:',bg= 'White')
        birthmarks.grid(row = 2,column =4,padx =2,pady = 7,sticky = W)

        txt_bm = ttk.Entry(upper_frame,textvariable = self.birthmark,width =22,font =('Arial',12,'bold'))
        txt_bm.grid(row = 2,column =5,padx =2,pady = 7,sticky = W)

        #ROW 5#

        #gender
        gender = Label(upper_frame,font =('Arial',12,'bold'),text = 'Gender:',bg= 'White')
        gender.grid(row = 4,column =0,padx =2,pady = 7,sticky = W)
        # Radio button gender
        gender_rb = Label(upper_frame,bd=2,relief = RIDGE,bg='White')
        gender_rb.place(x=80,y=150,width=260,height=35)

        male = Radiobutton(gender_rb,text ='Male',value='Male',variable =self.gender,font =('Arial',10,'bold'),bg = 'white')
        male.grid(row = 0,column =0,pady=2,padx=5,sticky =W)
        self.gender.set('Male')

        female = Radiobutton(gender_rb, text='Female', value='Female',variable =self.gender, font=('Arial', 10, 'bold'), bg='white')
        female.grid(row=0, column=1, pady=2, padx=5, sticky=W)
        self.gender.set('Female')

        others = Radiobutton(gender_rb, text='Others', value='Others',variable =self.gender, font=('Arial', 10, 'bold'), bg='white')
        others.grid(row=0, column=2, pady=2, padx=5, sticky=W)
        self.gender.set('Others')


        #most wanted
        most_wanted = Label(upper_frame,font =('Arial',12,'bold'),text = 'Most Wanted:',bg= 'White')
        most_wanted.grid(row = 4,column =2,padx =2,pady = 7,sticky = W)
        # Radio button wanted
        most_wanted_rb = Label(upper_frame, bd=2, relief=RIDGE, bg='White')
        most_wanted_rb.place(x=470, y=150, width=120, height=35)

        yes = Radiobutton(most_wanted_rb, text='yes', value='yes',variable =self.wanted, font=('Arial', 10, 'bold'), bg='white')
        yes.grid(row=0, column=0, pady=2, padx=5, sticky=W)
        self.wanted.set('yes')

        no = Radiobutton(most_wanted_rb, text='no', value='no',variable =self.wanted, font=('Arial', 10, 'bold'), bg='white')
        no.grid(row=0, column=1, pady=2, padx=5, sticky=W)
        self.wanted.set('no')

        #Buttoms
        buttons_frame = Label(upper_frame, bd=2, relief=RIDGE, bg='White')
        buttons_frame.place(x=550, y=200, width=606, height=65)

        #Save Button
        save_button = Button(buttons_frame,command =self.add_data,text='Save Record',font=('Arial', 14, 'bold'), bg='Blue',fg='White')
        save_button.grid(row = 0,column =0,padx =3,pady = 10)

        #update button
        update_button = Button(buttons_frame,command = self.update_data, text='Update Record', font=('Arial', 14, 'bold'), bg='Blue', fg='White')
        update_button.grid(row=0, column=1, padx=3, pady=10)

        #Clear Button
        clear_button = Button(buttons_frame,command =self.clear_data, text='Clear Record', font=('Arial', 14, 'bold'), bg='Blue', fg='White')
        clear_button.grid(row=0, column=2, padx=3, pady=10)

        #Right Side Image
        right_img = Image.open('images/hacker.jpg')
        right_img = right_img.resize((700, 300), Image.ANTIALIAS)
        self.h_photo = ImageTk.PhotoImage(right_img)

        self.r_img = Label(upper_frame, image=self.h_photo)
        self.r_img.place(x=1200, y=0, width=640, height=265)

        #delete Button
        delete_button = Button(buttons_frame,command =self.delete_data, text='Delete Record', font=('Arial', 14, 'bold'), bg='Blue', fg='White')
        delete_button.grid(row=0, column=3, padx=3, pady=10)

        #lower_frame
        lower_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text='Criminal Information Table',
                                 font=('Times New Roman', 12, 'bold'), bg='white', fg='red')
        lower_frame.place(x=10, y=310, width=1860, height=300)

        #search record frame
        search_frame = LabelFrame(lower_frame, bd=2, relief=RIDGE, text='Search Criminal Records',
                                 font=('Times New Roman', 12, 'bold'), bg='white', fg='red')
        search_frame.place(x=10, y=0, width=1830, height=70)

        #serach by
        search_by = Label(search_frame, font=('Arial', 12, 'bold'), text='Search by:', bg='Red', fg='White')
        search_by.grid(row=0, column=0, padx=2, sticky=W)

        self.com_search =StringVar()
        #combo box
        combobox_search = ttk.Combobox(search_frame,textvariable =self.com_search,font=('Arial', 12, 'bold'),width =18,state ='readonly')
        combobox_search['value']=('Select Options','Case_id','Criminal_no','Name')
        combobox_search.current(0)
        combobox_search.grid(row =0,column=1,sticky =W,padx =5)

        self.var_search =StringVar()
        txt_search = ttk.Entry(search_frame,textvariable =self.var_search, width=22, font=('Arial', 12, 'bold'))
        txt_search.grid(row=0, column=2, padx=5, pady=7, sticky=W)

        #search button
        search_button = Button(search_frame,command =self.search_data, text='Search', font=('Arial', 14, 'bold'), width=14, bg='Blue',
                                fg='White')
        search_button.grid(row=0, column=3, padx=5)


        #show all button
        showall_button = Button(search_frame,command = self.fetch_data, text='Show All', font=('Arial', 14, 'bold'),width = 14, bg='Blue', fg='White')
        showall_button.grid(row=0, column=4, padx=5)

        text_crimeagency = Label(search_frame,text = 'Anti-Crime IT Department',font=('Arial', 26, 'bold'),bg ='White',fg='Red')
        text_crimeagency.grid(row=0,column=5,padx=2,sticky =W)
        text_crimeagency.place(x=1000,y=0)

        #table frame
        table_frame = Frame(lower_frame,bd = 2,relief =RIDGE)
        table_frame.place(x=5,y=75,width = 1845,height =200)

        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient = VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame,columns =('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand =scroll_x.set,yscrollcommand =scroll_y.set)

        scroll_x.pack(side =BOTTOM,fill =X)
        scroll_y.pack(side =RIGHT,fill=Y)

        scroll_x.config(command = self.criminal_table.xview)
        scroll_y.config(command = self.criminal_table.yview)

        #Headings
        self.criminal_table.heading('1', text='Case ID')
        self.criminal_table.heading('2', text='Criminal no.')
        self.criminal_table.heading('3', text='Type of Crime')
        self.criminal_table.heading('4', text='Name')
        self.criminal_table.heading('5', text='Aliases')
        self.criminal_table.heading('6', text='Fathers Name')
        self.criminal_table.heading('7', text='Date of Arrest')
        self.criminal_table.heading('8', text='Date of Crime')
        self.criminal_table.heading('9', text='Birthmarks')
        self.criminal_table.heading('10', text='Age')
        self.criminal_table.heading('11', text='Occupation')
        self.criminal_table.heading('12', text='Nationality')
        self.criminal_table.heading('13', text='Gender')
        self.criminal_table.heading('14', text='Wanted')

        self.criminal_table['show'] = 'headings'

        self.criminal_table.column('1',width = 100)
        self.criminal_table.column('2',width = 100)
        self.criminal_table.column('3',width = 100)
        self.criminal_table.column('4',width = 100)
        self.criminal_table.column('5',width = 100)
        self.criminal_table.column('6',width = 100)
        self.criminal_table.column('7',width = 100)
        self.criminal_table.column('8',width = 100)
        self.criminal_table.column('8',width = 100)
        self.criminal_table.column('10',width = 100)
        self.criminal_table.column('11',width = 100)
        self.criminal_table.column('12',width = 100)
        self.criminal_table.column('13',width = 100)
        self.criminal_table.column('14',width = 100)

        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind('<ButtonRelease>',self.get_cursor)


        self.fetch_data()

    #Validating buttons for accepting and mofifying input
    #Add
    def add_data(self):
        if self.case_id == " ":
            messagebox.showerror('Error','Case ID is required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='Gyugda%&357ghjfd',
                                               database='criminal_management_system')
                cursor =conn.cursor()
                cursor.execute('insert into cms values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.case_id.get(),
                    self.criminal_no.get(),
                    self.crimetype.get(),
                    self.name.get(),
                    self.alias.get(),
                    self.fathersname.get(),
                    self.dateofarrest.get(),
                    self.dateofcrime.get(),
                    self.birthmark.get(),
                    self.age.get(),
                    self.occupation.get(),
                    self.nationality.get(),
                    self.gender.get(),
                    self.wanted.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Task Success','Records have been added')
            except EXCEPTION as e:
                messagebox.showerror('Error',f'due to {str(e)}')

    #fetching data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Gyugda%&357ghjfd',
                                               database='criminal_management_system')
        cursor = conn.cursor()
        cursor.execute('select * from cms')
        data = cursor.fetchall()
        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('', END,values = i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event =''):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']

        self.case_id.set(data[0]),
        self.criminal_no.set(data[1]),
        self.crimetype.set(data[2]),
        self.name.set(data[3]),
        self.alias.set(data[4]),
        self.fathersname.set(data[5]),
        self.dateofarrest.set(data[6]),
        self.dateofcrime.set(data[7]),
        self.birthmark.set(data[8]),
        self.age.set(data[9]),
        self.occupation.set(data[10]),
        self.nationality.set(data[11]),
        self.gender.set(data[12]),
        self.wanted.set(data[13])

    #update
    def update_data(self):
        if self.case_id == "":
            messagebox.showerror('Alert','Case ID is required')
        else:
            try:
                update = messagebox.askyesno('Update','Are you sure?') #change the text
                if update > 0:
                    conn =mysql.connector.connect(host='localhost',username='root',password='Gyugda%&357ghjfd',
                                               database='criminal_management_system')
                    cursor = conn.cursor()
                    cursor.execute('update cms set Criminal_no=%s, Type_of_Crime=%s, Name=%s, Aliases=%s, Fathers_Name=%s, Date_of_Arrest=%s, DateofCrime=%s, Birthmarks=%s, Age=%s, Occupation=%s, Nationality=%s, Gender=%s, Wanted=%s where Case_id=%s',
                                   (self.criminal_no.get(),
                                    self.crimetype.get(),
                                    self.name.get(),
                                    self.alias.get(),
                                    self.fathersname.get(),
                                    self.dateofarrest.get(),
                                    self.dateofcrime.get(),
                                    self.birthmark.get(),
                                    self.age.get(),
                                    self.occupation.get(),
                                    self.nationality.get(),
                                    self.gender.get(),
                                    self.wanted.get(),
                                    self.case_id.get()
                                    ))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Task Success','Reords Successfully updated')
            except EXCEPTION as e:
                   messagebox.showerror('Error',f'due to {str(e)}')

    #delete
    def delete_data(self):
        if self.case_id == '':
            messagebox.showerror('Error','Case id is Required')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you sure?')  # change the text
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Gyugda%&357ghjfd',
                                                   database='criminal_management_system')
                    cursor = conn.cursor()
                    sql = 'delete from cms where Case_id =%s'
                    value =(self.case_id.get(),)
                    cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Task Sucees','Records Deleted successfully')
            except EXCEPTION as e:
                messagebox.showerror('Error',f'due to{str(e)}')

    #clear
    def clear_data(self):
        self.case_id.set(''),
        self.criminal_no.set(''),
        self.crimetype.set(''),
        self.name.set(''),
        self.alias.set(''),
        self.fathersname.set(''),
        self.dateofarrest.set(''),
        self.dateofcrime.set(''),
        self.birthmark.set(''),
        self.age.set(''),
        self.occupation.set(''),
        self.nationality.set(''),
        self.gender.set(''),
        self.wanted.set('')

    #search_box
    def search_data(self):
        if self.com_search.get() == '':
            messagebox.showerror('Error','Choose an option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Gyugda%&357ghjfd',
                                               database='criminal_management_system')
                cursor = conn.cursor()
                cursor.execute('select * from cms where ' +str(self.com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except EXCEPTION as e:
                messagebox.showerror('Error', f'due to{str(e)}')



if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()