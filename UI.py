"""MIME UI Panels"""

import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

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

        mainbox = wx.BoxSizer(wx.VERTICAL)

        titlebox = wx.BoxSizer(wx.HORIZONTAL)

        gametitle = "Skyrim Management Pane"
        title = wx.StaticText(self, wx.ID_ANY, label=gametitle, style=wx.ALIGN_LEFT)
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        title.SetFont(font)
        titlebox.Add(title, 1, wx.LEFT | wx.ALIGN_LEFT,5)

        titlebox.AddStretchSpacer()

        gamelist = ["Skyrim", "Add..."]
        changegame = wx.ComboBox(self, wx.ID_ANY, "Change...", wx.DefaultPosition, (120, 50),
                    gamelist, wx.CB_DROPDOWN)
        titlebox.Add(changegame, 0, wx.RIGHT, 5)

        advicebox = wx.BoxSizer(wx.HORIZONTAL)

        gameadvice = "This is where a user defined description of the profile would go."
        advice = wx.StaticText(self, wx.ID_ANY, label=gameadvice, style=wx.ALIGN_LEFT)
        font = wx.Font(12, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        advice.SetFont(font)
        advicebox.Add(advice, 1, wx.LEFT | wx.ALIGN_LEFT,5)

        # panelbox = wx.BoxSizer(wx.HORIZONTAL)

        mainbox.Add(titlebox, 0, wx.TOP)
        mainbox.Add(advicebox, 0)

        self.SetSizer(mainbox)

        # self.finish()



class games(Panel):

    def __init__(self, parent, id=wx.ID_ANY):

        wx.Panel.__init__(self, parent, id)

        mainbox = wx.BoxSizer(wx.HORIZONTAL)

        vbox = wx.BoxSizer(wx.VERTICAL)

        leftPanel = wx.Panel(self, id=wx.ID_ANY)
        rightPanel = wx.Panel(self, id=wx.ID_ANY)

        self.list = CheckListCtrl(rightPanel)
        self.list.InsertColumn(0, 'File Name', width=140)
        self.list.InsertColumn(1, 'Date')
        self.list.InsertColumn(2, '')

        vbox2 = wx.BoxSizer(wx.VERTICAL)

        sel = wx.Button(leftPanel, -1, 'Select All', size=(100, -1))
        des = wx.Button(leftPanel, -1, 'Deselect All', size=(100, -1))
        apply = wx.Button(leftPanel, -1, 'Apply', size=(100, -1))

        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id=sel.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDeselectAll, id=des.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnApply, id=apply.GetId())

        vbox2.Add(sel, 0, wx.TOP, 5)
        vbox2.Add(des)
        vbox2.Add(apply)

        leftPanel.SetSizer(vbox2)

        vbox.Add(self.list, 1, wx.EXPAND | wx.TOP, 3)
        vbox.Add((-1, 10))

        rightPanel.SetSizer(vbox)

        mainbox.Add(leftPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        mainbox.Add(rightPanel, 1, wx.EXPAND)
        mainbox.Add((3, -1))

        self.SetSizer(mainbox)

        self.finish()

    def OnSelectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i)

    def OnDeselectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i, False)

    def OnApply(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            if i == 0: self.log.Clear()
            if self.list.IsChecked(i):
                self.log.AppendText(self.list.GetItemText(i) + '\n')



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
