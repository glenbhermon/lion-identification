
import wx #GUI toolkit, wx is a c++ library(wxWidgets) now ported to pyhton as wxPython]
import cv2 # OpenCV toolkit

import LeoSpyUI as lsu #wx.BoxSizer makes box grids to fit UI elements
import math
import csv
import os

from wx.lib.floatcanvas import FloatCanvas,NavCanvas

class MainWindow(lsu.MyFrame1):
    
    def __init__(self, parent):
        lsu.MyFrame1.__init__(self,parent) 
        self.PhotoMaxSize = 600 # a self
        icon = wx.Icon('logo.png', wx.BITMAP_TYPE_ANY)
        self.SetIcon(icon)
        self.flag=0

        #self.canvas = FloatCanvas.FloatCanvas(lsu.MyFrame1(self))
        #self.m_panel1 = (self.canvas)
    
    
    def reset(self,event): 
        '''
        All panels and bitmaps are reset by referencing
        their respective reset functions
        '''
        self.cList =[]
        self.m_bitmap21.SetBitmap(wx.NullBitmap)
        self.m_bitmap2.SetBitmap(wx.NullBitmap)
        self.m_textCtrl2.Clear()
        self.m_panel1.Refresh()
        self.flag=0

    def Log(self, text):
        '''
        This is a small function that we defined 
        to be able to keep sending whatever message we want to display
        within the window in the form of status text messages
        '''
        self.m_textCtrl2.AppendText(text)
        if not text[-1] == "\n":
            self.m_textCtrl2.AppendText("\n")


    def onBrowse(self, event):
        """ 
        Browse for file
        """
        '''
        function to browse for an image and get its filepath
        '''
        wildcard = "All files (*.*)|*.*"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt = (dialog.GetPath()) #saves the path address
        else:
            self.onBrowse(event)
        dialog.Destroy()
        self.img = wx.Image(self.photoTxt, wx.BITMAP_TYPE_ANY) # loads the image into img
        self.flag+=1
        self.onZoom(event=None) #in-house function call
        self.cList =[]

    def onView(self):
        self.filepath = self.photoTxt#Duplicate filepath from the filepath in photoTxt
        
        self.img0=cv2.imread('crop.png',0)

        self.th3 = cv2.adaptiveThreshold(self.img0,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY_INV,501,45)

        cv2.imwrite('sam.png', self.th3)
        self.img1=cv2.imread('sam.png')
        self.img2 = wx.Image('sam.png', wx.BITMAP_TYPE_ANY)
        '''
        img0 -> cropped image
        img1 -> cropped saved as sam.png (cv2)
        img2 -> cropped loaded from sam.png (wx)
        '''
        
        # scale the image, preserving the aspect ratio
        W = self.img2.GetWidth()
        H = self.img2.GetHeight()
        if W > H:
            self.NewW = self.PhotoMaxSize
            self.NewH = self.PhotoMaxSize * H / W
        else:
            self.NewH = self.PhotoMaxSize
            self.NewW = self.PhotoMaxSize * W / H
        self.img2 = self.img2.Scale(self.NewW,self.NewH)
        #img2 scaled to 600 (600 being the larger dimension)

        self.m_bitmap21.SetBitmap(wx.BitmapFromImage(self.img2))
        self.m_panel1.Refresh()
        self.img3 = wx.EmptyImage(self.NewW,self.NewH)
        #img3 -> empty wx image with same scale of 600 (600 being the larger dimension)

    def onZoom(self,event):
        ZoomApp = ZoomFrame(self) # making an object of class ZoomFrame
        ZoomApp.Show()# calling the Show function from the wx toolkit for this frame

    def someListener(self,evt):
        
        X=evt.GetX()
        Y=evt.GetY()
        '''
        Event binding the left click on bitmap 21 where img2 is displayed
        in LeoSpyUI -> wx.EVT_LEFT_DOWN
        '''
        if (self.flag==0):
            self.onBrowse(evt)
        
        #Getting the value of the red channel on the clicked pixel
        mR=self.img2.GetRed(X,Y)

        self.blob=wx.EmptyImage(self.NewW,self.NewH)

        '''
        The following code tries to set a jump value: meaning the amound of
        darkness that an adjacent pixel increase based on the darkness of the current pixel
        which is clicked by the user, this value is assumed by taking the value
        of the red channel of the current clicked pixel. The higher the current 
        red value the smaller the the difference of the jump value. When there is 
        a greater fluctuation, ie., a greater difference in the red channel value 
        of the current pixel with the next pixel (the differnce more that what 
        is set by the below jump value), then we have reached the edge of the 
        whisker spot, owing to the end of the darkness of the spot and the light 
        colour of the fur. This is the method used to enf the loop that searches 
        for the extant of every clicked whisker.
        '''

        '''if (mR>=20 and mR<=40):
            mVmax=mR+10
            mVmin=mR/2'''
        if (mR>=41 and mR<=100):
            mVmax=mR+10
            mVmin=mR/2
            jump=15
        if (mR>=101 and mR<=130):
            mVmax=mR+5
            mVmin=mR/4
            jump=12
        if (mR>=131 and mR<=170):
            mVmax=mR+3
            mVmin=mR/6
            jump=10
        else:

            mVmax=mR+(mR/2)
            mVmin=mR/2
            jump=10
            
        c=1        
        i=1
        self.Xc=0#this stores the sum od all the x coordinates to later calculate the centroid of a single whisker spot
        self.Yc=0#this stores the sum od all the y coordinates to later calculate the centroid of a single whisker spot
        self.Wn=0# this stores the total number of pixels picked up to later calculate the centroid of a single whisker spot
        

        while (i <= c):

            
            
            
            if ((X+i)>(self.NewW-1) or (Y+i)>(self.NewH-1) or (X-i)<0 or (Y-i)<0):
                break
            
            s = 0
            
                
                
                
            j = i+1    
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break  
                
                mGa=self.img2.GetRed(X+j,Y+i)

                if (mGa>mVmin and mGa<mVmax):
                    if (abs(self.img2.GetRed(X+j,Y+i)-self.img2.GetRed(X+j-1,Y+i))<=jump):
                        self.img3.SetRGB(X+j,Y+i,255,255,255)
                        self.blob.SetRGB(X+j,Y+i,255,255,255)
                        self.Xc+=X+j
                        self.Yc+=Y+i
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break
            j = i+1
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break  

                mGf=self.img2.GetRed(X+j,Y-i)

                if (mGf>mVmin and mGf<mVmax):
                    if (abs(self.img2.GetRed(X+j,Y-i)-self.img2.GetRed(X+j-1,Y+i))<=jump):
                        self.img3.SetRGB(X+j,Y-i,255,255,255)
                        self.blob.SetRGB(X+j,Y-i,255,255,255)
                        self.Xc+=X+j
                        self.Yc+=Y-i
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break
            
            j = i+1    
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break  

                mGu=self.img2.GetRed(X-j,Y+i)

                if (mGu>mVmin and mGu<mVmax):
                    if (abs(self.img2.GetRed(X-j,Y+i)-self.img2.GetRed(X-j+1,Y+i))<=jump):
                        self.img3.SetRGB(X-j,Y+i,255,255,255)
                        self.blob.SetRGB(X-j,Y+i,255,255,255)
                        self.Xc+=X-j
                        self.Yc+=Y+i
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break


            j = i+1
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break  

                mGd=self.img2.GetRed(X-j,Y-i)

                if (mGd>mVmin and mGd<mVmax):
                    if (abs(self.img2.GetRed(X-j,Y-i)-self.img2.GetRed(X-j+1,Y+i))<=jump):
                        self.img3.SetRGB(X-j,Y-i,255,255,255)
                        self.blob.SetRGB(X-j,Y-i,255,255,255)
                        self.Xc+=X-j
                        self.Yc+=Y-i
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break
            

            j = i+1
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break

                mRa=self.img2.GetRed(X+i,Y+j)
                            
          
                if (mRa>mVmin and mRa<mVmax):
                    if (abs(self.img2.GetRed(X+i,Y+j)-self.img2.GetRed(X+i,Y+j-1))<=jump):
                        self.img3.SetRGB(X+i,Y+j,255,255,255)
                        self.blob.SetRGB(X+i,Y+j,255,255,255)
                        self.Xc+=X+i
                        self.Yc+=Y+j
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break
            

            j = i+1
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break

                mRf=self.img2.GetRed(X+i,Y-j)

                if (mRf>mVmin and mRf<mVmax):
                    if (abs(self.img2.GetRed(X+i,Y-j)-self.img2.GetRed(X+i,Y-j+1))<=jump):
                        self.img3.SetRGB(X+i,Y-j,255,255,255)
                        self.blob.SetRGB(X+i,Y-j,255,255,255)
                        self.Xc+=X+i
                        self.Yc+=Y-j
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break


            j = i+1
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break

                mRu=self.img2.GetRed(X-i,Y+j)

                if (mRu>mVmin and mRu<mVmax):
                    if (abs(self.img2.GetRed(X-i,Y+j)-self.img2.GetRed(X-i,Y+j-1))<=jump):
                        self.img3.SetRGB(X-i,Y+j,255,255,255)
                        self.blob.SetRGB(X-i,Y+j,255,255,255)
                        self.Xc+=X-i
                        self.Yc+=Y+j
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break


            j = i+1
            while (j >= i+1):
                
                
                if ((X+j)>(self.NewW-1) or (Y+j)>(self.NewH-1) or (X-j)<0 or (Y-j)<0):
                    break

                mRd=self.img2.GetRed(X-i,Y-j)

                if (mRd>mVmin and mRd<mVmax):
                    if (abs(self.img2.GetRed(X-i,Y-j)-self.img2.GetRed(X-i,Y-j+1))<=jump):
                        self.img3.SetRGB(X-i,Y-j,255,255,255)
                        self.blob.SetRGB(X-i,Y-j,255,255,255)
                        self.Xc+=X-i
                        self.Yc+=Y-j
                        self.Wn+=1
                    else:
                        break
                    j = j+1
                else:
                    break

                
            

            mGx=self.img2.GetRed(X+i,Y+i)
            mGy=self.img2.GetRed(X-i,Y-i)
            mGs=self.img2.GetRed(X+i,Y-i)
            mGt=self.img2.GetRed(X-i,Y+i)

            mRx=self.img2.GetRed(X,Y+i)
            mRy=self.img2.GetRed(X,Y-i)
            mRs=self.img2.GetRed(X+i,Y)
            mRt=self.img2.GetRed(X-i,Y)


            if (mGx>mVmin and mGx<mVmax):
                if (abs(self.img2.GetRed(X+i,Y+i)-self.img2.GetRed(X+i-1,Y+i-1))<=jump):
                    self.img3.SetRGB(X+i,Y+i,255,255,255)
                    self.blob.SetRGB(X+i,Y+i,255,255,255)
                    s = s+1
                    self.Xc+=X+i
                    self.Yc+=Y+i
                    self.Wn+=1

            if (mGy>mVmin and mGy<mVmax):
                if (abs(self.img2.GetRed(X-i,Y-i)-self.img2.GetRed(X-i+1,Y-i+1))<=jump):
                    self.img3.SetRGB(X-i,Y-i,255,255,255)
                    self.blob.SetRGB(X-i,Y-i,255,255,255)
                    s = s+1
                    self.Xc+=X-i
                    self.Yc+=Y-i
                    self.Wn+=1
                
            if (mGs>mVmin and mGs<mVmax):
                if (abs(self.img2.GetRed(X+i,Y-i)-self.img2.GetRed(X+i-1,Y-i+1))<=jump):
                    self.img3.SetRGB(X+i,Y-i,255,255,255)
                    self.blob.SetRGB(X+i,Y-i,255,255,255)
                    s = s+1
                    self.Xc+=X+i
                    self.Yc+=Y-i
                    self.Wn+=1

            if (mGt>mVmin and mGt<mVmax):
                if (abs(self.img2.GetRed(X-i,Y+i)-self.img2.GetRed(X-i+1,Y+i-1))<=jump):
                    self.img3.SetRGB(X-i,Y+i,255,255,255)
                    self.blob.SetRGB(X-i,Y+i,255,255,255)
                    s = s+1
                    self.Xc+=X-i
                    self.Yc+=Y+i
                    self.Wn+=1
                
            if (mRx>mVmin and mRx<mVmax):
                if (abs(self.img2.GetRed(X,Y+i)-self.img2.GetRed(X,Y+i-1))<=jump):
                    self.img3.SetRGB(X,Y+i,255,255,255)
                    self.blob.SetRGB(X,Y+i,255,255,255)
                    s = s+1
                    self.Xc+=X
                    self.Yc+=Y+i
                    self.Wn+=1

            if (mRy>mVmin and mRy<mVmax):
                if (abs(self.img2.GetRed(X,Y-i)-self.img2.GetRed(X,Y-i+1))<=jump):
                    self.img3.SetRGB(X,Y-i,255,255,255)
                    self.blob.SetRGB(X,Y-i,255,255,255)
                    s = s+1
                    self.Xc+=X
                    self.Yc+=Y-i
                    self.Wn+=1
                
            if (mRs>mVmin and mRs<mVmax):
                if (abs(self.img2.GetRed(X+i,Y)-self.img2.GetRed(X+i-1,Y))<=jump):
                    self.img3.SetRGB(X+i,Y,255,255,255)
                    self.blob.SetRGB(X+i,Y,255,255,255)
                    s = s+1
                    self.Xc+=X+i
                    self.Yc+=Y
                    self.Wn+=1

            if (mRt>mVmin and mRt<mVmax):
                if (abs(self.img2.GetRed(X-i,Y)-self.img2.GetRed(X-i+1,Y))<=jump):
                    self.img3.SetRGB(X-i,Y,255,255,255)
                    self.blob.SetRGB(X-i,Y,255,255,255)
                    s = s+1
                    self.Xc+=X-i
                    self.Yc+=Y
                    self.Wn+=1


            i = i+1#incrementer for the main while loop
            if s>=3 :
                c = c+1# if there are more than 3 pixels marked in a single run, continue searching
        
        self.centroid()
        '''
        calling the cenrtoid function to compute the centroud 
        of a single whisker spot, after finding all its contributing pixels
        '''


        # scale the image, preserving the aspect ratio
        W = self.img3.GetWidth()
        H = self.img3.GetHeight()
        if W > H:
            NewW = 200
            NewH = 200 * H / W
        else:
            NewH = 200
            NewW = 200 * W / H
        self.img4 = self.img3
        self.img4 = self.img4.Scale(NewW,NewH)

        #the image to have a small preview in the UI
 
        self.m_bitmap2.SetBitmap(wx.BitmapFromImage(self.img4))
        self.m_panel1.Refresh()
        img_1= self.img4.SaveFile('output3am.png', wx.BITMAP_TYPE_PNG)
    
        
    def centroid(self):
        
        '''img_5= self.blob.SaveFile('blob.png', wx.BITMAP_TYPE_PNG)
        im = cv2.imread('blob.png')
        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        
        try:
        
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cnt = contours[-1]
            cv2.drawContours(im, contours, -1, (0,0,255),2)
            cnt = contours[0]
            M = cv2.moments(cnt) 
            print M 

        
            cx = int(M['m10']/M['m00']) 
            cy = int(M['m01']/M['m00'])'''

        cx = self.Xc/self.Wn
        cy = self.Yc/self.Wn
        self.cList2 = []
        self.cList2.append((cx,cy))#this maintains the list of centroids until all the whiskers are clicked
        self.cList.extend(self.cList2)
        #print "Updated List : ", self.cList
        self.Log("Centroid is : %d , %d  " % (cx, cy))
        return (cx,cy)

        '''area = cv2.contourArea(cnt)
        #print ("Area :%s" %(area))
        img_1=cv2.imwrite('brandnew1.jpg',im)'''
           

        '''except ZeroDivisionError:
            print "please try again"'''

        
    def save_cal(self, event):
        '''
        creating a csv file saving the ratio list of
        all possible ratios of all distances
        between the centroids.
        '''
        self.profile = 'no_profile'
        if (self.m_radioBtn2.GetValue() == True):
            self.profile='_right_profile'
        if (self.m_radioBtn4.GetValue() == True):
            self.profile='_left_profile'    
        with open('Csvs/' + self.m_textCtrl3.Value + self.profile + '.csv', 'w') as csvfile:
            '''
            file naming scheme of lion name and the specified profile is taken 
            into account for the generated csv file
            '''
            mywriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(self.disratiolist)-1):
                mywriter.writerow([self.disratiolist[i]])
        
        '''with open('Lion1.csv', 'rb') as csvfile:
            myreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in myreader:
                print ', '.join(row)'''
    
    def compare(self, event):
        '''
        comparing all the files within the csv folder, flie by file
        and row by row, searching for similarity between the ratios in the 
        file and the current ratio list of the current image (generated
        after the calculate ratios button is clicked) The score value is 
        increased by 1 if even one ratio matches within 1 unit of 
        coordinate distance ratio.
        '''
        files = os.listdir('Csvs')
        score=0
        for f in files:
            with open('Csvs/' + f, 'rb') as csvfile:
                myreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in myreader:
                    i=0
                    if(abs(self.disratiolist[i]-float(row[0]))<=1):
                        score+=1
                    else:
                        score-=1
                    i+=1
            self.Log( ' For  '+f+':')
            if (score>100):

                self.Log( 'This is a match')
                self.Log( 'score: %d \n' % score  )
            elif (score >50 and score <100  ):

                self.Log( 'This is a less probability of a match')
                self.Log( 'score: %d \n'% score)
            else :
                self.Log( 'This is no match')
                self.Log( 'score: %d \n'% score)
    def calculate(self, event):
        '''
        calculating the distance between all the centroids and then generating
        a ratio list of all the distances calculated
        '''
        self.dislist = []
        for i in range(len(self.cList)-1):
            for j in range(i,len(self.cList)-1):
                dis= math.sqrt(((self.cList[i][0]-self.cList[j+1][0])**2)+((self.cList[i][1]-self.cList[j+1][1])**2))
                self.dislist.append(dis)
        gen1 = (str(w) for w in self.dislist)
        self.Log('Distances are:')
        self.Log(','.join(gen1))
        self.disratiolist = []
        for a in range(len(self.dislist)-1):
            for b in range(a,len(self.dislist)-1):
                ratio = round(self.dislist[a]/self.dislist[b+1],3)
                self.disratiolist.append(ratio)
        gen2 = (str(w) for w in self.disratiolist)
        self.Log('Distance ratios are:')
        self.Log(','.join(gen2))
        

       

