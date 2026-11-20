import tkinter as tk
#创建弹窗前的导包
from tkinter import messagebox
#导入json文件，用于存储数据
import json
#创建主窗口
mainroot=tk.Tk()
#设置窗口标题
mainroot.title("Welcome")
#设置窗口大小及位置
mainroot.geometry('500x500+600+300')
#窗口锁定
mainroot.resizable(width=False, height=False)
#窗口置顶，不被覆盖
mainroot.attributes('-topmost', True)
#设置窗口关闭时执行的函数
def goodbye():
    #四种弹窗（前三个图标不一样，最后一个有确认取消两个按钮）：showerror，showinfo，showwarning，askokcancel（标题，文本内容）
    result=messagebox.askokcancel("提醒","你确定退出")
    if result:
        # 销毁窗口
        mainroot.destroy()
    else:
        pass
#销毁窗口时执行函数，'WM_DELETE_WINDOW'为固定语句
mainroot.protocol('WM_DELETE_WINDOW',goodbye)
#标签组件（窗口，文本，字体，字体颜色fg，背景bg）+组件布局[填充布局pack(),自定义布局place (x=,y=),网格布局grid(row=,column=)]
tk.Label(mainroot,text="Welcome to Milktea!",font=(26)).place(x=150,y=0)
tk.Label(mainroot,text="账号:",font=(26)).place(x=80,y=100)
tk.Label(mainroot,text="密码:",font=(26)).place(x=80,y=150)
#设置变量以获取用户输入的账号及密码
username=tk.StringVar()
password=tk.StringVar()
#设置提示文本（或者说设置变量的默认值）
username.set("请输入账号")
password.set("请输入密码")
#输入框组件（窗口，传参，宽度，字体）
tk.Entry(mainroot,textvariable=username,width=30).place(x=150,y=100)
tk.Entry(mainroot,textvariable=password,width=30).place(x=150,y=150)

def login():
    #with open打开文件（文件名，权限）；as f将文件命名为f
    with open("users.json","r") as f:
        #load（f）将文本转换为列表/字典，便于读取
        user_list=json.load(f)
    #遍历查找
    for user in user_list:
        if user["Username"]==username.get().strip() and user["Password"]==password.get().strip():#get()是读取变量，strip()用于去除首尾空格
                messagebox.showinfo("Welcome","登录成功")
    else:
        messagebox.showerror("错误","账号或密码错误")

def register():
    #创建子窗口
    register_root = tk.Toplevel()
    # 设置窗口标题
    register_root.title("注册")
    # 设置窗口大小及位置
    register_root.geometry('500x500+600+300')
    # 窗口锁定
    register_root.resizable(width=False, height=False)
    # 窗口置顶，不被覆盖
    register_root.attributes('-topmost', True)
    # 标签组件（窗口，文本，字体，字体颜色fg，背景bg）+组件布局
    tk.Label(register_root, text="Welcome to Milktea!", font=(26)).place(x=150, y=0)
    tk.Label(register_root, text="账号:", font=(26)).place(x=80, y=100)
    tk.Label(register_root, text="密码:", font=(26)).place(x=80, y=150)
    # 设置变量以获取用户输入的账号及密码
    register_username=tk.StringVar()
    register_password=tk.StringVar()
    # 输入框组件（窗口，传参获取输入信息，宽度，字体）
    tk.Entry(register_root, textvariable=register_username, width=30).place(x=150, y=100)
    tk.Entry(register_root, textvariable=register_password, width=30).place(x=150, y=150)
    def register2():
        # 拦截空名字
        if not register_username.get().strip():
            messagebox.showerror("Wrong","Name cannot be empty")
            raise ValueError("Name cannot be empty")
        if not register_password.get().strip():
            messagebox.showerror("Wrong","Name cannot be empty")
            raise ValueError("Name cannot be empty")
        #初始化，保证列表存在
        user_list=[]
        # with open打开文件（文件名，权限）；as f将文件命名为f
        with open("users.json", "r") as f:
            # load（f）将文本转换为列表/字典，便于读取
            user_list = json.load(f)
        # 遍历查找
        for user in user_list:
            #[""]里的是键名
            if user["Username"] == register_username.get().strip() and user["Password"] == register_password.get().strip():
                messagebox.showinfo("注意","存在账户信息")
                #返回主窗口,即销毁子窗口
                register_root.destroy()
                break
        else: #else和for组一起，如果break触发就执行else
            # with open打开文件（文件名，权限）；as f将文件命名为f
            with open("users.json","w") as f:
                # 这里的Username,Password就是自己设置的键名
                new_user = {"Username": register_username.get().strip(), "Password": register_password.get().strip()}
                # append将new_user的信息添加进列表中
                user_list.append(new_user)
                # dump（user_list,f）将列表/字典转换为文本，刚好与load作用相反，indent=?缩进几格
                json.dump(user_list,f,indent=4)
            messagebox.showinfo("Welcome","注册成功")
            register_root.destroy()
    tk.Button(register_root, command=register2, text="注册", font=(26), width=5).place(x=250, y=200)
    register_root.mainloop()
#按钮组件（窗口，参数（按钮的触发开关，即点击按钮就运行command指定的函数），文本，字体，宽度）
tk.Button(mainroot,command=login,text="登录",font=(26),width=5).place(x=150,y=200)
tk.Button(mainroot,command=register,text="注册",font=(26),width=5).place(x=250,y=200)
#开启窗口
mainroot.mainloop()
