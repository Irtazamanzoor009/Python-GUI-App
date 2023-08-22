from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.messagebox as msg
from SignUpBL import SignUp_BL
from MUserDL import MUser_DL
from SignInBL import SignIn_BL
from ProductsDL import Products_DL
from ProductsBL import Products_BL
from ManagerBL import Manager_BL
from tkinter import font
from CustomerCartDL import CustomerCart_DL
from CustomerBL import Customer_BL
listofpages = []
indexeslist = []
class GUIApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x800")
        self.root.title("Grocery Store Management System")
        self.current_page = None
        MUser_DL.ReadUserFromFile("Users.txt")
        Products_DL.ReadProductFromFile("Products.txt")
        CustomerCart_DL.ReadCustomerCart("cart.txt")
        
        self.SignInPage = SignInPage(self.root)
        self.SignUpPage = SignUpPage(self.root)
        self.AdminPage = AdminPage(self.root)
        self.ViewProductsPage = ViewProductsPage(self.root)
        self.AddProductsPage = AddProductsPage(self.root, self.ViewProductsPage)
        self.UpdateProductsPage = UpdateProductsPage(self.root, self.ViewProductsPage)
        self.DeleteProductsPage = DeleteProductsPage(self.root, self.ViewProductsPage, self.UpdateProductsPage)
        

        self.UpdateProductsPage.set_delete_page(self.DeleteProductsPage)

        self.UserPage = UserPage(self.SignInPage,None)
        
        self.ViewCartUser = ViewCartUser(None)
        self.ViewProductsPageUser = ViewProductPageUser(self.root, self.SignInPage)
        self.Changecart = ChangeCart(None)
        
        #self.ViewProductsPage.set_delete_page(self.SignInPage)
        self.SignInPage.pack(side=TOP, fill=BOTH, expand=True)
        self.SignUpPage.pack(side=TOP, fill=BOTH, expand=True)
        self.AdminPage.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.ViewProductsPage.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.AddProductsPage.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.DeleteProductsPage.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.UpdateProductsPage.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.UserPage.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.ViewProductsPageUser.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.ViewCartUser.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.Changecart.pack(side = TOP, fill = BOTH, expand = TRUE)
        self.show_page(self.SignInPage)

        
    def show_page(self, page):
        self.SignInPage.pack_forget()
        self.SignUpPage.pack_forget()
        self.AdminPage.pack_forget()
        self.ViewProductsPage.pack_forget()
        self.AddProductsPage.pack_forget()
        self.DeleteProductsPage.pack_forget()
        self.UpdateProductsPage.pack_forget()
        self.UserPage.pack_forget()
        self.ViewProductsPageUser.pack_forget()
        self.ViewCartUser.pack_forget()
        self.Changecart.pack_forget()
        for item in listofpages:
            item.pack_forget()
        page.pack(side=TOP, fill=BOTH, expand=True)
        page.tkraise()

    def run(self):
        self.root.mainloop()
        
