from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock

# ============================================================
# PARAKH — SMART REAL-TIME NGO MONITORING & INSPECTION SYSTEM
# Elevated demo/prototype version
# ============================================================

Window.size = (1280, 780)
Window.clearcolor = (0.95, 0.95, 0.93, 1)

NAVY = (0.035, 0.065, 0.10, 1)
NAVY2 = (0.075, 0.11, 0.16, 1)
WHITE = (1, 1, 1, 1)
CREAM = (0.965, 0.955, 0.925, 1)
CREAM2 = (0.91, 0.90, 0.87, 1)
BLACK = (0.055, 0.065, 0.075, 1)
GREY = (0.39, 0.41, 0.43, 1)
LIGHT_GREY = (0.72, 0.74, 0.75, 1)
BLUE = (0.08, 0.34, 0.63, 1)
CYAN = (0.05, 0.52, 0.65, 1)
GREEN = (0.12, 0.52, 0.32, 1)
RED = (0.72, 0.18, 0.19, 1)
ORANGE = (0.78, 0.46, 0.12, 1)
PURPLE = (0.37, 0.27, 0.60, 1)

NGOS = [
    {"name":"ABC Foundation", "location":"New Delhi", "status":"COMPLIANT",
     "last":"08 Sept 2026", "risk":"LOW", "score":"92 / 100"},
    {"name":"XYZ Welfare Society", "location":"Ghaziabad", "status":"ACTION REQUIRED",
     "last":"02 Sept 2026", "risk":"HIGH", "score":"41 / 100"},
    {"name":"Udaan Welfare Society", "location":"Gurugram", "status":"PENDING",
     "last":"05 Sept 2026", "risk":"MEDIUM", "score":"68 / 100"},
    {"name":"Sahyog Child Care", "location":"Noida", "status":"INSPECTION DUE",
     "last":"29 Aug 2026", "risk":"HIGH", "score":"48 / 100"},
    {"name":"Nayi Disha Trust", "location":"Faridabad", "status":"COMPLIANT",
     "last":"07 Sept 2026", "risk":"LOW", "score":"88 / 100"},
]

class Card(BoxLayout):
    def __init__(self, bg=WHITE, radius=14, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*bg)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size,
                                       radius=[dp(radius)])
        self.bind(pos=self._sync, size=self._sync)
    def _sync(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

class MenuButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0,0,0,0)
        self.color = (0.88,0.91,0.93,1)
        self.font_size = dp(12)
        self.bold = True
        self.halign = "left"
        self.valign = "middle"
        self.padding = [dp(15),0]

