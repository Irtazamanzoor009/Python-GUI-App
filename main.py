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

def on_entry_click(event, check, check2):
    if check2 == True:  # sign in
        if check == False:
            if txtusername.get() == "Username":
                txtusername.delete(0, END)
                txtusername.config(fg="black")
        elif check == True:
            if txtuserpassword.get() == "Password":
                txtuserpassword.delete(0, END)
                txtuserpassword.config(fg="black", show='*')
                # txtuserpassword.config(show='*')
    elif check2 == False: # sign up
        if check == False:
            if txtusername_signup.get() == "Username":
                txtusername_signup.delete(0,END)
                txtusername_signup.config(fg="black")
        elif check == True:
            if txtuserpassword_signup.get() == "Password":
                txtuserpassword_signup.delete(0,END)
                txtuserpassword_signup.config(fg="black", show='*')
        elif check == None:
            if txtuserrole_signup.get() == "Role":
                txtuserrole_signup.delete(0,END)
                txtuserrole_signup.config(fg="black")

def on_Leave(event, check, check2):
    if check2 == True: # sign in
        if check == False:
            if txtusername.get() == '':
                txtusername.insert(0,"Username")
        elif check == True:
            if txtuserpassword.get() == '':
                txtuserpassword.config(show="")
                txtuserpassword.insert(0,"Password")
    elif check2 == False:
        if check == False:
            if txtusername_signup.get() == '':
                txtusername_signup.insert(0,"Username")
        elif check == True:
                if txtuserpassword_signup.get() == '':
                    txtuserpassword_signup.config(show="")
                    txtuserpassword_signup.insert(0,"Password")
        elif check == None:
                if txtuserrole_signup.get() == '':
                    txtuserrole_signup.insert(0,"Role")
def On_Click(event, item):
    if item == "name":
        if txtproductname.get() == "Product Name":
            txtproductname.delete(0,END)
            txtproductname.config(fg="black")
    elif item == "price":
        if txtproductprice.get() == "Product Price":
            txtproductprice.delete(0,END)
            txtproductprice.config(fg="black")
    elif item == "quantity":
        if txtproductquantity.get() == "Product Quantity":
            txtproductquantity.delete(0, END)
            txtproductquantity.config(fg="black")

def OnLeave(event, item):
    if item == "name":
        if txtproductname.get() == '':
            txtproductname.insert(0,"Product Name")
    elif item == "price":
        if txtproductprice.get() == '':
            txtproductprice.insert(0, "Product Price")
    elif item == "quantity":
        if txtproductquantity.get() == '':
            txtproductquantity.insert(0, "Product Quantity")

def showPassword():
    showpass = Button(frame, image=hideimage, command= HidePassword, border=0, bg="white")
    showpass.place(x=310,y=140)
    txtuserpassword.config(show="")
   

def HidePassword():
    hidepass = Button(frame, image=showimage, border=0, command=showPassword, bg="white")
    hidepass.place(x=310,y=140)
    txtuserpassword.config(show='*')
    
def showPassword_SignUp():
    showpass = Button(frame1, image=hideimage, command= HidePassword_SignUp, border=0, bg="white")
    showpass.place(x=310,y=140)
    txtuserpassword_signup.config(show="")

def HidePassword_SignUp():
    hidepass = Button(frame1, image=showimage, border=0, command=showPassword_SignUp, bg="white")
    hidepass.place(x=310,y=140)
    txtuserpassword_signup.config(show='*')

def show_page(page):
    SignInPage.pack_forget()
    SignUpPage.pack_forget()
    AdminPage.pack_forget()
    ViewProductsPage.pack_forget()
    AddProductsPage.pack_forget()
    DeleteProductsPage.pack_forget()
    page.pack(side=TOP, fill=BOTH, expand=True)
    page.tkraise()

def SetSignUpValuesDefault():
    txtusername_signup.delete(0,END)
    txtuserpassword_signup.delete(0,END)
    txtuserrole_signup.delete(0,END)
    txtusername_signup.insert(0,"Username")
    txtuserpassword_signup.config(show="")
    txtuserpassword_signup.insert(0,"Password")
    txtuserrole_signup.insert(0,"Role")
    