class ZoomFrame(lsu.MyFrame2):
    
    def __init__(self, parent):

        lsu.MyFrame2.__init__(self,parent)
        icon = wx.Icon('logo.png', wx.BITMAP_TYPE_ANY)
        self.SetIcon(icon)
        self.box = wx.BoxSizer( wx.VERTICAL )
        self.m_panel3.SetSizer( self.box )
        self.m_panel3.Layout()
        self.box.Fit( self.m_panel3 )
        NC = NavCanvas.NavCanvas(self.m_panel3)
        '''
        NavCanvas adds the navigation toolbar to zoom and pan around in the image
        '''
        self.Canvas = NC.Canvas
        self.box.Add( NC, 4, wx.EXPAND )
        self.Canvas.AddScaledBitmap(wx.Bitmap(parent.img),(0,0),800,Position = "cc")
        self.Canvas.Draw() 
        self.parent = parent

    def OnSavePNG(self,event=None):
       '''import os
       dlg = wx.FileDialog(
       self, message="Save file as ...", defaultDir=os.getcwd(), 
       defaultFile="", wildcard="*.png", style=wx.SAVE)
       if dlg.ShowModal() == wx.ID_OK:
           path = dlg.GetPath()
           if not(path[-4:].lower() == ".png"):
               path = path+".png" '''
       self.Canvas.SaveAsImage("crop.png")
       self.parent.onView()
       self.Close()
		
if __name__ == "__main__":
    app = wx.App()
    MainApp = MainWindow(None)
    MainApp.Show()
    app.MainLoop()