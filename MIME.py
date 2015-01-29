"""Multiple Installation Management Engine"""

import wx


class My_App(wx.App):

    def OnInit(self):
        self.frame = My_Frame(None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def OnExit(self):
        print 'App Object Dying ...'


class My_Frame(wx.Frame):

    def __init__(self, parent=None,id=-1, pos=wx.DefaultPosition, style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP):

        size = (800, 600)

        wx.Frame.__init__(self, parent, id, 'Multiple Installation Management Engine', pos, size, style)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        #=>CREATE MENU BAR<=#
        self.menuData = \
                (("&Settings",
                    ("&Games", "Games Settings", self.OnGames),
                    ("&Filters", "Filter Settings", self.OnFilters),
                    ("&Profiles", "Profile Settings", self.OnProfiles),
                    ("", "", ""),
                    ("&Quit", "Quit", self.OnCloseWindow)),
                ("&Help",
                    ("&About", "About MIME", self.OnAbout)))
        self.createMenuBar()

        #=>CREATE PANELS<=#
        self.panelList = []
        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        self.PanelMain = self.addPanel(UI_main, sizer_h)
        self.PanelGames = self.addPanel(UI_games, sizer_h)
        self.PanelFilters = self.addPanel(UI_filters, sizer_h)
        self.PanelProfiles = self.addPanel(UI_profiles, sizer_h)
        self.PanelAbout = self.addPanel(UI_about, sizer_h)
        self.SetSizer(sizer_h)
        self.Center()
        self.PanelMain.ShowYourself()


    def hidePanels(self):
        #hides each panel in self.panelList()
        for eachPanel in self.panelList:
            eachPanel.Hide()

    def OnCloseWindow(self, event):
        #what to do when top level is closed
        self.Destroy()

    def addPanel(self, uiClass, sizer):
        #panel constructor, called in My_Frame.__init__
        panel = uiClass(self)
        self.panelList.append(panel)
        sizer.Add(panel, 1, wx.EXPAND)
        return panel

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData:
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu

    def OnGames(self, event):
        self.hidePanels()
        self.PanelGames.ShowYourself()

    def OnFilters(self, event):
        self.hidePanels()
        self.PanelFilters.ShowYourself()

    def OnProfiles(self, event):
        self.hidePanels()
        self.PanelProfiles.ShowYourself()

    def OnAbout(self, event):
        self.hidePanels()
        self.PanelAbout.ShowYourself()

class Panel(wx.Panel):
    def ShowYourself(self):
        self.Raise()
        self.Fit()
        self.GetParent().GetSizer().Show(self)
        self.GetParent().GetSizer().Layout()

    def finish(self):
        self.Raise()
        self.SetPosition((0,0))
        self.Fit()
        self.Hide()

class UI_main(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        mastersizer = wx.BoxSizer(wx.VERTICAL)
        mastersizer.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Change Active Profile', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        rowtopsizer = wx.BoxSizer(wx.HORIZONTAL)
        rowtopsizer.Add(txtHeader, 3, wx.ALIGN_LEFT)
        rowtopsizer.Add((0,0), 1)

        mastersizer.Add(rowtopsizer, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my ddl titles should go.\n\n'
        text = text + 'This is where my dropdowns should go..\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        mastersizer.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        mastersizer.AddSpacer(15)
        self.SetSizer(mastersizer)
        self.finish()


class UI_games(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        mastersizer = wx.BoxSizer(wx.VERTICAL)
        mastersizer.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Games Settings', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        rowtopsizer = wx.BoxSizer(wx.HORIZONTAL)
        rowtopsizer.Add(txtHeader, 3, wx.ALIGN_LEFT)
        rowtopsizer.Add((0,0), 1)

        mastersizer.Add(rowtopsizer, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the games settings options
        text = 'This is where my settings for games will go.\n\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        mastersizer.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the save button, etc

        mastersizer.AddSpacer(15)
        self.SetSizer(mastersizer)
        self.finish()



class UI_filters(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        mastersizer = wx.BoxSizer(wx.VERTICAL)
        mastersizer.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Filter Settings', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        rowtopsizer = wx.BoxSizer(wx.HORIZONTAL)
        rowtopsizer.Add(txtHeader, 3, wx.ALIGN_LEFT)
        rowtopsizer.Add((0,0), 1)

        mastersizer.Add(rowtopsizer, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my filter settings should go.\n\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        mastersizer.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        mastersizer.AddSpacer(15)
        self.SetSizer(mastersizer)

        self.finish()

class UI_profiles(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        mastersizer = wx.BoxSizer(wx.VERTICAL)
        mastersizer.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Profile Settings', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        rowtopsizer = wx.BoxSizer(wx.HORIZONTAL)
        rowtopsizer.Add(txtHeader, 3, wx.ALIGN_LEFT)
        rowtopsizer.Add((0,0), 1)

        mastersizer.Add(rowtopsizer, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my profile settings should go.\n\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        mastersizer.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        mastersizer.AddSpacer(15)
        self.SetSizer(mastersizer)

        self.finish()


class UI_about(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        mastersizer = wx.BoxSizer(wx.VERTICAL)
        mastersizer.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'About Multiple Installation Management Engine', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        rowtopsizer = wx.BoxSizer(wx.HORIZONTAL)
        rowtopsizer.Add(txtHeader, 3, wx.ALIGN_LEFT)
        rowtopsizer.Add((0,0), 1)

        mastersizer.Add(rowtopsizer, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my about info should go.\n\n'
        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        mastersizer.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        mastersizer.AddSpacer(15)
        self.SetSizer(mastersizer)

        self.finish()


def main():
    app = My_App(redirect = False)
    app.MainLoop()


if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------

# class UI_Main(wx.Panel):
#
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'Multiple Installation Management Engine')
#         panel = wx.Panel(self, -1)
#         panel.SetBackgroundColour("White")
#
#         # master sizer for the whole panel
#         mastersizer = wx.BoxSizer(wx.VERTICAL)
#         mastersizer.AddSpacer(15)
#
#
#
#     def buttonData(self):
#         return (("First", self.OnFirst),
#                 ("<< PREV", self.OnPrev),
#                 ("NEXT >>", self.OnNext),
#                 ("Last", self.OnLast))
#
#     def createButtonBar(self, panel, yPos = 0):
#         xPos = 0
#         for eachLabel, eachHandler in self.buttonData():
#             pos = (xPos, yPos)
#             button = self.buildOneButton(panel, eachLabel, eachHandler, pos)
#             xPos += button.GetSize().width
#
#     def buildOneButton(self, parent, label, handler, pos=(0,0)):
#         button = wx.Button(parent, -1, label, pos)
#         self.Bind(wx.EVT_BUTTON, handler, button)
#         return button
#
#     def textFieldData(self):
#         return (("First Name", (10, 50)),
#                 ("Last Name", (10, 80)))
#
#     def createTextFields(self, panel):
#         for eachLabel, eachPos in self.textFieldData():
#             self.createCaptionedText(panel, eachLabel, eachPos)
#
#     def createCaptionedText(self, panel, label, pos):
#         static = wx.StaticText(panel, wx.NewId(), label, pos)
#         static.SetBackgroundColour("White")
#         textPos = (pos[0] + 75, pos[1])
#         wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1), pos=textPos)
#

#     def OnFirst(self, event): pass
#     def OnLast(self, event): pass
#     def OnNext(self, event): pass
#     def OnPrev(self, event): pass

#
# if __name__ == '__main__':
#     app = wx.App()
#     frame = MIMEGUI(parent=None, id=-1)
#     frame.Show()
#     app.MainLoop()