def SetSignInValuesDefault():
    txtusername.delete(0,END)
    txtuserpassword.delete(0,END)
    txtusername.insert(0,"Username")
    txtuserpassword.config(show="")
    txtuserpassword.insert(0,"Password")
    
def btnSignUp():
    try:
        username = txtusername_signup.get()
        password = txtuserpassword_signup.get()
        role = txtuserrole_signup.get()
        if username != "Username" and username != '':
            if password != "Password" and password != '':
                if role != "Role" and role != '' and ((role !="Admin" or role !="admin") or(role != "User" or role != "user")):
                    user = SignUp_BL(username,password, role)
                    MUser_DL.AddInList(user)
                    MUser_DL.StoreUserInFile("Users.txt")
                    print(txtusername_signup.get(), txtuserpassword_signup.get(), txtuserrole_signup.get())
                    msg.showinfo("Sign Up", "Signed Up Successfully")
                    SetSignUpValuesDefault()
                else:
                    msg.showerror("Role Error", "Please Enter Valid Role")
            else:
                msg.showerror("Password Error", "Please Enter Valid Password")
        else:
            msg.showerror("Username Error", "Please Enter Valid Username")
    except Exception as e:
        print("An Error Occured", e)

def btnSignIn():
    username = txtusername.get()
    password = txtuserpassword.get()
    if (username != None and username != "Username") and (password != None and password != "Password"):
        signinuser = SignIn_BL(username, password)
        getrole = MUser_DL.GetRole(signinuser)
        if getrole == "Admin" or getrole == "admin":
            msg.showinfo("","Welcome Admin Menu")
            SetSignInValuesDefault()
        elif getrole == "User" or getrole == "user":
            msg.showinfo("","Welcome User Menu")
            SetSignInValuesDefault()
        else:
            msg.showerror("Error", "User Not Found")
    else:
        msg.showerror("Error", "Invalid Credentials")

def displayProducts(grid):
    for i,item in enumerate(Products_DL.productsList):
        grid.insert("", "end", values=(i+1,item.GetProductName, item.GetProductQuantity, item.GetProductPrice))
        
def DatagridCenter(gridname):
    for col in gridname["columns"]:
        gridname.column(col, anchor='center')

def SetProductsDefaultValues():
    txtproductname.delete(0,END)
    txtproductprice.delete(0,END)
    txtproductquantity.delete(0,END)
    txtproductname.insert(0,"Product Name")
    txtproductprice.insert(0,"Product Price")
    txtproductquantity.insert(0, "Product Quantity")
    
def clear_datagrid(grid):
    grid.delete(*grid.get_children())

def UpdateGrid(grid):
    clear_datagrid(grid)
    displayProducts(grid)
def addproduct():
    try:
        if txtproductname.get() != None and txtproductname.get() != "Product Name":
            if txtproductprice.get() != NONE and txtproductprice.get() != "Product Price":
                if txtproductquantity.get() != None and txtproductquantity.get() != "Product Quantity":
                    product = Manager_BL(txtproductname.get(), txtproductquantity.get(), txtproductprice.get())
                    Products_DL.AddInProductList(product)
                    Products_DL.StoreProductsInfile("Products.txt")
                    UpdateGrid(datagrid)
                    UpdateGrid(datagrid_deleteproduct)
                    msg.showinfo("Product Added","Product has been added successfully")
                    SetProductsDefaultValues()
                else:            
                   msg.showerror("Error","Invalid Quantity")
            else:
                msg.showerror("Error","Invalid Price")
        else:
            msg.showerror("Error","Invalid Name")
    except Exception as e:
        msg.showerror("An Error Occured", e)

Products_DL.ReadProductFromFile("Products.txt")
MUser_DL.ReadUserFromFile("Users.txt")
root = Tk()
root.geometry("1000x800")
root.title("Grocery Store Management System")

SignInPage = Frame(root, bg="white")
SignUpPage = Frame(root, bg="white")
AdminPage = Frame(root, bg="white")
ViewProductsPage = Frame(root, bg="white")
AddProductsPage = Frame(root, bg="white")
DeleteProductsPage = Frame(root, bg="white")

SignInPage.pack(side=TOP, fill=BOTH, expand=True)
SignUpPage.pack(side=TOP, fill=BOTH, expand=True)
AdminPage.pack(side=TOP, fill=BOTH, expand= True)
ViewProductsPage.pack(side=TOP, fill=BOTH, expand=TRUE)
AddProductsPage.pack(side=TOP, fill=BOTH, expand= True)
DeleteProductsPage.pack(side=TOP, fill=BOTH, expand=True)

 ## -----------   Sign In Page ----------- ##

