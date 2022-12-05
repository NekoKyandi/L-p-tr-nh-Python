import speedtest
import tkinter 
from tkinter import *
import tkinter.messagebox
# khai báo speedtest
# st = speedtest.Speedtest()
# gán biến st với thư viện speed test có sẵn trong python 
option =""
# option = int(input('''What speed do you want to test (Bạn muốn kiểm tra loại tốc độ nào?):  
# 1) Download Speed (Tốc độ tải xuống) 
# 2) Upload Speed  (Tốc độ tải lên)
# 3) Ping (Tốc độ mạng)
# Your Choice (Lựa chọn của bạn là?): '''))
# nhập đầu vào với kiểu dữ liệu int với option là 1 or 2 or 3


def show():
    st = speedtest.Speedtest()
    global option
    if option == 1:  
        # lựa chọn 1
        choose = "Download"
        speed = st.download()
        # gán giá trị vào speed
    elif option == 2: 
        # lựa chọn 2
        choose = "Upload"
        speed = st.upload()
        # gán giá trị vào speed
    elif option == 3:  
        # lựa chọn 3
        choose = "Ping"
        servernames =[]  
        # Khai báo servernames là 1 danh sách
        st.get_servers(servernames)  
        # lấy dữ liệu servernames trong thư viện speedtest
        speed = st.results.ping
        # gán giá trị vào speed
    else:
        # Nếu đầu vào (option) không hợp lệ (1,2,3) thì chạy lệnh print
        print("Please enter the correct choice!")
        print("Vui lòng nhập đúng lựa chọn!")

    #  phân loại tốc tộ mạng
    if(speed<1000):
        speedWithUnits=str(round(speed, 3))+" bps"
    elif(speed<1000000):
        speedWithUnits=str(round(speed/1000, 3))+" Kbps"
    elif(speed<1000000000):
        speedWithUnits=str(round(speed/1000000, 3))+" Mbps"
    else:
        speedWithUnits=str(round(speed/1000000000, 3))+" Gbps"
    # print("Lựa chọn của bạn : {0}, Speed: {1}".format(choose, speedWithUnits ))
    tkinter.messagebox.showinfo("Kết quả","xin chào, tốc độ " +choose+" của bạn là:"+speedWithUnits)

def download():
    print ("dow")
    global option
    option=1
    show()

def upload():
    print ("up")
    global option
    option=2
    show()

def ping():
    print ("ping")
    global option
    option= 3
    show()

wn = tkinter.Tk()
wn.title("Trình kiểm tra tốc độ Internet của bạn")
wn.geometry('700x300')
wn.config(bg='azure')
 
Label(wn, 
    text='Bạn không biết tốc độ mạng của mình là bao nhiêu?.',
    bg='azure',
    fg='black', 
    font=('Courier', 15)).place(x=18, y=10)

Label(wn, 
    text='Kiểm tra tốc độ bạn của bạn ngay nào!.',
    bg='azure',
    fg='black', 
    font=('Courier', 12)).place(x=30, y=40)

Button(wn, 
    text="Check Download Speed", 
    bg='ivory3',
    font=('Courier', 15),
    width=20,
    command=download).place(x=230, y=80)

Button(wn, 
    text="Check Upload Speed", 
    bg='ivory3',
    font=('Courier', 15),
    width=20,
    command=upload).place(x=230, y=150)

Button(wn, 
    text="Check Ping", 
    bg='ivory3',
    font=('Courier', 15),
    width=20,
    command=ping).place(x=230, y=220)

wn.mainloop()