class ActionButton(Button):
    def __init__(self, bg=BLUE, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_down = ""
        self.background_color = bg
        self.color = WHITE
        self.bold = True
        self.font_size = dp(10)
        self.radius = [dp(8)]

class ParakhApp(App):
    def build(self):
        self.root = BoxLayout(orientation="horizontal")
        self.create_sidebar()
        self.main_area = BoxLayout(orientation="vertical")
        self.root.add_widget(self.sidebar)
        self.root.add_widget(self.main_area)
        self.show_overview()
        return self.root

    def create_sidebar(self):
        self.sidebar = BoxLayout(
            orientation="vertical", size_hint_x=None, width=dp(255),
            padding=[dp(16),dp(18),dp(14),dp(16)], spacing=dp(2))
        with self.sidebar.canvas.before:
            Color(*NAVY)
            self.sidebar_bg = Rectangle(pos=self.sidebar.pos, size=self.sidebar.size)
        self.sidebar.bind(pos=lambda o,v:setattr(self.sidebar_bg,"pos",v),
                          size=lambda o,v:setattr(self.sidebar_bg,"size",v))

        brand = BoxLayout(orientation="horizontal", size_hint_y=None,
                          height=dp(72), spacing=dp(9))
        brand.add_widget(Label(text="◈", font_size=dp(31), bold=True,
                               color=WHITE, size_hint_x=None, width=dp(42)))
        words = BoxLayout(orientation="vertical")
        words.add_widget(Label(text="PARAKH", font_size=dp(22), bold=True,
                               color=WHITE, halign="left"))
        words.add_widget(Label(text="SMART NGO MONITORING", font_size=dp(8),
                               bold=True, color=(.60,.66,.70,1), halign="left"))
        brand.add_widget(words)
        self.sidebar.add_widget(brand)

        self.sidebar.add_widget(Label(text="CONTROL ROOM", font_size=dp(9),
            bold=True, color=(.48,.56,.60,1), size_hint_y=None,
            height=dp(34), halign="left"))

        menu = [
            ("●   National Dashboard", self.show_overview),
            ("▣   NGO Registry", self.show_registry),
            ("◉   Inspections", self.show_inspections),
            ("⌖   GIS / Risk Map", self.show_gis),
            ("✓   Attendance", self.show_attendance),
            ("✣   AI Risk Insights", self.show_ai),
            ("▣   Live CCTV", self.show_cctv),
            ("♧   Complaints", self.show_complaints),
            ("⚠   Alert Center", self.show_alerts),
            ("▤   Reports", self.show_reports),
        ]
        for text, func in menu:
            b = MenuButton(text=text, size_hint_y=None, height=dp(42))
            b.bind(on_release=lambda x,f=func:f())
            self.sidebar.add_widget(b)

        self.sidebar.add_widget(Widget())
        self.sidebar.add_widget(Label(
            text="●  SYSTEM ONLINE\nLive monitoring • Demo environment",
            font_size=dp(9), bold=True, color=(.57,.65,.68,1),
            size_hint_y=None, height=dp(48), halign="left"))

    def header(self, page_name):
        h = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(74),
                      padding=[dp(25),dp(10),dp(22),dp(10)], spacing=dp(10))
        with h.canvas.before:
            Color(*WHITE)
            bg = Rectangle(pos=h.pos,size=h.size)
        h.bind(pos=lambda o,v:setattr(bg,"pos",v), size=lambda o,v:setattr(bg,"size",v))

        h.add_widget(Label(text="☰", font_size=dp(22), bold=True, color=GREY,
                           size_hint_x=None,width=dp(35)))
        h.add_widget(Label(
            text="Government of India  /  Ministry of Social Justice & Empowerment",
            font_size=dp(10), bold=True, color=GREY, halign="left"))
        h.add_widget(Widget())
        info = BoxLayout(orientation="vertical", size_hint_x=None,width=dp(180))
        info.add_widget(Label(text="Department Official",font_size=dp(10),
                              bold=True,color=BLACK,halign="right"))
        info.add_widget(Label(text="●  Active • 09:42 IST",font_size=dp(8),
                              color=GREEN,halign="right"))
        h.add_widget(info)
        h.add_widget(Label(text="AS",font_size=dp(11),bold=True,color=WHITE,
                           size_hint_x=None,width=dp(36)))
        h.add_widget(Label(text="◈  PARAKH",font_size=dp(14),bold=True,color=NAVY,
                           size_hint_x=None,width=dp(105)))
        return h

    def page(self,title,subtitle):
        self.main_area.clear_widgets()
        self.main_area.add_widget(self.header(title))
        body=BoxLayout(orientation="vertical",padding=[dp(30),dp(22),dp(30),dp(20)],spacing=dp(12))
        title_row=BoxLayout(size_hint_y=None,height=dp(48))
        title_row.add_widget(Label(text=title,font_size=dp(26),bold=True,
                                   color=BLACK,halign="left"))
        body.add_widget(title_row)
        body.add_widget(Label(text=subtitle,font_size=dp(9),bold=True,color=GREY,
                              size_hint_y=None,height=dp(20),halign="left"))
        return body

    def stat_card(self,number,title,detail,accent=BLUE,icon="●"):
        c=Card(orientation="vertical",padding=dp(17),spacing=dp(2))
        c.add_widget(Label(text=f"{icon}   LIVE",font_size=dp(8),bold=True,
                           color=accent,size_hint_y=None,height=dp(22),halign="left"))
        c.add_widget(Label(text=number,font_size=dp(29),bold=True,color=BLACK,halign="left"))
        c.add_widget(Label(text=title,font_size=dp(11),bold=True,color=GREY,halign="left"))
        c.add_widget(Label(text=detail,font_size=dp(8),color=accent,halign="left"))
        return c

    def show_overview(self):
        body=self.page("National Dashboard","LIVE CONTROL ROOM  /  15 SEPTEMBER 2026  •  DEMO DATA")
        body.add_widget(Label(
            text="Good evening, Ananya. Here is the national view of NGOs, inspections, evidence and actions requiring attention.",
            font_size=dp(11),color=GREY,size_hint_y=None,height=dp(28),halign="left"))

        actions=BoxLayout(size_hint_y=None,height=dp(38),spacing=dp(8))
        actions.add_widget(Widget())
        refresh=ActionButton(text="⟳  Refresh dashboard",bg=CREAM2,color=BLACK,size_hint_x=None,width=dp(145))
        refresh.bind(on_release=lambda x:self.show_overview())
        actions.add_widget(refresh)
        new=ActionButton(text="+  Assign inspection",bg=BLUE,size_hint_x=None,width=dp(145))
        new.bind(on_release=lambda x:self.show_inspections())
        actions.add_widget(new)
        body.add_widget(actions)

        cards=GridLayout(cols=4,spacing=dp(12),size_hint_y=None,height=dp(128))
        for args in [
            ("14","Total NGOs","12 compliant • 2 need attention",BLUE,"▣"),
            ("11","Active / Compliant","79% of monitored NGOs",GREEN,"✓"),
            ("03","Inspections Pending","1 high-risk case",ORANGE,"◉"),
            ("02","Issues Detected","2 require action this week",RED,"⚠"),
        ]:
            cards.add_widget(self.stat_card(*args))
        body.add_widget(cards)

        middle=GridLayout(cols=2,spacing=dp(14))
        activity=Card(orientation="vertical",padding=dp(16),spacing=dp(6))
        activity.add_widget(Label(text="RECENT INSPECTION ACTIVITY",font_size=dp(10),
                                  bold=True,color=BLACK,size_hint_y=None,height=dp(25),halign="left"))
        for line in [
            "ABC Foundation        ✓  Inspection submitted     18:34",
            "XYZ Welfare Society   ⚠  Issue flagged             17:20",
            "Nayi Disha Trust       ✓  Compliance verified       15:45",
            "Udaan Welfare Society  ◉  Inspector assigned        14:12",
        ]:
            activity.add_widget(Label(text=line,font_size=dp(9),color=GREY,halign="left"))
        middle.add_widget(activity)

        critical=Card(orientation="vertical",padding=dp(16),spacing=dp(5))
        critical.add_widget(Label(text="CRITICAL ISSUES",font_size=dp(10),bold=True,
                                  color=RED,size_hint_y=None,height=dp(25),halign="left"))
        critical.add_widget(Label(text="HIGH  •  XYZ Welfare Society",font_size=dp(10),
                                  bold=True,color=BLACK,halign="left"))
        critical.add_widget(Label(text="Financial records require verification",font_size=dp(9),
                                  color=GREY,halign="left"))
        critical.add_widget(Label(text="HIGH  •  Sahyog Child Care",font_size=dp(10),
                                  bold=True,color=BLACK,halign="left"))
        critical.add_widget(Label(text="Inspection overdue • 17 days",font_size=dp(9),
                                  color=RED,halign="left"))
        middle.add_widget(critical)
        body.add_widget(middle)

        bottom=Card(orientation="horizontal",padding=dp(14),size_hint_y=None,height=dp(68))
        bottom.add_widget(Label(text="UPCOMING INSPECTIONS\n3 inspections scheduled • 1 surprise inspection recommended",
                                font_size=dp(9),bold=True,color=GREY,halign="left"))
        b=ActionButton(text="VIEW ALL",bg=NAVY,size_hint_x=None,width=dp(105))
        b.bind(on_release=lambda x:self.show_inspections())
        bottom.add_widget(b)
        body.add_widget(bottom)
        self.main_area.add_widget(body)

    def show_registry(self):
        body=self.page("NGO Registry","REGISTERED ORGANISATIONS  /  SEARCH • FILTER • RISK STATUS")
        controls=BoxLayout(size_hint_y=None,height=dp(40),spacing=dp(8))
        search=TextInput(hint_text="Search NGO name or location...",multiline=False,
                         background_color=WHITE,foreground_color=BLACK)
        controls.add_widget(search)
        filt=Spinner(text="All",values=("All","Compliant","Pending","High Risk","Inspection Due"),
                     size_hint_x=None,width=dp(150))
        controls.add_widget(filt)
        body.add_widget(controls)

        scroll=ScrollView()
        rows=GridLayout(cols=1,spacing=dp(8),size_hint_y=None)
        rows.bind(minimum_height=rows.setter("height"))
        for n in NGOS:
            c=Card(orientation="horizontal",padding=dp(12),size_hint_y=None,height=dp(70),spacing=dp(8))
            info=BoxLayout(orientation="vertical")
            info.add_widget(Label(text=n["name"],font_size=dp(12),bold=True,color=BLACK,halign="left"))
            info.add_widget(Label(text=f'{n["location"]}   •   Last inspection: {n["last"]}',
                                  font_size=dp(8),color=GREY,halign="left"))
            c.add_widget(info)
            c.add_widget(Label(text=n["status"],font_size=dp(9),bold=True,
                              color=GREEN if n["status"]=="COMPLIANT" else RED if "ACTION" in n["status"] else ORANGE,
                              size_hint_x=None,width=dp(135)))
            c.add_widget(Label(text=f'RISK {n["risk"]}\n{n["score"]}',font_size=dp(9),
                              bold=True,color=RED if n["risk"]=="HIGH" else ORANGE if n["risk"]=="MEDIUM" else GREEN,
                              size_hint_x=None,width=dp(90)))
            view=ActionButton(text="VIEW",bg=BLUE,size_hint_x=None,width=dp(75))
            view.bind(on_release=lambda x,name=n["name"]:self.show_inspection_detail(name))
            c.add_widget(view)
            rows.add_widget(c)
        scroll.add_widget(rows)
        body.add_widget(scroll)
        self.main_area.add_widget(body)

    def show_inspections(self):
        body=self.page("Inspections","INSPECTION MANAGEMENT  /  SCHEDULED • SURPRISE • COMPLETED")
        tabs=BoxLayout(size_hint_y=None,height=dp(38),spacing=dp(7))
        for t in ["All","Pending","Scheduled","Completed"]:
            b=ActionButton(text=t,bg=NAVY if t=="All" else CREAM2,
                           color=WHITE if t=="All" else BLACK,size_hint_x=None,width=dp(105))
            tabs.add_widget(b)
        tabs.add_widget(Widget())
        assign=ActionButton(text="+  Randomly assign inspection",bg=PURPLE,
                            size_hint_x=None,width=dp(190))
        assign.bind(on_release=lambda x:self.show_assignment_popup())
        tabs.add_widget(assign)
        body.add_widget(tabs)

        data=[
            ("INS-26091","ABC Foundation","16 Sept 2026","SCHEDULED","LOW"),
            ("INS-26092","XYZ Welfare Society","16 Sept 2026","SURPRISE","HIGH"),
            ("INS-26093","Udaan Welfare Society","17 Sept 2026","PENDING","MEDIUM"),
            ("INS-26094","Sahyog Child Care","18 Sept 2026","INSPECTION DUE","HIGH"),
            ("INS-26095","Nayi Disha Trust","12 Sept 2026","COMPLETED","LOW"),
        ]
        for i in data:
            c=Card(orientation="horizontal",padding=dp(12),spacing=dp(8),
                   size_hint_y=None,height=dp(68))
            info=BoxLayout(orientation="vertical")
            info.add_widget(Label(text=i[1],font_size=dp(11),bold=True,color=BLACK,halign="left"))
            info.add_widget(Label(text=f"{i[0]}   •   {i[2]}   •   {i[3]}",
                                  font_size=dp(8),color=GREY,halign="left"))
            c.add_widget(info)
            c.add_widget(Label(text=f"RISK  {i[4]}",font_size=dp(9),bold=True,
                              color=RED if i[4]=="HIGH" else ORANGE if i[4]=="MEDIUM" else GREEN,
                              size_hint_x=None,width=dp(90)))
            v=ActionButton(text="OPEN",bg=BLUE,size_hint_x=None,width=dp(85))
            v.bind(on_release=lambda x,name=i[1]:self.show_inspection_detail(name))
            c.add_widget(v)
            body.add_widget(c)
        body.add_widget(Widget())
        self.main_area.add_widget(body)

    def show_inspection_detail(self,name):
        ngo=next((x for x in NGOS if x["name"]==name),NGOS[0])
        body=self.page("Inspection Detail",f'{name.upper()}  /  FIELD INSPECTION MODULE  •  {ngo["location"]}')
        top=GridLayout(cols=3,spacing=dp(10),size_hint_y=None,height=dp(90))
        top.add_widget(self.stat_card("09:30","Inspection time","15 Sept 2026",BLUE,"◷"))
        top.add_widget(self.stat_card("FIELD-07","Inspector","Department PMU Team",PURPLE,"●"))
        top.add_widget(self.stat_card(ngo["risk"],"Current risk",ngo["score"],RED if ngo["risk"]=="HIGH" else GREEN,"⚠"))
        body.add_widget(top)

        body.add_widget(Label(text="LIVE EVIDENCE & CHECKLIST",font_size=dp(10),bold=True,
                              color=BLACK,size_hint_y=None,height=dp(25),halign="left"))
        checks=["Infrastructure","Staff attendance","Beneficiary records","Financial records",
                "Scheme implementation","Safety / compliance"]
        grid=GridLayout(cols=2,spacing=dp(8))
        for item in checks:
            c=Card(orientation="horizontal",padding=dp(10),size_hint_y=None,height=dp(54))
            c.add_widget(Label(text=item,font_size=dp(10),bold=True,color=BLACK,halign="left"))
            s=Spinner(text="Satisfactory",values=("Satisfactory","Needs Attention","Issue"),
                      size_hint_x=None,width=dp(135))
            c.add_widget(s)
            grid.add_widget(c)
        body.add_widget(grid)

        actions=BoxLayout(size_hint_y=None,height=dp(44),spacing=dp(8))
        for txt,bg in [("Capture Geo-tagged Evidence",CYAN),("Start Random VC",PURPLE),
                       ("Save Inspection",GREEN)]:
            b=ActionButton(text=txt,bg=bg)
            b.bind(on_release=lambda x,t=txt:self.notify(t))
            actions.add_widget(b)
        body.add_widget(actions)
        self.main_area.add_widget(body)

    def show_assignment_popup(self):
        box=BoxLayout(orientation="vertical",padding=dp(15),spacing=dp(10))
        box.add_widget(Label(text="AI / RULE-BASED RANDOM ASSIGNMENT",font_size=dp(13),
                             bold=True,color=BLACK))
        box.add_widget(Label(text="System selected XYZ Welfare Society because of high risk + overdue evidence.",
                             font_size=dp(10),color=GREY))
        ok=ActionButton(text="ASSIGN TO PMU TEAM",bg=PURPLE)
        box.add_widget(ok)
        p=__import__("kivy.uix.popup",fromlist=["Popup"]).Popup(
            title="Inspection Assignment",content=box,size_hint=(None,None),size=(dp(430),dp(220)))
        ok.bind(on_release=p.dismiss)
        p.open()

    def notify(self,text):
        box=BoxLayout(orientation="vertical",padding=dp(15))
        box.add_widget(Label(text=f"✓  {text}\n\nDemo action completed successfully.",
                             font_size=dp(11),color=BLACK))
        p=__import__("kivy.uix.popup",fromlist=["Popup"]).Popup(
            title="PARAKH",content=box,size_hint=(None,None),size=(dp(380),dp(180)))
        close=ActionButton(text="OK",bg=NAVY)
        box.add_widget(close); close.bind(on_release=p.dismiss); p.open()

    def simple_page(self,title,subtitle,items):
        body=self.page(title,subtitle)
        grid=GridLayout(cols=2,spacing=dp(12))
        for heading,detail,accent in items:
            c=Card(orientation="vertical",padding=dp(18),spacing=dp(5))
            c.add_widget(Label(text=heading,font_size=dp(12),bold=True,color=BLACK,halign="left"))
            c.add_widget(Label(text=detail,font_size=d