Label(root, text="Grocery Store Management System", bg="Light blue", fg="black", font="Serif 30 bold", pady=10).pack(side=TOP, fill=X)
root.grid_columnconfigure(0, weight=1)

img = Image.open("1.png")
img_resize = img.resize((500,500), Image.LANCZOS)
photo = ImageTk.PhotoImage(img_resize)
lblImage = Label(SignInPage,image=photo)
lblImage.place(x=5, y = 100)

frame = Frame(SignInPage, width=350, height=350, bg="white")
frame.place(x = 600, y = 150)

heading = Label(frame, text = "Sign In", bg="White", fg="#57a1f8", font = ('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=100, y = 0)

usernamesignIn = StringVar()
usernamesignIn.set("")
txtusername = Entry(frame, textvariable=usernamesignIn, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtusername.insert(0,"Username")
txtusername.bind("<FocusIn>", lambda event: on_entry_click(event, False, True))
txtusername.bind("<FocusOut>" , lambda event: on_Leave(event, False, True))
txtusername.place(x=45,y=80)

Frame(frame, width=290, height=2, bg="black").place(x= 40, y = 107)

## For Password

userpasswordsignIn = StringVar()
userpasswordsignIn.set("")
txtuserpassword = Entry(frame, textvariable=userpasswordsignIn, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtuserpassword.insert(0,"Password")
txtuserpassword.bind("<FocusIn>", lambda event: on_entry_click(event, True, True))
txtuserpassword.bind("<FocusOut>" , lambda event: on_Leave(event, True, True))
hideimage = ImageTk.PhotoImage(file="hide.ico")
showimage = ImageTk.PhotoImage(file = "show.ico")
hideButton = Button(frame, image=showimage, border=0, bg="white", command= showPassword)
hideButton.place(x=310,y=140)
txtuserpassword.place(x=45,y=150)
Frame(frame, width=290, height=2, bg="black").place(x= 40, y = 177)

Button(frame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=btnSignIn).place(x = 45, y = 204)

label = Label(frame, text="Dont't have an account?" , fg="black", bg="white", font=('Microsoft YaHei UI Light', 9))
label.place(x = 70, y = 270)
signup = Button(frame, width=6, text="Sign Up", border=0, bg="white", fg="#57a1f8", cursor="hand2", command= lambda: show_page(SignUpPage))
signup.place(x = 215, y = 270)


## --------------- Sign Up Page ---------------- ##

lblImage2 = Label(SignUpPage,image=photo)
lblImage2.place(x=5, y = 100)

frame1 = Frame(SignUpPage, width=350, height=400, bg="white")
frame1.place(x = 600, y = 150)

heading = Label(frame1, text = "Sign Up", bg="White", fg="#57a1f8", font = ('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=100, y = 0)

username_signup = StringVar()
username_signup.set("")
txtusername_signup = Entry(frame1, textvariable=username_signup, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtusername_signup.insert(0,"Username")
txtusername_signup.bind("<FocusIn>", lambda event: on_entry_click(event, False, False))
txtusername_signup.bind("<FocusOut>" , lambda event: on_Leave(event, False, False))
txtusername_signup.place(x=45,y=80)

Frame(frame1, width=290, height=2, bg="black").place(x= 40, y = 107)

## For Password

userpassword_signup = StringVar()
userpassword_signup.set("")
txtuserpassword_signup = Entry(frame1, textvariable=userpassword_signup, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtuserpassword_signup.insert(0,"Password")
txtuserpassword_signup.bind("<FocusIn>", lambda event: on_entry_click(event, True, False))
txtuserpassword_signup.bind("<FocusOut>" , lambda event: on_Leave(event, True, False))
# hideimage = ImageTk.PhotoImage(file="hide.ico")
# showimage = ImageTk.PhotoImage(file = "show.ico")
hideButton1 = Button(frame1, image=showimage, border=0, bg="white", command=showPassword_SignUp)
hideButton1.place(x=310,y=140)
txtuserpassword_signup.place(x=45,y=150)
Frame(frame1, width=290, height=2, bg="black").place(x= 40, y = 177)

## For Role

userrole_signUp = StringVar()
userrole_signUp.set("")
txtuserrole_signup = ttk.Combobox(frame1, values=["Admin", "User"], width=33, height=10, font= ('Microsoft YaHei UI Light', 11))
#txtuserrole_signup = Entry(frame1, textvariable=userrole_signUp, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtuserrole_signup.insert(0,"Role")
#txtuserrole_signup.bind("<FocusIn>", lambda event: on_entry_click(event, None, False))
#txtuserrole_signup.bind("<FocusOut>" , lambda event: on_Leave(event, None, False))
txtuserrole_signup.place(x = 45, y = 215)
Frame(frame1, width=290, height=2, bg="black").place(x= 40, y = 247)


Button(frame1, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=btnSignUp).place(x = 45, y = 280)
GotoSignIn = Button(frame1, width=20, pady=7, text="Go to Sign In", bg="#57a1f8", fg="white", border=0, command= lambda: show_page(SignInPage))
GotoSignIn.place(x=45, y = 350)

##--------------------------------------------------##
## ---------------- Admin Page --------------------- ##
## ---------------------------------------------------##

Adminframe = Frame(AdminPage, width=350, height=650, bg="white smoke")
Adminframe.place(x = 0, y = 0)

img = Image.open("managerLogo.png")
img_resize = img.resize((300,300), Image.LANCZOS)
photo = ImageTk.PhotoImage(img_resize)
lblImage = Label(AdminPage,image=photo,bg="White smoke")
lblImage.place(x=25, y = 70)

lbladminMenu = Label(Adminframe , text= "Admin Menu", font= ('Manrope', 30 , 'bold') , bg="white smoke", fg="#57a1f8")
lbladminMenu.place(x = 65, y = 400)

ProductsFrame = Frame(AdminPage , width=700, height=500, bg= "white smoke")
ProductsFrame.place(x=450, y = 50)



viewProductsImage = Image.open("ViewProducts.png")
imgResize = viewProductsImage.resize((100,100) , Image.LANCZOS)
photoproduct = ImageTk.PhotoImage(imgResize)    
btnViewProducts = Button(ProductsFrame , image=photoproduct, borderwidth=6, bg="#57a1f8", command= lambda: show_page(ViewProductsPage)) ## View Products
btnViewProducts.place(x= 50, y= 50)    
Label(ProductsFrame, text = "View Products", font= ('Manrope', 10 , 'bold'), bg="white smoke").place(x=55, y = 170)

AddProductsImage = Image.open("AddProduct.png")
imgResize1 = AddProductsImage.resize((100,100) , Image.LANCZOS)
photoproduct1 = ImageTk.PhotoImage(imgResize1)    
btnAddProducts = Button(ProductsFrame , image=photoproduct1, borderwidth=6, bg="#57a1f8", command= lambda: show_page(AddProductsPage)) ## Add Products
btnAddProducts.place(x= 250, y= 50)    
Label(ProductsFrame, text = "Add Products", font= ('Manrope', 10 , 'bold'), bg="white smoke").place(x=260, y = 170)

DeleteProductImage = Image.open("DeleteProduct.png")
imgResize2 = DeleteProductImage.resize((100,100), Image.LANCZOS)
photoproduct2 = ImageTk.PhotoImage(imgResize2)
btnDeleteProduct = Button(ProductsFrame, image=photoproduct2, borderwidth=6 , bg="#57a1f8", command= lambda: show_page(DeleteProductsPage)) ## Delete Products
btnDeleteProduct.place(x = 450, y = 50)
Label(ProductsFrame, text="Delete Product", font= ('Manrope', 10 , 'bold'), bg="white smoke").place(x = 460, y = 170)

UpdateProductImage = Image.open("update_product.png")
imgResize3 = UpdateProductImage.resize((100,100), Image.LANCZOS)
photoproduct3 = ImageTk.PhotoImage(imgResize3)
btnUpdateProduct = Button(ProductsFrame, image=photoproduct3, borderwidth=6 , bg="#57a1f8") ## Update Products
btnUpdateProduct.place(x = 50, y = 250)
Label(ProductsFrame, text="Update Product", font= ('Manrope', 10 , 'bold'), bg="white smoke").place(x = 55, y = 370)

## =======================================================
## ==================  View Products ===================== ##
## =========================================================

ViewProductFrame = Frame(ViewProductsPage, width=350, height=650, bg="white smoke")
ViewProductFrame.place(x = 0, y = 0)

ViewProduct_img = Image.open("managerLogo.png")
ViewProduct_img_resize = ViewProduct_img.resize((300,300), Image.LANCZOS)
ViewProduct_photo = ImageTk.PhotoImage(ViewProduct_img_resize)
ViewProduct_lblImage = Label(ViewProductFrame,image=ViewProduct_photo,bg="White smoke")
ViewProduct_lblImage.place(x=25, y = 70)

lblproductinfo = Label(ViewProductFrame , text= "Products Info", font= ('Manrope', 30 , 'bold') , bg="white smoke", fg="#57a1f8")
lblproductinfo.place(x = 65, y = 400)

datagridframe = Frame(ViewProductsPage, width=900, height=500, bg="white")
datagridframe.place(x = 400, y = 70)

datagrid = ttk.Treeview(datagridframe, columns=("Column0","Column1", "Column2", "Column3"), show="headings")
datagrid.heading("Column0", text="No.")
datagrid.heading("Column1", text="Product Name" )
datagrid.heading("Column2", text="Product Quantity")
datagrid.heading("Column3", text="Product Price")
datagrid.place(x = 0, y = 50)
DatagridCenter(datagrid)
displayProducts(datagrid)
style = ttk.Style()
#style.configure("Custom.Treeview", padding=(0, 5))
style.configure("Custom.Treeview", padding=(5, 5), rowheight = 30)  # Adjust padding values as needed
style.configure("Custom.Treeview.Heading", padding=(0, 2))
datagrid.configure(style="Custom.Treeview")

Gotoadmenu = Button(datagridframe, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= lambda: show_page(AdminPage))
Gotoadmenu.place(x=0, y = 400)

 ## =====================================================================
 ## ========================   Add Product Page ====================== ##
 ## =======================================================================
 
AddProductFrame = Frame(AddProductsPage, width=350, height=650, bg="white smoke")
AddProductFrame.place(x = 0, y = 0) 
 
AddProduct_img = Image.open("managerLogo.png")
AddProduct_img_resize = AddProduct_img.resize((300,300), Image.LANCZOS)
AddProduct_photo = ImageTk.PhotoImage(AddProduct_img_resize)
AddProduct_lblImage = Label(AddProductFrame,image=AddProduct_photo,bg="White smoke")
AddProduct_lblImage.place(x=25, y = 70)

lblAddProduct = Label(AddProductFrame , text= "Add Products", font= ('Manrope', 30 , 'bold') , bg="white smoke", fg="#57a1f8")
lblAddProduct.place(x = 65, y = 400)

Addproductframe2 = Frame(AddProductsPage, bg="white", width=600, height=400)
Addproductframe2.place(x = 500, y = 100)

ProductName = StringVar()
ProductPrice = StringVar()
ProductQuantity = StringVar()
ProductName.set("")
ProductPrice.set("")
ProductQuantity.set("")

txtproductname = Entry(Addproductframe2, textvariable=ProductName, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtproductname.insert(0,"Product Name")
txtproductname.bind("<FocusIn>", lambda event: On_Click(event,"name"))
txtproductname.bind("<FocusOut>", lambda event: OnLeave(event,"name"))
txtproductname.place(x = 50, y = 50)
Frame(Addproductframe2, width=280, height=2, bg="black").place(x= 50, y = 80)

txtproductprice = Entry(Addproductframe2, textvariable=ProductPrice, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtproductprice.insert(0,"Product Price")
txtproductprice.bind("<FocusIn>", lambda event: On_Click(event,"price"))
txtproductprice.bind("<FocusOut>", lambda event: OnLeave(event,"price"))
txtproductprice.place(x = 50, y = 120)
Frame(Addproductframe2, width=280, height=2, bg="black").place(x= 50, y = 150)

txtproductquantity = Entry(Addproductframe2, textvariable=ProductQuantity, width=25, fg="Black", border=0, bg="white", font = ('Microsoft YaHei UI Light', 11))
txtproductquantity.insert(0,"Product Quantity")
txtproductquantity.bind("<FocusIn>", lambda event: On_Click(event,"quantity"))
txtproductquantity.bind("<FocusOut>", lambda event: OnLeave(event,"quantity"))
txtproductquantity.place(x = 50, y = 190)
Frame(Addproductframe2, width=280, height=2, bg="black").place(x= 50, y = 220)

Button(Addproductframe2, width=39, pady=7, text="Add Product", bg="#57a1f8", fg="white", border=0, command = addproduct).place(x = 50, y = 280)
GotoAdminMenu = Button(Addproductframe2, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= lambda: show_page(AdminPage))
GotoAdminMenu.place(x=50, y = 350)

## ===========================================================
## ===================  Delete Product page ==================
## ===========================================================

index = StringVar()

DeleteProductFrame = Frame(DeleteProductsPage, width=350, height=650, bg="white smoke")
DeleteProductFrame.place(x = 0, y = 0) 
 
DeleteProduct_img = Image.open("managerLogo.png")
DeleteProduct_img_resize = DeleteProduct_img.resize((300,300), Image.LANCZOS)
DeleteProduct_photo = ImageTk.PhotoImage(DeleteProduct_img_resize)
DeleteProduct_lblImage = Label(DeleteProductFrame,image=DeleteProduct_photo,bg="White smoke")
DeleteProduct_lblImage.place(x=25, y = 70)

lblDeleteProduct = Label(DeleteProductFrame , text= "Delete Products", font= ('Manrope', 30 , 'bold') , bg="white smoke", fg="#57a1f8")
lblDeleteProduct.place(x = 35, y = 400)

datagridframe_deletepage = Frame(DeleteProductsPage, width=900, height=500, bg="white")
datagridframe_deletepage.place(x = 400, y = 70)

datagrid_deleteproduct = ttk.Treeview(datagridframe_deletepage, columns=("Column0","Column1", "Column2", "Column3"), show="headings")
datagrid_deleteproduct.heading("Column0", text="No.")
datagrid_deleteproduct.heading("Column1", text="Product Name" )
datagrid_deleteproduct.heading("Column2", text="Product Quantity")
datagrid_deleteproduct.heading("Column3", text="Product Price")
datagrid_deleteproduct.place(x = 0, y = 50)
DatagridCenter(datagrid_deleteproduct)
displayProducts(datagrid_deleteproduct)
style2 = ttk.Style()
#style.configure("Custom.Treeview", padding=(0, 5))
style2.configure("Custom.Treeview", padding=(5, 5), rowheight = 30)  # Adjust padding values as needed
style2.configure("Custom.Treeview.Heading", padding=(0, 2))
datagrid_deleteproduct.configure(style="Custom.Treeview")

def on_item_select(event, grid):
    global index
    selected_items = grid.selection()
    if selected_items:
        selected_item = selected_items[0]  # Get the selected item's ID
        i = str(grid.index(selected_item))
        index.set(str(i)) 
        print(index.get())
    
    


datagrid_deleteproduct.bind("<<TreeviewSelect>>", lambda event, grid=datagrid_deleteproduct: on_item_select(event, grid))

Gotoadmenu2 = Button(datagridframe_deletepage, width=20, pady=7, text="Go Back", bg="#57a1f8", fg="white", border=0, command= lambda: show_page(AdminPage))
Gotoadmenu2.place(x=0, y = 400)

def DeleteProduct():  ## index ko -1 ya x krna hy ===================
    
    selectedItem = (index.get())
    if selectedItem:
            selectedItem = int(selectedItem)
            val = msg.askyesno("Question","Do you want to delete that Product? ")
            if val:
                Products_DL.DeleteProducts(selectedItem)
                UpdateGrid(datagrid_deleteproduct)
                UpdateGrid(datagrid)
                Products_DL.StoreProductsInfile("Products.txt")
                msg.showinfo("Deleted","Your Item has been deleted")
            else:
                msg.showinfo("Cancelled","Your operation has been cancelled")
            
    else:
        msg.showerror("Error","Item not selected")

deleteitem = Button(datagridframe_deletepage, width=20, pady=7, text="Delete", bg="red", fg="white", border=0, command=DeleteProduct)
deleteitem.place(x = 200, y = 400)

## ====================================================
##= ================== Update Product ==================
## =====================================================

show_page(AdminPage)
root.mainloop()