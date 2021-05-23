import asyncio
from pyppeteer import launch
import time
from datetime import datetime
from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter import*

def now():
    dt = datetime.now()
    timee=3600-(dt.minute*60)-dt.second-dt.microsecond*0.000001
    return timee
def patch_pyppeteer():
    import pyppeteer.connection
    original_method = pyppeteer.connection.websockets.client.connect

    def new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)

    pyppeteer.connection.websockets.client.connect = new_method


patch_pyppeteer()
def chrome():
  async def main():
    Link=link.get()
    Sec=float(sec.get())
    User=user.get()
    Password=password.get()
    browser = await launch({
      'executablePath': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
      'headless': False})
    page1=await browser.newPage()
    await page1.goto('chrome://settings/content/images')
    time.sleep(2)
    page = await browser.newPage()
    await page.goto(Link)
    await page.waitForSelector('#login-form-validate > div.switch-div.no-animation.active.social > div > a.btn.btn-link.div-trigger.fixed-trigger.float-left')
    await page.click('#login-form-validate > div.switch-div.no-animation.active.social > div > a.btn.btn-link.div-trigger.fixed-trigger.float-left')
    await page.waitForSelector('#log_username')
    await page.focus('#log_username')
    await page.keyboard.type(User)
    await page.waitForSelector('#log_password')
    await page.focus('#log_password')
    await page.keyboard.type(Password)
    time.sleep(1)
    await page.waitForSelector('#login_real')
    await page.click('#login_real')
    await page.waitForSelector('#root > div > div.container.saveOrder_zf5y > div.right_16Bw > div:nth-child(2) > div.content_1e24 > div.billTotalCost_1I5b > div:nth-child(1) > span.price')
    time.sleep(now()-6)
    await page.reload()
    time.sleep(now()-Sec)
    await page.reload()
    for i in range(10):
      await page.waitForSelector('#root > div > div.container.saveOrder_zf5y > div.right_16Bw > div:nth-child(2) > div.content_1e24 > div.billTotalCost_1I5b > div:nth-child(1) > span.price')
      price=await page.querySelectorEval('#root > div > div.container.saveOrder_zf5y > div.right_16Bw > div:nth-child(2) > div.content_1e24 > div.billTotalCost_1I5b > div:nth-child(1) > span.price','(e => e.innerText)')
      if len(price)<8:
        await page.waitForSelector('#root > div > div.container.saveOrder_zf5y > div.right_16Bw > div.placeHolder_3wIg > div > div > div > button')
        await page.click('#root > div > div.container.saveOrder_zf5y > div.right_16Bw > div.placeHolder_3wIg > div > div > div > button')
        break
      else:
        await page.reload()
        
          
    time.sleep(50)
    await browser.close()

  asyncio.get_event_loop().run_until_complete(main())

class Example(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.parent = parent
    self.initUI()
  
  def initUI(self):
    self.parent.title("Doreamon")
    self.pack(fill=BOTH, expand=1)
    global user
    global password
    global link
    global sec
    user=StringVar()
    user.set('0368948823')
    password=StringVar()
    password.set('anhyeuem')
    link=StringVar()
    sec=StringVar()
    sec.set('0.25')
    frame000=Frame(self)
    frame000.pack(fill=X)
    lbl1 = Label(frame000, text="User:",fg='red')
    en1=Entry(frame000,textvariable=user)
    lbl1.pack(side=LEFT, padx=4, pady=5)
    en1.pack(side =LEFT, pady=5, expand=True)
    lbl2 = Label(frame000, text="Pass:",fg='red')
    en2=Entry(frame000,show="*",textvariable=password)
    lbl2.pack(side=LEFT, padx=4, pady=5)
    en2.pack(side =LEFT, pady=5, expand=True)
    frame001=Frame(self)
    frame001.pack(fill=X,pady=50,padx=5)
    lb001 = Label(frame001, text="Link:",fg='red')
    en001=Entry(frame001,width=35,textvariable=link)
    lb001.pack(side=LEFT, pady=10)
    en001.pack(side =LEFT, expand=True)
    en002=Entry(frame001,width=5,textvariable=sec,fg='red')
    en002.pack(side =LEFT, expand=True)
    frame1=Frame(self)
    frame1.pack(fill=X,padx=0)
    btn=Button(frame1,text ="Hốt thôi",command=chrome,fg='white',bg='#00CC00',width=80)
    btn.pack(side =LEFT,padx=100,pady=5)

  
  def onSelect(self, val):
    sender = val.widget
    idx = sender.curselection()
    value = sender.get(idx)
    self.var.set(value)
 
root = Tk()
ex = Example(root)
root.geometry("350x300+200+10")
root.mainloop()
