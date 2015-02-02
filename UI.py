"""MIME UI Panels"""

import wx

class Panel(wx.Panel):

    def show_yourself(self):
        self.Raise()
        self.Fit()
        self.GetParent().GetSizer().Show(self)
        self.GetParent().GetSizer().Layout()

    def finish(self):
        self.Raise()
        self.SetPosition((0,0))
        self.Fit()
        self.Hide()

class main(Panel):

    def __init__(self, parent, id=wx.ID_ANY):

        wx.Panel.__init__(self, parent, id)

        heading1 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        # master sizer for the whole panel
        sizer_v = wx.BoxSizer(wx.VERTICAL)
        sizer_v.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Multiple Installation Management Engine', (0, 0))
        txtHeader.SetFont(heading1)

        sizer_topRow = wx.BoxSizer(wx.HORIZONTAL)
        sizer_topRow.Add(txtHeader, 3, wx.ALIGN_LEFT)
        sizer_topRow.Add((0,0), 1)

        sizer_v.Add(sizer_topRow, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my ddl titles should go.\n\n'
        text = text + 'This is where my dropdowns should go..\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        sizer_v.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        sizer_v.AddSpacer(15)
        self.SetSizer(sizer_v)
        self.finish()


class games(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        sizer_v = wx.BoxSizer(wx.VERTICAL)
        sizer_v.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Games Settings', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        sizer_topRow = wx.BoxSizer(wx.HORIZONTAL)
        sizer_topRow.Add(txtHeader, 3, wx.ALIGN_LEFT)
        sizer_topRow.Add((0,0), 1)

        sizer_v.Add(sizer_topRow, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the games settings options
        text = 'This is where my settings for games will go.\n\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        sizer_v.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the save button, etc

        sizer_v.AddSpacer(15)
        self.SetSizer(sizer_v)
        self.finish()



class filters(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        sizer_v = wx.BoxSizer(wx.VERTICAL)
        sizer_v.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Filter Settings', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        sizer_topRow = wx.BoxSizer(wx.HORIZONTAL)
        sizer_topRow.Add(txtHeader, 3, wx.ALIGN_LEFT)
        sizer_topRow.Add((0,0), 1)

        sizer_v.Add(sizer_topRow, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my filter settings should go.\n\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        sizer_v.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        sizer_v.AddSpacer(15)
        self.SetSizer(sizer_v)

        self.finish()

class profiles(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        sizer_v = wx.BoxSizer(wx.VERTICAL)
        sizer_v.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'Profile Settings', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        sizer_topRow = wx.BoxSizer(wx.HORIZONTAL)
        sizer_topRow.Add(txtHeader, 3, wx.ALIGN_LEFT)
        sizer_topRow.Add((0,0), 1)

        sizer_v.Add(sizer_topRow, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my profile settings should go.\n\n'

        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        sizer_v.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)


        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        sizer_v.AddSpacer(15)
        self.SetSizer(sizer_v)

        self.finish()


class about(Panel):

    def __init__(self, parent, id=-1):

        wx.Panel.__init__(self, parent, id)

        # master sizer for the whole panel
        sizer_v = wx.BoxSizer(wx.VERTICAL)
        sizer_v.AddSpacer(15)

        # build the top row
        txtHeader = wx.StaticText(self, -1, 'About Multiple Installation Management Engine', (0, 0))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        txtHeader.SetFont(font)

        sizer_topRow = wx.BoxSizer(wx.HORIZONTAL)
        sizer_topRow.Add(txtHeader, 3, wx.ALIGN_LEFT)
        sizer_topRow.Add((0,0), 1)

        sizer_v.Add(sizer_topRow, 0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the drop downs, swap buttons
        text = 'This is where my about info should go.\n\n'
        txtBasic = wx.StaticText(self, -1, text)
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        txtBasic.SetFont(font)
        sizer_v.Add(txtBasic, 1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)

        # build the file lists, descriptors, and show filtered files checkbox

        # finish master sizer
        sizer_v.AddSpacer(15)
        self.SetSizer(sizer_v)

        self.finish()
