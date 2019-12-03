import sys
import time
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout #for popup 'x' button
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class PrintLog:
    def __init__(self, filename):
        self.out_file = open(filename, "a+")
        self.old_stdout = sys.stdout

        sys.stdout = self
    #executed when software does print
    def write(self, text): 
        self.old_stdout.write(text)
        self.out_file.write(text)
        
    #executed when with block begins
    def __enter__(self): 
        return self
    #executed when with block ends
    def __exit__(self, type, value, traceback): 
        #stop logging
        sys.stdout = self.old_stdout
    
    def setfilename():
    	timestr = time.strftime("%Y%m%d-%H%M%S")
    	filename1 = "worklog.txt"
    	curfilename = timestr+filename1
    	return curfilename

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)
        
        self.inside = BoxLayout(spacing = 10)
        self.add_widget(self.inside)
        
        
        self.btn1 = Button(text="Create Report", size_hint=(.5, .3))
        
        self.btn1.bind(on_press=self.callback)
        self.add_widget(self.btn1)
        
        
        self.btn2 = Button(text="Open popup", size_hint=(.5, .3))
        
        self.btn2.bind(on_press=self.workscreen)
        self.add_widget(self.btn2)
        
        content = RelativeLayout()
        content_cancel = Button(text='confirm', 
        				pos_hint={'center_x': 0.5, 'center_y': 0.15}, 
        				size_hint=(.35, .25),
        				background_normal='',
        				background_color=(0, 0.4, 1, 1))
        content.add_widget(content_cancel)
        content.add_widget(Label(text="This is some helpful text."))
        self.popup = Popup(title='Popup title', #separator_height=0,
        			#content=Button(text='Close me!', pos_hint={'left': 1, 'top': 1}),
        			#title_size=0, #font size only
        			#title_align=(left),
        			content=content,
        			auto_dismiss=False,
        			size_hint=(None, None), size=(400, 400))
        
        #self.popup.content.bind(on_press=self.popup.dismiss)
        content_cancel.bind(on_press=self.popup.dismiss) #for popup 'x' button
        
        self.btn3 = Button(text="Create worklog", size_hint=(.5, .3))
        
        self.btn3.bind(on_press=self.worklog)
        self.add_widget(self.btn3)
        
        self.workloglist=[]
        
    	
    def worklog(self, instance):
    	print("worklog is being pressed...")
    	print("Timestamp: %s" % time.ctime())
    	self.workloglist.append("Create worklog is being pressed...")
    	self.workloglist.append("Timestamp: %s" % time.ctime())
    	
    	print("YOUR WORKLOG:")
    	with PrintLog(PrintLog.setfilename()):
    		for work in self.workloglist:
    			print(work)
        
    def workscreen(self, instance):
        self.popup.open()
    
    def callback(self, instance):
    	print('Create report is being pressed...')
    	print("Timestamp: %s" % time.ctime())
    	self.workloglist.append("Create report is being pressed...")
    	self.workloglist.append("Timestamp: %s" % time.ctime())
    
    

class MainApp(App):

    def build(self):
    
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            #Color(0, 1, 0)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    MainApp().run()

