
from datetime import date
from datetime import datetime
from datetime import timedelta
import csv
today = date.today()
from tkinter import *
from reportlab.pdfgen import canvas

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1300,height = 700)
        self.root.minsize(width = 1300,height = 700)
        self.root.title("Eletricity Billing")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        self.Consumer_no = StringVar()

        self.last_month = IntVar()
        self.current_reading = IntVar()
        self.unit = IntVar()
        self.load = IntVar()
        self.date = StringVar()
        a = date.today()
        self.date.set(a)
        self.last_date = StringVar()
        x = a + timedelta(days=10)
        self.last_date.set(x)
        self.rs = StringVar()
        self.sub = StringVar()
        self.discount = StringVar()

        #===================================
        bg_color = "gray"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Electricity Billing",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer  No==================#
        cbill_lbl = Label(F1,text = "Customer Number",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.Consumer_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = 'black',fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

        #==================Unit Frame=====================#
        F2 = LabelFrame(self.root,text = 'Unit',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 975,height = 380)
        #===========last month
        unit_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Last Month Reading:")
        unit_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        unit_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.last_month)
        unit_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
        #===========current month
        unit_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Current Month Reading:")
        unit_lbl.grid(row = 0,column = 2,padx = 10,pady = 20)
        unit_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.current_reading)
        unit_en.grid(row = 0,column = 3,ipady = 5,ipadx = 5)
        #===========unit Content
        unit_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Number of Unit:")
        unit_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        unit_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.unit)
        unit_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======load 
        load_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Load(in kWh)")
        load_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        load_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.load)
        load_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
        #=======date 
        load_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Date")
        load_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        load_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.date)
        load_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
        #=======lastdate 
        load_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Last Date")
        load_lbl.grid(row = 1,column = 2,padx = 10,pady = 20)
        load_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.last_date)
        load_en.grid(row = 1,column = 3,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 340,height = 380)
        #===========
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 135)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Unit Amount")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.rs)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        sub_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Subcharges")
        sub_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        sub_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.sub)
        sub_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        dis_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Discount By Gov.")
        dis_lbl.grid(row = 0,column = 2,padx = 10,pady = 5)
        dis_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.discount)
        dis_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)
        

        #====================
        total_btn = Button(F4,text = "Total",bg = 'black',fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 3,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = 'black',fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 4,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = 'black',fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 5,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = 'black',fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 6,ipadx = 20)
        #=======================
        save_btn = Button(F4,text = "Save",bg = 'black',fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.save_data)
        save_btn.grid(row = 1,column = 7,ipadx = 20,padx=20)
        #=======================
        pdf_btn = Button(F4,text = "Pdf",bg = 'black',fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.generate_pdf)
        pdf_btn.grid(row = 1,column = 8,ipadx = 20,padx=10)

#Function to get total 
    def total(self):
        #=================Total Unit Prices
        self.x = self.current_reading.get()-self.last_month.get()
        self.unit.set(self.x)
        self.rs_price=(self.unit.get() * 5.5)
        self.rs.set("Rs."+str(self.rs_price))
        self.sub_price=self.rs_price*0.005
        self.sub.set("Rs."+str(self.sub_price))
        self.discount_price=self.rs_price*0.04
        self.discount.set("Rs."+str(self.discount_price))
#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"   Sample Eletricity Private Ltd.\n")
        self.txt.insert(END,f"\nCunsumer No.  : {str(self.Consumer_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No.     : {str(self.c_phone.get())}")
        self.txt.insert(END,f"\nDate          : {str(self.date.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add unit,load to bill area
    def bill_area(self):
        self.welcome_soft()
        self.txt.insert(END,f"\nLast Month Reading :{self.last_month.get()}")
        self.txt.insert(END,f"\nCurrent Reading    :{self.current_reading.get()}")
        self.txt.insert(END,f"\nUnit               :{self.unit.get()}")
        self.txt.insert(END,f"\nLoad(in kw)        :{self.load.get()}")
        self.txt.insert(END,f"\nLast date to submit:{self.last_date.get()}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\nTotal amount   : {self.rs_price+self.sub_price-self.discount_price}")
        self.txt.insert(END,f"\nWith Late Fine : {self.rs_price+self.sub_price-self.discount_price+10}")
    #Function to exit
    def exit(self):
        self.root.destroy()
    def save_data(self):
        filename = "customer_data.csv"
        data = [
            # ["Customer Name", "Phone No.", "Consumer No.", "Last Month Reading", "Current Month Reading", "Number of Units", "Load", "Date", "Last Date"],
            [self.cus_name.get(), self.c_phone.get(), self.Consumer_no.get(), self.last_month.get(), self.current_reading.get(), self.unit.get(), self.load.get(), self.date.get(), self.last_date.get()]
        ]

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("Data saved successfully!")
    def generate_pdf(self):
        filename = "bill.pdf"
        c = canvas.Canvas(filename)

        # Setting up the PDF content
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "Sample Electricity Private Ltd.")
        c.setFont("Helvetica", 12)
        c.drawString(100, 720, f"Consumer No.  : {str(self.Consumer_no.get())}")
        c.drawString(100, 700, f"Customer Name : {str(self.cus_name.get())}")
        c.drawString(100, 680, f"Phone No.     : {str(self.c_phone.get())}")
        c.drawString(100, 660, f"Date          : {str(self.date.get())}")
        c.drawString(100, 640, "===================================")
        c.drawString(100, 620, "===================================")
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 590, "Bill Area")
        c.setFont("Helvetica", 12)
        c.drawString(100, 560, f"Last Month Reading : {self.last_month.get()}")
        c.drawString(100, 540, f"Current Reading    : {self.current_reading.get()}")
        c.drawString(100, 520, f"Unit               : {self.unit.get()}")
        c.drawString(100, 500, f"Load(in kw)        : {self.load.get()}")
        c.drawString(100, 480, f"Last date to submit: {self.last_date.get()}")
        c.drawString(100, 460, "===================================")
        c.drawString(100, 430, f"Total          : {self.rs_price+self.sub_price-self.discount_price}")
        c.drawString(100, 410, f"With Late Fine : {self.rs_price+self.sub_price-self.discount_price+10}")

        # Saving and closing the PDF file
        c.save()
        print(f"PDF generated successfully: {filename}")

    #Function To Clear All Fields
root = Tk()
object = Bill_App(root)
root.mainloop()