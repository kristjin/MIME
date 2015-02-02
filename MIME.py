"""Multiple Installation Management Engine"""

import wx
import UI


class App(wx.App):

    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def OnExit(self):
        print 'App Exited'


class MainFrame(wx.Frame):

    def __init__(self, parent=None,id=-1, pos=wx.DefaultPosition, style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP):

        size = (800, 600)

        wx.Frame.__init__(self, parent, id, 'Multiple Installation Management Engine', pos, size, style)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        # =>CREATE MENU BAR<= #
        self.menuData = \
                (("&Settings",
                    ("&Games", "Games Settings", self.OnGames),
                    ("&Filters", "Filter Settings", self.OnFilters),
                    ("&Profiles", "Profile Settings", self.OnProfiles),
                    ("", "", ""),
                    ("&Quit", "Quit", self.OnCloseWindow)),
                ("&Help",
                    ("&About", "About MIME", self.OnAbout)))
        self.create_menu_bar()

        # =>CREATE PANELS<= #
        self.panelList = []
        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        self.PanelMain = self.add_panel(UI.main, sizer_h)
        self.PanelGames = self.add_panel(UI.games, sizer_h)
        self.PanelFilters = self.add_panel(UI.filters, sizer_h)
        self.PanelProfiles = self.add_panel(UI.profiles, sizer_h)
        self.PanelAbout = self.add_panel(UI.about, sizer_h)
        self.SetSizer(sizer_h)
        self.Center()
        self.PanelMain.show_yourself()

    def hide_panels(self):
        # hides each panel in self.panelList()
        for eachPanel in self.panelList:
            eachPanel.Hide()

    def add_panel(self, ui, sizer):
        # panel constructor, called in MainFrame.__init__
        panel = ui(self)
        self.panelList.append(panel)
        sizer.Add(panel, 1, wx.EXPAND)
        return panel

    def create_menu_bar(self):
        bar = wx.MenuBar()
        for eachMenuData in self.menuData:
            label = eachMenuData[0]
            items = eachMenuData[1:]
            bar.Append(self.create_menu(items), label)
        self.SetMenuBar(bar)

    def create_menu(self, data):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in data:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            item = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, item)
        return menu

    def OnCloseWindow(self, event):
        # what to do when top level is closed
        self.Destroy()

    def OnGames(self, event):
        self.hide_panels()
        self.PanelGames.show_yourself()

    def OnFilters(self, event):
        self.hide_panels()
        self.PanelFilters.show_yourself()

    def OnProfiles(self, event):
        self.hide_panels()
        self.PanelProfiles.show_yourself()

    def OnAbout(self, event):
        self.hide_panels()
        self.PanelAbout.show_yourself()

def main():
    app = App(redirect = False)
    app.MainLoop()


if __name__ == '__main__':
    main()