class Functions():
    
    @staticmethod
    def ShowImageOnLogin(self,imgname):
        self.img = Image.open(imgname)
        self.img_resize = self.img.resize((500,500))
        self.photo = ImageTk.PhotoImage(self.img_resize)
        self.lblImage = Label(self,image=self.photo)
        self.lblImage.place(x=5, y = 100)
        
    @staticmethod
    def UpperLabel(self):
        self.lbl = Label(self, text="Grocery Store Management System", bg="Light blue", fg="black", font="Serif 30 bold", pady=10)
        self.lbl.pack(side=TOP, fill=X)
        self.grid_columnconfigure(0, weight=1)
    
    @staticmethod
    def AdminSideFrame(self, imgname, Fx_pos, Fy_pos, text, Lx_pos, Ly_pos):
        self.Adminframe = Frame(self, width=350, height=650, bg="white smoke")
        self.Adminframe.place(x = Fx_pos, y = Fy_pos)
        
        self.img = Image.open(imgname)
        self.img_resize = self.img.resize((300,300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.img_resize)
        self.lblImage = Label(self.Adminframe,image=self.photo,bg="White smoke")
        self.lblImage.place(x=25, y = 70)
        
        self.lbladminMenu = Label(self.Adminframe , text= text, font= ('Manrope', 30 , 'bold') , bg="white smoke", fg="#57a1f8")
        self.lbladminMenu.place(x = Lx_pos, y = Ly_pos)
        
    @staticmethod
    def DataGridProducts(self,grid_x, grid_y):
        datagridframe = Frame(self, width=900, height=390, bg="white")
        datagridframe.place(x = grid_x, y = grid_y)

        self.datagrid = ttk.Treeview(datagridframe, columns=("Column0","Column1", "Column2", "Column3"), show="headings")
        self.datagrid.heading("Column0", text="No.")
        self.datagrid.heading("Column1", text="Product Name" )
        self.datagrid.heading("Column2", text="Product Quantity")
        self.datagrid.heading("Column3", text="Product Price")
        self.datagrid.place(x = 0, y = 50)
        #Functions.DatagridCenter(self.datagrid)
        #Functions.displayProducts(self.datagrid)        
        self.style = ttk.Style()
        self.style.configure("Custom.Treeview", padding=(5, 5), rowheight = 30)  # Adjust padding values as needed
        self.style.configure("Custom.Treeview.Heading", padding=(0, 2))
        self.datagrid.configure(style="Custom.Treeview")
    
    @staticmethod
    def DisplayCart(datagrid, name):
        index = 1
        for i, item in enumerate(CustomerCart_DL.cartlist):
            if name == item.GetCustomerName:
                datagrid.insert("","end", values = (index, item.GetProductName, item.GetProductQuantity, item.GetIndividualPrice))
                index = index + 1
                indexeslist.append((i,item))
    
    @staticmethod
    def displayProducts(datagrid):
        for i,item in enumerate(Products_DL.productsList):
            datagrid.insert("", "end", values=(i+1,item.GetProductName, item.GetProductQuantity, item.GetProductPrice))
    @staticmethod 
    def DatagridCenter(datagrid):
        for col in datagrid["columns"]:
            datagrid.column(col, anchor='center')
    
    @staticmethod       
    def clear_datagrid(grid):
        grid.delete(*grid.get_children())

    @staticmethod
    def UpdateGrid(grid):
        Functions.clear_datagrid(grid)
        Functions.displayProducts(grid)
        
    @staticmethod
    def Updatecart(grid, name):
        Functions.clear_datagrid(grid)
        Functions.DisplayCart(grid, name)
    
class SignInPage(Frame):
    def __init__(self,root):
        super().__init__(root,bg="white")  

        Functions.UpperLabel(self)
        Functions.ShowImageOnLogin(self,"1.png")
        self.username = None
        self.frame = Frame(self, width=350, height=350, bg="white")
        self.frame.place(x = 600, y = 150)

        heading = Label(self.frame, text = "Sign In", bg="White", fg="#57a1f8", font = ('Microsoft YaHei UI Light', 30, 'bold'))
        heading.place(x=100, y = 0)

        self.usernamesignIn = StringVar()
        self.usernamesignIn.set("")
        self.txtusername = Entry(self.frame, textvariable=self.usernamesignIn, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
        self.txtusername.insert(0,"Username")
        self.txtusername.bind("<FocusIn>", lambda event: self.on_entry_click(event, False))
        self.txtusername.bind("<FocusOut>" , lambda event: self.on_Leave(event, False))
        self.txtusername.place(x=45,y=80)

        #Frame(frame, width=290, height=2, bg="black").place(x= 40, y = 107)
        self.AddLineBelow(self.frame, 40, 107)

        ## For Password

        self.userpasswordsignIn = StringVar()
        self.userpasswordsignIn.set("")
        self.txtuserpassword = Entry(self.frame, textvariable=self.userpasswordsignIn, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
        self.txtuserpassword.insert(0,"Password")
        self.txtuserpassword.bind("<FocusIn>", lambda event: self.on_entry_click(event, True))
        self.txtuserpassword.bind("<FocusOut>" , lambda event: self.on_Leave(event, True))
        self.hideimage = ImageTk.PhotoImage(file="hide.ico")
        self.showimage = ImageTk.PhotoImage(file = "show.ico")
        self.hideButton = Button(self.frame, image=self.showimage, border=0, bg="white", command= self.showPassword)
        self.hideButton.place(x=310,y=140)
        self.txtuserpassword.place(x=45,y=150)
        
        self.AddLineBelow(self.frame,40,177)
        #Frame(frame, width=290, height=2, bg="black").place(x= 40, y = 177)

        Button(self.frame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command= self.btnSignIn).place(x = 45, y = 204)

        label = Label(self.frame, text="Dont't have an account?" , fg="black", bg="white", font=('Microsoft YaHei UI Light', 9))
        label.place(x = 70, y = 270)
        signup = Button(self.frame, width=6, text="Sign Up", border=0, bg="white", fg="#57a1f8", cursor="hand2", command= self.go_to_sign_up)
        signup.place(x = 215, y = 270)
        
    def on_entry_click(self,event, check):
        if check == False:
            if self.txtusername.get() == "Username":
                self.txtusername.delete(0, END)
                self.txtusername.config(fg="black")
        elif check == True:
            if self.txtuserpassword.get() == "Password":
                self.txtuserpassword.delete(0, END)
                self.txtuserpassword.config(fg="black", show='*')
                    
    def on_Leave(self,event, check):
        if check == False:
            if self.txtusername.get() == '':
                self.txtusername.insert(0,"Username")
        elif check == True:
            if self.txtuserpassword.get() == '':
                self.txtuserpassword.config(show="")
                self.txtuserpassword.insert(0,"Password")
                
    def showPassword(self):
        showpass = Button(self.frame, image = self.hideimage, command= self.HidePassword, border=0, bg="white")
        showpass.place(x=310,y=140)
        self.txtuserpassword.config(show="")


    def HidePassword(self):
        hidepass = Button(self.frame, image= self.showimage, border=0, command = self.showPassword, bg="white")
        hidepass.place(x=310,y=140)
        self.txtuserpassword.config(show='*')

    def AddLineBelow(self,frame, x_pos, y_pos):
        Frame(frame, width=290, height=2, bg="black").place(x= x_pos, y = y_pos)

    def go_to_sign_up(self):
        app.show_page(app.SignUpPage)
        
    def go_to_AdminPage(self):
        app.show_page(app.AdminPage)
        
    def go_to_UserPage(self, name):
        #app.show_page(app.UserPage)
        userpage = UserPage(self,name)
        listofpages.append(userpage)
        app.show_page(userpage)
        
    
        
    def SetSignInValuesDefault(self):
        self.txtusername.delete(0,END)
        self.txtuserpassword.delete(0,END)
        self.txtusername.insert(0,"Username")
        self.txtuserpassword.config(show="")
        self.txtuserpassword.insert(0,"Password")
    
    def btnSignIn(self):
        global name
        username = self.txtusername.get()
        password = self.txtuserpassword.get()
        if (username != None and username != "Username") and (password != None and password != "Password"):
            signinuser = SignIn_BL(username, password)
            self.getrole = MUser_DL.GetRole(signinuser)
            if self.getrole == "Admin" or self.getrole == "admin":
                self.SetSignInValuesDefault()
                self.go_to_AdminPage()
            elif self.getrole == "User" or self.getrole == "user":
                self.username = username
                name = username
                self.SetSignInValuesDefault()
                self.go_to_UserPage(username)
                
                
            else:
                msg.showerror("Error", "User Not Found")
        else:
            msg.showerror("Error", "Invalid Credentials")
        
class SignUpPage(Frame):
    def __init__(self,root):
        super().__init__(root,bg="white")
        

        Functions.UpperLabel(self)
        Functions.ShowImageOnLogin(self,"1.png")
        
        self.frame1 = Frame(self, width=350, height=400, bg="white")
        self.frame1.place(x = 600, y = 150)

        heading = Label(self.frame1, text = "Sign Up", bg="White", fg="#57a1f8", font = ('Microsoft YaHei UI Light', 30, 'bold'))
        heading.place(x=100, y = 0)

        self.username_signup = StringVar()
        self.username_signup.set("")
        self.txtusername_signup = Entry(self.frame1, textvariable=self.username_signup, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
        self.txtusername_signup.insert(0,"Username")
        self.txtusername_signup.bind("<FocusIn>", lambda event: self.on_entry_click(event, False))
        self.txtusername_signup.bind("<FocusOut>" , lambda event: self.on_Leave(event, False))
        self.txtusername_signup.place(x=45,y=80)
        self.AddLineBelow(self.frame1, 40 , 107)

        ## For Password

        self.userpassword_signup = StringVar()
        self.userpassword_signup.set("")
        self.txtuserpassword_signup = Entry(self.frame1, textvariable=self.userpassword_signup, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
        self.txtuserpassword_signup.insert(0,"Password")
        self.txtuserpassword_signup.bind("<FocusIn>", lambda event: self.on_entry_click(event, True))
        self.txtuserpassword_signup.bind("<FocusOut>" , lambda event: self.on_Leave(event, True))
        self.hideimage = ImageTk.PhotoImage(file="hide.ico")
        self.showimage = ImageTk.PhotoImage(file = "show.ico")
        self.hideButton1 = Button(self.frame1, image=self.showimage, border=0, bg="white", command=self.showPassword_SignUp)
        self.hideButton1.place(x=310,y=140)
        self.txtuserpassword_signup.place(x=45,y=150)        
        self.AddLineBelow(self.frame1, 40, 177)
        
        ## For Role

        self.userrole_signUp = StringVar()
        self.userrole_signUp.set("")
        self.txtuserrole_signup = ttk.Combobox(self.frame1, values=["Admin", "User"], width=33, height=10, font= ('Microsoft YaHei UI Light', 11))
        self.txtuserrole_signup.insert(0,"Role")
        self.txtuserrole_signup.place(x = 45, y = 215)        
        self.AddLineBelow(self.frame1, 40, 247)
        Button(self.frame1, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command= self.btnSignUp).place(x = 45, y = 280)
        GotoSignIn = Button(self.frame1, width=20, pady=7, text="Go to Sign In", bg="#57a1f8", fg="white", border=0, command= self.go_to_sign_In)
        GotoSignIn.place(x=45, y = 350)

    def AddLineBelow(self,frame, x_pos, y_pos):
        Frame(frame, width=290, height=2, bg="black").place(x= x_pos, y = y_pos)
        
    def on_entry_click(self,event, check):
        if check == False:
            if self.txtusername_signup.get() == "Username":
                self.txtusername_signup.delete(0,END)
                self.txtusername_signup.config(fg="black")
        elif check == True:
            if self.txtuserpassword_signup.get() == "Password":
                self.txtuserpassword_signup.delete(0,END)
                self.txtuserpassword_signup.config(fg="black", show='*')
        elif check == None:
            if self.txtuserrole_signup.get() == "Role":
                self.txtuserrole_signup.delete(0,END)
                self.txtuserrole_signup.config(fg="black")
            
    def on_Leave(self,event, check):
        if check == False:
            if self.txtusername_signup.get() == '':
                self.txtusername_signup.insert(0,"Username")
        elif check == True:
                if self.txtuserpassword_signup.get() == '':
                    self.txtuserpassword_signup.config(show="")
                    self.txtuserpassword_signup.insert(0,"Password")
        elif check == None:
                if self.txtuserrole_signup.get() == '':
                    self.txtuserrole_signup.insert(0,"Role")
                    
    def showPassword_SignUp(self):
        showpass = Button(self.frame1, image=self.hideimage, command= self.HidePassword_SignUp, border=0, bg="white")
        showpass.place(x=310,y=140)
        self.txtuserpassword_signup.config(show="")

    def HidePassword_SignUp(self):
        hidepass = Button(self.frame1, image=self.showimage, border=0, command= self.showPassword_SignUp, bg="white")
        hidepass.place(x=310,y=140)
        self.txtuserpassword_signup.config(show='*')
        
    def go_to_sign_In(self):
        app.show_page(app.SignInPage)
        
    def btnSignUp(self):
        try:
            username = self.txtusername_signup.get()
            password = self.txtuserpassword_signup.get()
            role = self.txtuserrole_signup.get()
            if username != "Username" and username != '':
                if password != "Password" and password != '':
                    if role != "Role" and role != '' and ((role !="Admin" or role !="admin") or(role != "User" or role != "user")):
                        user = SignUp_BL(username,password, role)
                        MUser_DL.AddInList(user)
                        MUser_DL.StoreUserInFile("Users.txt")
                        print(self.txtusername_signup.get(), self.txtuserpassword_signup.get(), self.txtuserrole_signup.get())
                        msg.showinfo("Sign Up", "Signed Up Successfully")
                        self.SetSignUpValuesDefault()
                    else:
                        msg.showerror("Role Error", "Please Enter Valid Role")
                else:
                    msg.showerror("Password Error", "Please Enter Valid Password")
            else:
                msg.showerror("Username Error", "Please Enter Valid Username")
        except Exception as e:
            print("An Error Occured", e)
            
    def SetSignUpValuesDefault(self):
        self.txtusername_signup.delete(0,END)
        self.txtuserpassword_signup.delete(0,END)
        self.txtuserrole_signup.delete(0,END)
        self.txtusername_signup.insert(0,"Username")
        self.txtuserpassword_signup.config(show="")
        self.txtuserpassword_signup.insert(0,"Password")
        self.txtuserrole_signup.insert(0,"Role")
        
class AdminPage(Frame):
    def __init__(self,root):
        super().__init__(root,bg="white")
        
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"managerLogo.png",0,70,"Admin Menu", 65,400)
        
        self.ProductsFrame = Frame(self , width=700, height=500, bg= "white smoke")
        self.ProductsFrame.place(x=450, y = 120)

        self.viewproductImage = self.GiveImage("ViewProducts.png")
        btnViewProducts = Button(self.ProductsFrame , image=self.viewproductImage, borderwidth=6, bg="#57a1f8", command=self.go_to_ViewProductPage) ## View Products
        btnViewProducts.place(x= 50, y= 50)    
        self.OptionName(self.ProductsFrame, "View Products", 55, 170)
        
        self.AddProductImage = self.GiveImage("AddProduct.png")
        btnAddProducts = Button(self.ProductsFrame , image=self.AddProductImage, borderwidth=6, bg="#57a1f8", command= self.go_to_AddProductPage) ## Add Products
        btnAddProducts.place(x= 250, y= 50) 
        self.OptionName(self.ProductsFrame, "Add Product", 260,170)
        
        self.DeleteProductImage = self.GiveImage("DeleteProduct.png")
        btnDeleteProduct = Button(self.ProductsFrame, image=self.DeleteProductImage, borderwidth=6 , bg="#57a1f8", command= self.go_to_DeleteProductPage) ## Delete Products
        btnDeleteProduct.place(x = 450, y = 50)
        self.OptionName(self.ProductsFrame, "Delete Product", 460,170)
        
        self.UpdateProductImage = self.GiveImage("update_product.png")
        btnUpdateProduct = Button(self.ProductsFrame, image=self.UpdateProductImage, borderwidth=6 , bg="#57a1f8", command= self.go_to_UpdateProductPage) ## Update Products
        btnUpdateProduct.place(x = 50, y = 250)
        self.OptionName(self.ProductsFrame, "Update Product", 55, 370)

    def GiveImage(self, imgname):
        viewProductsImage = Image.open(imgname)
        imgResize = viewProductsImage.resize((100,100) , Image.LANCZOS)
        photoproduct = ImageTk.PhotoImage(imgResize)   
        return photoproduct
    
    def OptionName(self, framename, text, x_pos, y_pos):
        Label(framename, text = text, font= ('Manrope', 10 , 'bold'), bg="white smoke").place(x=x_pos, y = y_pos)

    def go_to_ViewProductPage(self):
        app.show_page(app.ViewProductsPage)
        
    def go_to_AddProductPage(self):
        app.show_page(app.AddProductsPage)
        
    def go_to_DeleteProductPage(self):
        app.show_page(app.DeleteProductsPage)
        
    def go_to_UpdateProductPage(self):
        app.show_page(app.UpdateProductsPage)
        
class ViewProductsPage(Frame):
    def __init__(self,root):
        super().__init__(root,bg="white")
        
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"managerLogo.png",0,70,"Products Info", 55,400)
        
        Functions.DataGridProducts(self,400,150)   
        Functions.displayProducts(self.datagrid)
        Functions.DatagridCenter(self.datagrid) 
            

        self.BelowDatagridFrame = Frame(self, width = 900, height=50, bg="white")
        self.BelowDatagridFrame.place(x=400, y= 550)
        Gotoadmenu = Button(self.BelowDatagridFrame, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= self.go_to_AdminPage)
        Gotoadmenu.place(x=0, y = 5)
    
    # def showname(self):
    #     name = self.Signinpage.username
    #     msg.showinfo("name", str(name))
    
    def go_to_AdminPage(self):
        app.show_page(app.AdminPage)
        
class AddProductsPage(Frame):
    def __init__(self,root, viewproductpage):
        super().__init__(root,bg="white")
        self.Viewproductpage = viewproductpage
        
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"managerLogo.png",0,70,"Add Products", 55,400)
        
        self.view = ViewProductsPage(root)
        self.Addproductframe = Frame(self, bg="white", width=600, height=400)
        self.Addproductframe.place(x = 500, y = 150)

        self.ProductName = StringVar()
        self.ProductPrice = StringVar()
        self.ProductQuantity = StringVar()
        self.ProductName.set("")
        self.ProductPrice.set("")
        self.ProductQuantity.set("")

        self.txtproductname = Entry(self.Addproductframe, textvariable=self.ProductName, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
        self.txtproductname.insert(0,"Product Name")
        self.txtproductname.bind("<FocusIn>", lambda event: self.On_Click(event,"name"))
        self.txtproductname.bind("<FocusOut>", lambda event: self.OnLeave(event,"name"))
        self.txtproductname.place(x = 50, y = 50)
        self.AddLineBelow(self.Addproductframe, 50,80)
        
        self.txtproductprice = Entry(self.Addproductframe, textvariable=self.ProductPrice, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
        self.txtproductprice.insert(0,"Product Price")
        self.txtproductprice.bind("<FocusIn>", lambda event: self.On_Click(event,"price"))
        self.txtproductprice.bind("<FocusOut>", lambda event: self.OnLeave(event,"price"))
        self.txtproductprice.place(x = 50, y = 120)
        self.AddLineBelow(self.Addproductframe, 50, 150)
        
        self.txtproductquantity = Entry(self.Addproductframe, textvariable=self.ProductQuantity, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
        self.txtproductquantity.insert(0,"Product Quantity")
        self.txtproductquantity.bind("<FocusIn>", lambda event: self.On_Click(event,"quantity"))
        self.txtproductquantity.bind("<FocusOut>", lambda event: self.OnLeave(event,"quantity"))
        self.txtproductquantity.place(x = 50, y = 190)
        self.AddLineBelow(self.Addproductframe, 50, 220)
        
        Button(self.Addproductframe, width=39, pady=7, text="Add Product", bg="#57a1f8", fg="white", border=0, command= self.addproduct).place(x = 50, y = 280)
        Functions.UpdateGrid(self.view.datagrid)
        GotoAdminMenu = Button(self.Addproductframe, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= self.go_to_AdminPage)
        GotoAdminMenu.place(x=50, y = 350)
        
        
    def AddLineBelow(self, framename, x_pos, y_pos):
        Frame(framename, width=280, height=2, bg="black").place(x= x_pos, y = y_pos)

    def go_to_AdminPage(self):
        app.show_page(app.AdminPage)

    def On_Click(self,event, item):
        if item == "name":
            if self.txtproductname.get() == "Product Name":
                self.txtproductname.delete(0,END)
                self.txtproductname.config(fg="black")
        elif item == "price":
            if self.txtproductprice.get() == "Product Price":
                self.txtproductprice.delete(0,END)
                self.txtproductprice.config(fg="black")
        elif item == "quantity":
            if self.txtproductquantity.get() == "Product Quantity":
                self.txtproductquantity.delete(0, END)
                self.txtproductquantity.config(fg="black")

    def OnLeave(self,event, item):
        if item == "name":
            if self.txtproductname.get() == '':
                self.txtproductname.insert(0,"Product Name")
        elif item == "price":
            if self.txtproductprice.get() == '':
                self.txtproductprice.insert(0, "Product Price")
        elif item == "quantity":
            if self.txtproductquantity.get() == '':
                self.txtproductquantity.insert(0, "Product Quantity")
                
    def addproduct(self):
        try:
            if self.txtproductname.get() != None and self.txtproductname.get() != "Product Name":
                if self.txtproductprice.get() != NONE and self.txtproductprice.get() != "Product Price":
                    if self.txtproductquantity.get() != None and self.txtproductquantity.get() != "Product Quantity":
                        product = Manager_BL(self.txtproductname.get(), self.txtproductquantity.get(), self.txtproductprice.get())
                        Products_DL.AddInProductList(product)
                        Products_DL.StoreProductsInfile("Products.txt")
                        Functions.UpdateGrid(self.Viewproductpage.datagrid)
                        #UpdateGrid(datagrid)
                        #UpdateGrid(datagrid_deleteproduct)
                        msg.showinfo("Product Added","Product has been added successfully")
                        self.SetProductsDefaultValues()
                    else:            
                        msg.showerror("Error","Invalid Quantity")
                else:
                    msg.showerror("Error","Invalid Price")
            else:
                msg.showerror("Error","Invalid Name")
        except Exception as e:
            msg.showerror("An Error Occured", e)
        
    def SetProductsDefaultValues(self):
        self.txtproductname.delete(0,END)
        self.txtproductprice.delete(0,END)
        self.txtproductquantity.delete(0,END)
        self.txtproductname.insert(0,"Product Name")
        self.txtproductprice.insert(0,"Product Price")
        self.txtproductquantity.insert(0, "Product Quantity")
        
        
class DeleteProductsPage(Frame):
    def __init__(self,root, viewproductpage, updateproductpage):
        super().__init__(root,bg="white")
        self.Viewproductpage = viewproductpage
        self.Updateproductpage = updateproductpage
        
        self.index = StringVar()
        self.index.set("x")
        
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"managerLogo.png",0,70,"Delete Products", 30,400)
        
        Functions.DataGridProducts(self,400,150)   
        Functions.displayProducts(self.datagrid)
        Functions.DatagridCenter(self.datagrid) 
        
        self.BelowDatagridFrame = Frame(self, width = 900, height=50, bg="white")
        self.BelowDatagridFrame.place(x=400, y= 550)
        Gotoadmenu = Button(self.BelowDatagridFrame, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= self.go_to_AdminPage)
        Gotoadmenu.place(x=0, y = 5)
        deleteitem = Button(self.BelowDatagridFrame, width=20, pady=7, text="Delete", bg="red", fg="white", border=0, command=self.DeleteProduct)
        deleteitem.place(x = 250, y = 5)
        
        self.datagrid.bind("<<TreeviewSelect>>", lambda event, grid= self.datagrid: self.on_item_select(event, grid))
    
    @staticmethod
    def UpdateGridinDeleteProductClass(self):
        Functions.UpdateGrid(self.datagrid)
    
    def on_item_select(self,event, grid):
        selected_items = grid.selection()
        if selected_items:
            selected_item = selected_items[0]  # Get the selected item's ID
            i = str(grid.index(selected_item))
            self.index.set(str(i)) 
            print(self.index.get())
            
    def DeleteProduct(self):  ## index ko -1 ya x krna hy ===================    
        selectedItem = (self.index.get())
        if selectedItem != "x":
                selectedItem = int(selectedItem)
                val = msg.askyesno("Question","Do you want to delete that Product? ")
                if val:
                    Products_DL.DeleteProducts(selectedItem)
                    Functions.UpdateGrid(self.Viewproductpage.datagrid)
                    Functions.UpdateGrid(self.datagrid)
                    Functions.UpdateGrid(self.Updateproductpage.datagrid)
                    Products_DL.StoreProductsInfile("Products.txt")
                    msg.showinfo("Deleted","Your Item has been deleted")
                else:
                    msg.showinfo("Cancelled","Your operation has been cancelled")
                
        else:
            msg.showerror("Error","Item not selected")
        
    def go_to_AdminPage(self):
        app.show_page(app.AdminPage)
        
class UpdateProductsPage(Frame):
    def __init__(self,root, viewproductpage):
        super().__init__(root,bg="white")
        self.Viewproductpage = viewproductpage
        
        self.Deleteproductpage = None
        
        
        
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"managerLogo.png",0,70,"Update Products", 20,400)
        
        Functions.DataGridProducts(self,400,150)   
        Functions.displayProducts(self.datagrid)
        Functions.DatagridCenter(self.datagrid) 
        self.datagrid.bind("<<TreeviewSelect>>", lambda event, grid= self.datagrid: self.on_item_select(event, grid))
        self.index = StringVar()
        self.index.set("x")
        
        
        
        self.BelowDatagridFrame = Frame(self, width = 900, height=50, bg="white")
        self.BelowDatagridFrame.place(x=400, y= 550)
        Gotoadmenu = Button(self.BelowDatagridFrame, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= self.go_to_AdminPage)
        Gotoadmenu.place(x=0, y = 5)
        btnUpdatePrice = Button(self.BelowDatagridFrame, width=20, pady=7, text="Update Price", bg="#57a1f8", fg="white", border=0, command=self.OpenUpdatePriceMenu)
        btnUpdatePrice.place(x = 250, y = 5)
        btnUpdateQuantity = Button(self.BelowDatagridFrame, width=20, pady=7, text="Update Quantity", bg="#57a1f8", fg="white", border=0, command= self.OpenUpdateQuantityMenu)
        btnUpdateQuantity.place(x = 450, y = 5)
        
    def set_delete_page(self, delete_page):
        self.Deleteproductpage = delete_page
        
    def go_to_AdminPage(self):
        app.show_page(app.AdminPage)
        
    def OpenUpdatePriceMenu(self):
        print(self.index.get())
        selectedItem = self.index.get()
        if selectedItem != "x":
            self.newform = Toplevel(self)
            self.newform.configure(bg="white")
            root_x = self.winfo_x()
            root_y = self.winfo_y()
            root_width = self.winfo_width()
            root_height = self.winfo_height()

            new_width = 400  # Set the width of the new form
            new_height = 300  # Set the height of the new form

            new_x = root_x + (root_width - new_width) // 2
            new_y = root_y + (root_height - new_height) // 2

            self.newform.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")
            self.newform.title("Update Price")
            self.newform.resizable(False,False)
            
            name = self.GetProductName()
            NewQuantity = StringVar()
            
            self.productname = StringVar()
            self.productname.set("x")
            self.productname.set(str(name))
            Label(self.newform, textvariable = self.productname, width=25, fg="Black", bg="white",border= 0, font = ('Microsoft YaHei UI Light', 11), anchor="w").place(x = 50, y = 50)
            self.AddLineBelow(self.newform , 50, 80)
            self.txtNewPrice = Entry(self.newform, textvariable=NewQuantity,width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
            self.txtNewPrice.insert(0,"New Price")
            self.txtNewPrice.bind("<FocusIn>" ,lambda event: self.On_Click(event,"price"))
            self.txtNewPrice.bind("<FocusOut>",lambda event: self.OnLeave(event,"price"))
            self.txtNewPrice.place(x = 50, y = 120)
            self.AddLineBelow(self.newform, 50, 150)
            
            Button(self.newform, text="Update", width=15, pady=7,bg="#57a1f8", fg="white", border=0, command=self.UpdatePrice).place(x = 220,  y= 200)
            Button(self.newform, text="Cancel", width=15, pady=7,bg="red", fg="white", border=0, command = self.newform.destroy).place(x = 50,  y= 200)
        else:
            msg.showerror("Error","Please select any item")
           
    
    def OpenUpdateQuantityMenu(self):
        print(self.index.get())
        selectedItem = self.index.get()
        if selectedItem != "x":
            self.newform = Toplevel(self)
            root_x = self.winfo_x()
            root_y = self.winfo_y()
            root_width = self.winfo_width()
            root_height = self.winfo_height()

            new_width = 400  # Set the width of the new form
            new_height = 300  # Set the height of the new form

            new_x = root_x + (root_width - new_width) // 2
            new_y = root_y + (root_height - new_height) // 2

            self.newform.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")
            self.newform.title("Update Quantity")
            self.newform.configure(bg="white")
            self.newform.resizable(False,False)
            
            name = self.GetProductName()
            NewQuantity = StringVar()
            
            self.productname = StringVar()
            self.productname.set("x")
            self.productname.set(str(name))
            Label(self.newform, textvariable = self.productname, width=25, fg="Black", bg="white",border= 0, font = ('Microsoft YaHei UI Light', 11), anchor="w").place(x = 50, y = 50)
            self.AddLineBelow(self.newform , 50, 80)
            self.txtNewQuantity = Entry(self.newform, textvariable=NewQuantity,width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
            self.txtNewQuantity.insert(0,"New Quantity")
            self.txtNewQuantity.bind("<FocusIn>" ,lambda event: self.On_Click(event,"quantity"))
            self.txtNewQuantity.bind("<FocusOut>",lambda event: self.OnLeave(event, "quantity"))
            self.txtNewQuantity.place(x = 50, y = 120)
            self.AddLineBelow(self.newform, 50, 150)
            
            Button(self.newform, text="Update", width=15, pady=7,bg="#57a1f8", fg="white", border=0, command=self.Update).place(x = 220,  y= 200)
            Button(self.newform, text="Cancel", width=15, pady=7,bg="red", fg="white", border=0, command= self.newform.destroy).place(x = 50,  y= 200)
        else:
            msg.showerror("Error","Please select any item")
        
    def on_item_select(self,event, grid):
        selected_items = grid.selection()
        if selected_items:
            selected_item = selected_items[0]  # Get the selected item's ID
            i = str(grid.index(selected_item))
            self.index.set(str(i)) 
            print(self.index.get())   
    
    def GetProductName(self):
        selectedItem = int(self.index.get())
        name = Products_DL.GetProductName(selectedItem)
        return name
        
    
    
    
    def Update(self):
        try:
            selectedItem = int(self.index.get())
            newquantity = self.txtNewQuantity.get()
            if newquantity != '' and newquantity != "New Quantity":
                newquantity = float(newquantity)
                if newquantity > 0:
                    Products_DL.ChangeQuantity(selectedItem,int(newquantity))
                    Products_DL.StoreProductsInfile("Products.txt")
                    Functions.UpdateGrid(self.Viewproductpage.datagrid)
                    Functions.UpdateGrid(self.datagrid)
                    Functions.UpdateGrid(self.Deleteproductpage.datagrid)
                    self.index.set("x")
                    self.newform.destroy()
                    msg.showinfo("Updated"," Quantity has been Updated")
                else:
                    msg.showerror("Error","Please Enter Valid Quantity")
            else:
                msg.showerror("Error","Please Enter Valid Quantity")
        except Exception as e:
            msg.showwarning("An error occured at update function" , e)
            
    def UpdatePrice(self):
        try:
            selectedItem = int(self.index.get())
            newprice = self.txtNewPrice.get()
            if newprice != '' and newprice != "New Price":
                newprice = float(newprice)
                if newprice > 0:
                    Products_DL.ChangePrice(selectedItem,int(newprice))
                    Products_DL.StoreProductsInfile("Products.txt")
                    Functions.UpdateGrid(self.Viewproductpage.datagrid)
                    Functions.UpdateGrid(self.datagrid)
                    Functions.UpdateGrid(self.Deleteproductpage.datagrid)
                    self.index.set("x")
                    self.newform.destroy()
                    msg.showinfo("Updated"," Price has been Updated")
                else:
                    msg.showerror("Error","Please Enter Valid Price")
            else:
                msg.showerror("Error","Please Enter Valid Price")
        except Exception as e:
            msg.showwarning("An error occured at update function" , e)
    
             
        
    def AddLineBelow(self, framename, x_pos, y_pos):
        Frame(framename, width=280, height=2, bg="black").place(x= x_pos, y = y_pos)
        
    def On_Click(self,event,item):
        if item == "quantity":
            if self.txtNewQuantity.get() == "New Quantity":
                self.txtNewQuantity.delete(0,END)
                self.txtNewQuantity.config(fg="black")
        elif item == "price":
            if self.txtNewPrice.get() == "New Price":
                self.txtNewPrice.delete(0,END)
                self.txtNewPrice.config(fg="black")
    def OnLeave(self, event, item):
        if item == "quantity":
            if self.txtNewQuantity.get() == '':
                self.txtNewQuantity.insert(0,"New Quantity")
        elif item == "price":
            if self.txtNewPrice.get() == '':
                self.txtNewPrice.insert(0,"New Price")
    
    def update_page(self, update_page):
        self.UpdateProductsPage = update_page
        
        
class UserPage(Frame):
    def __init__(self,signinpage,name):
        super().__init__(bg="white")
        self.Signinpage = signinpage
        Functions.UpperLabel(self)
        self.name = name
        Functions.AdminSideFrame(self,"UserLogo.png",0,70,"User Menu",65, 400)
        self.uperframe = Frame(self,width=700, height=30, bg="white")
        self.uperframe.place(x = 400, y=80)
        Label(self.uperframe, text=f"Welcome, {self.name}", fg="#57a1f8", bg="white", font=("",15,"")).place(x=5,y=5)
        self.ProductsFrame = Frame(self , width=700, height=500, bg= "white smoke")
        self.ProductsFrame.place(x=450, y = 120)
        
        self.viewproductImage = self.GiveImage("ViewProducts.png")
        btnViewProducts = Button(self.ProductsFrame , image=self.viewproductImage, borderwidth=6, bg="#57a1f8", command=self.go_to_ViewProductPageUser) ## View Products
        btnViewProducts.place(x= 50, y= 50)    
        self.OptionName(self.ProductsFrame, "View Products", 55, 170)
        
        self.ViewCartImage = self.GiveImage("ViewCart.png")
        btnViewCart = Button(self.ProductsFrame , image=self.ViewCartImage, borderwidth=6, bg="#57a1f8", command=self.go_to_ViewCartPage) ## View Cart
        btnViewCart.place(x= 250, y= 50) 
        self.OptionName(self.ProductsFrame, "View Cart", 270,170)
        
        self.UpdateCartImage = self.GiveImage("ChangeCart.png")
        btnUpdateCart = Button(self.ProductsFrame, image=self.UpdateCartImage, borderwidth=6 , bg="#57a1f8", command=self.go_to_UpdateCartPage) ## Update Cart
        btnUpdateCart.place(x = 450, y = 50)
        self.OptionName(self.ProductsFrame, "Update Cart", 460,170)
        
    def go_to_ViewProductPageUser(self):
        app.show_page(app.ViewProductsPageUser)
    
    def sendname(self):
        app.ViewCartUser
        
    def go_to_ViewCartPage(self):
        #name0 = self.Signinpage.username
        view_cart_user = ViewCartUser(self.name)
        listofpages.append(view_cart_user)
        #ViewCartUser.setname(self, name)
        app.show_page(view_cart_user)
        
    def go_to_UpdateCartPage(self):
        #name1 = self.Signinpage.username
        Update_cart_user = ChangeCart(self.name)
        listofpages.append(Update_cart_user)
        #ViewCartUser.setname(self, name)
        app.show_page(Update_cart_user)
        
        
    def OptionName(self, framename, text, x_pos, y_pos):
        Label(framename, text = text, font= ('Manrope', 10 , 'bold'), bg="white smoke").place(x=x_pos, y = y_pos)
        
    def GiveImage(self, imgname):
        viewProductsImage = Image.open(imgname)
        imgResize = viewProductsImage.resize((100,100) , Image.LANCZOS)
        photoproduct = ImageTk.PhotoImage(imgResize)   
        return photoproduct
    
class ViewProductPageUser(Frame):
    def __init__(self,root, signinpage):
        super().__init__(root,bg="white")
        self.Signinpage = signinpage
        #self.username = None
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"UserLogo.png",0,70,"View Products", 65, 400)
        
        Functions.DataGridProducts(self,400,150)   
        Functions.displayProducts(self.datagrid)
        #Functions.DisplayCart(self.datagrid, self.Signinpage.username)
        Functions.DatagridCenter(self.datagrid) 
        self.datagrid.bind("<<TreeviewSelect>>", lambda event, grid= self.datagrid: self.on_item_select(event, grid))
        
        self.index = StringVar()
        self.index.set("x")

        self.BelowDatagridFrame = Frame(self, width = 900, height=50, bg="white")
        self.BelowDatagridFrame.place(x=400, y= 550)
        Gotoadmenu = Button(self.BelowDatagridFrame, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= self.go_to_UserPage)
        Gotoadmenu.place(x=0, y = 5)
        AddtoCartButton = Button(self.BelowDatagridFrame, width=20, pady=7, text="Add to Cart", bg="SpringGreen2", fg="white", border=0, font=("",9,"bold"), command=self.EnterQuantityMenu)
        AddtoCartButton.place(x = 660, y = 5)
    
    # def GetSignin_page(self, update_page):
    #     self.Signinpage = update_page
        
    def EnterQuantityMenu(self):
        selectedItem = (self.index.get())
        if selectedItem != "x":
            self.newform = Toplevel(self)
            root_x = self.winfo_x()
            root_y = self.winfo_y()
            root_width = self.winfo_width()
            root_height = self.winfo_height()

            new_width = 400  # Set the width of the new form
            new_height = 300  # Set the height of the new form

            new_x = root_x + (root_width - new_width) // 2
            new_y = root_y + (root_height - new_height) // 2

            self.newform.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")
            self.newform.title("Enter Quantity")
            self.newform.configure(bg="white")
            self.newform.resizable(False,False)
            name = self.GetProductName()
            self.productname = StringVar()
            self.productname.set("x")
            self.productname.set(str(name))
            Label(self.newform, text = f"Product Name: {self.productname.get()}", width=25, fg="Black", bg="white",border= 0, font = ('Microsoft YaHei UI Light', 11), anchor="w").place(x = 50, y = 50)
            self.AddLineBelow(self.newform , 50, 80)
            self.NewQuantity = StringVar()
            self.txtquantity = Entry(self.newform, textvariable=self.NewQuantity,width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
            self.txtquantity.insert(0,"Enter Quantity")
            self.txtquantity.bind("<FocusIn>" ,lambda event: self.On_Click(event))
            self.txtquantity.bind("<FocusOut>",lambda event: self.OnLeave(event))
            self.txtquantity.place(x = 50, y = 120)
            self.AddLineBelow(self.newform, 50, 150)
            
            Button(self.newform, text="Add", width=15, pady=7,bg="#57a1f8", fg="white", border=0, command= self.Addtocart).place(x = 220,  y= 200)
            Button(self.newform, text="Cancel", width=15, pady=7,bg="red", fg="white", border=0, command= self.newform.destroy).place(x = 50,  y= 200)
        else:
            msg.showerror("Error","Please select any item")
    
    def Addtocart(self):
        print(self.Signinpage.username)
        try:
            cusotmername = self.Signinpage.username
            productname = self.productname.get()
            productquantity = str(self.txtquantity.get())
            if productquantity != '' and productquantity != "Enter Quantity":
                getprice = Products_DL.GetProductPrice(str(productname))
                individualprice = int(getprice) * int(productquantity)
                customerproduct = Customer_BL(str(cusotmername), str(productname), (productquantity), (individualprice))
                CustomerCart_DL.AddtoCart(customerproduct)
                CustomerCart_DL.StoreCustomerCart("cart.txt")
                self.index.set("x")
                self.newform.destroy()
                msg.showinfo("Product Added", f"{str(productquantity)} {str(productname)} has been added to your cart")
            else:
                msg.showerror("Invalid Quantity", "Please Enter Valid Quantity")
        except Exception as e:
            msg.showwarning("An error occured in Add to cart Option", e)
            
    def On_Click(self,event):
        if self.txtquantity.get() == "Enter Quantity":
            self.txtquantity.delete(0,END)
            self.txtquantity.config(fg="gray1") 
            
    def OnLeave(self,event):
        if self.txtquantity.get() == '':
            self.txtquantity.insert(0,"Enter Quantity")
            
    def AddLineBelow(self, framename, x_pos, y_pos):
        Frame(framename, width=280, height=2, bg="black").place(x= x_pos, y = y_pos)
        
    def GetProductName(self):
        selectedItem = int(self.index.get())
        name = Products_DL.GetProductName(selectedItem)
        return name
    
    def on_item_select(self,event, grid):
        selected_items = grid.selection()
        if selected_items:
            selected_item = selected_items[0]  # Get the selected item's ID
            i = str(grid.index(selected_item))
            self.index.set(str(i)) 
            print(self.index.get())
    
    def go_to_UserPage(self):
        #app.show_page(app.UserPage)
        userpage3 = UserPage(self.Signinpage,self.Signinpage.username)
        listofpages.append(userpage3)
        app.show_page(userpage3)
        
        
class ViewCartUser(Frame):
    def __init__(self, name):
        super().__init__(bg="white")
        #self.Signinpage = signinpage
        self.username = name
        
        
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"UserLogo.png",0,70,"Your Cart", 65,400)
        Functions.DataGridProducts(self,400,150) 
        
        self.go_to_PrintCart()
        Functions.DatagridCenter(self.datagrid) 
        
        self.BelowDatagridFrame = Frame(self, width = 900, height=50, bg="white")
        self.BelowDatagridFrame.place(x=400, y= 550)
        Gotoadmenu = Button(self.BelowDatagridFrame, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= self.go_to_UserPage)
        Gotoadmenu.place(x=0, y = 5)
    
       
    def go_to_UserPage(self):
       # app.show_page(app.UserPage)
        userpage2 = UserPage(None,self.username)
        listofpages.append(userpage2)
        app.show_page(userpage2)
    
    @staticmethod
    def set_name(self, name):
        self.username = name
        print(self.username)
    
    def go_to_PrintCart(self):        
        Functions.DisplayCart(self.datagrid, self.username)  # Use the updated username
        
        
class ChangeCart(Frame):
    def __init__(self, name):
        super().__init__(bg="white")    
        self.username = name
        
        self.cartindex = StringVar()
        self.cartindex.set("x")
        
        Functions.UpperLabel(self)
        Functions.AdminSideFrame(self,"UserLogo.png",0,70,"Your Cart", 65,400)
        Functions.DataGridProducts(self,400,150) 
        self.go_to_PrintCart() 
        Functions.DatagridCenter(self.datagrid)   
        self.datagrid.bind("<<TreeviewSelect>>", lambda event, grid= self.datagrid: self.on_item_select(event, grid))
        
        self.BelowDatagridFrame = Frame(self, width = 900, height=50, bg="white")
        self.BelowDatagridFrame.place(x=400, y= 550)
        Gotoadmenu = Button(self.BelowDatagridFrame, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= self.go_to_UserPage)
        Gotoadmenu.place(x=0, y = 5) 
        Clearcart = Button(self.BelowDatagridFrame, width=20, pady=7, text="Clear Cart", bg="red", fg="white", border=0, command= self.btnClearcart)
        Clearcart.place(x = 650, y =5)
        btndeleteproduct = Button(self.BelowDatagridFrame, width=20, pady=7, text="Delete Product", bg="red", fg="white", border=0, command=self.btndeleteproduct)
        btndeleteproduct.place(x = 200, y = 5)
    
    def btndeleteproduct(self):
        selectedItem = (self.cartindex.get())
        if selectedItem != "x":
            selectedItem = int(selectedItem)
            val = msg.askyesno("Question","Are you sure to delete this product?")
            if val:
                original_index, item = indexeslist[selectedItem]
                name = CustomerCart_DL.GetProductName(original_index)
                check = CustomerCart_DL.deleteproductfromcart(name, self.username)
                CustomerCart_DL.StoreCustomerCart("cart.txt")
                Functions.Updatecart(self.datagrid, self.username)
                msg.showinfo("Product Deleted","Your product has been deleted")
        else:
            msg.showerror("Error","Please select any item")        
    
    def go_to_PrintCart(self):        
        Functions.DisplayCart(self.datagrid, self.username)  # Use the updated username
    
    def go_to_UserPage(self):
       # app.show_page(app.UserPage)
        userpage3 = UserPage(None,self.username)
        listofpages.append(userpage3)
        app.show_page(userpage3)
        
    def btnClearcart(self):
        value = msg.askyesno("Clear cart","Are you sure to clear your cart?")
        if value:
            #print(self.username)
            indexes = CustomerCart_DL.GetUserIndexes(self.username)
            CustomerCart_DL.ClearCart(indexes)
            CustomerCart_DL.StoreCustomerCart("cart.txt")
            Functions.Updatecart(self.datagrid, self.username)
            msg.showinfo("Cart Cleared","Your cart has been cleard")
     
    
    def on_item_select(self,event, grid):
        selected_items = grid.selection()
        if selected_items:
            selected_item = selected_items[0]  # Get the selected item's ID
            i = str(grid.index(selected_item))
            self.cartindex.set(str(i)) 
            print(self.cartindex.get())   

if __name__ == "__main__":
    app = GUIApp()
    app.run()
