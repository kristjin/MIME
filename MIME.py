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

    def __init__(self, parent=None,id=-1, pos=wx.DefaultPosition, style=wx.CAPTION | wx.STAY_ON_TOP):

        size = (800, 600)
        wx.Frame.__init__(self, parent, id, 'Multiple Installation Management Engine', pos, size, style)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.createMenuBar()

        sizer_h = wx.BoxSizer(wx.HORIZONTAL)

        self.PanelMain = UI_main(self)
        sizer_h.Add(self.PanelMain, 1, wx.EXPAND)

        self.PanelGames = UI_games(self)
        sizer_h.Add(self.PanelGames, 1, wx.EXPAND)

        self.PanelFilters = UI_filters(self)
        sizer_h.Add(self.PanelFilters, 1, wx.EXPAND)

        self.PanelProfiles = UI_profiles(self)
        sizer_h.Add(self.PanelProfiles, 1, wx.EXPAND)

        self.PanelAbout = UI_about(self)
        sizer_h.Add(self.PanelAbout, 1, wx.EXPAND)

        self.SetSizer(sizer_h)

        self.PanelMain.ShowYourself()


    def menuData(self):
        return (("&Settings",
                    ("&Games", "Games Settings", self.OnGames),
                    ("&Filters", "Filter Settings", self.OnFilters),
                    ("&Profiles", "Profile Settings", self.OnProfiles),
                    ("", "", ""),
                    ("&Quit", "Quit", self.OnCloseWindow)),
                ("&Help",
                    ("&About", "About MIME", self.OnAbout)))
    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
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

    def OnCloseWindow(self, event):
        self.Destroy()

    # Just grouping the empty event handlers together
    def OnGames(self, event): pass
    def OnFilters(self, event): pass
    def OnProfiles(self, event): pass
    def OnAbout(self, event): pass



class UI_main(wx.Panel):

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

        self.Raise()
        self.SetPosition((0,0))
        self.Fit()
        self.Hide()


    def ShowYourself(self):
        self.Raise()
        self.GetParent().Center()
        self.Fit()
        self.GetParent().GetSizer().Show(self)
        self.GetParent().GetSizer().Layout()

class UI_games(wx.Panel):

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

        # finish master sizer
        mastersizer.AddSpacer(15)
        self.SetSizer(mastersizer)

        self.Raise()
        self.SetPosition((0,0))
        self.Fit()
        self.Hide()


    def ShowYourself(self):
        self.Raise()
        self.GetParent().Center()
        self.Fit()
        self.GetParent().GetSizer().Show(self)
        self.GetParent().GetSizer().Layout()

class UI_filters(wx.Panel):

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

        self.Raise()
        self.SetPosition((0,0))
        self.Fit()
        self.Hide()


    def ShowYourself(self):
        self.Raise()
        self.GetParent().Center()
        self.Fit()
        self.GetParent().GetSizer().Show(self)
        self.GetParent().GetSizer().Layout()

class UI_profiles(wx.Panel):

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

        self.Raise()
        self.SetPosition((0,0))
        self.Fit()
        self.Hide()


    def ShowYourself(self):
        self.Raise()
        self.GetParent().Center()
        self.Fit()
        self.GetParent().GetSizer().Show(self)
        self.GetParent().GetSizer().Layout()

class UI_about(wx.Panel):

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

        self.Raise()
        self.SetPosition((0,0))
        self.Fit()
        self.Hide()


    def ShowYourself(self):
        self.Raise()
        self.GetParent().Center()
        self.Fit()
        self.GetParent().GetSizer().Show(self)
        self.GetParent().GetSizer().Layout()







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
