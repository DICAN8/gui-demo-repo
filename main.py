from tkinter import *
import customtkinter
from ctypes import windll



windll.shcore.SetProcessDpiAwareness(1)
#Window
window = Tk()
window.geometry('1920x1024')
window.config(background='#212121')

#Constants
font_family = 'Malgun' #font
button_Hover_color = '#2b2b2b'
inactive_button_color = '#828378'
left_side_frame_bg = '#262626'
main_background_color = '#212121'

#PhotoImages
api_img = PhotoImage(file='Left Frame Icons\\API.png')
api_dim_img = PhotoImage(file='Left Frame Icons\\API_dim.png')
team_img = PhotoImage(file='Left Frame Icons\\team.png')
team_hover_img = PhotoImage(file='Left Frame Icons\\team_hover.png')
environments_img = PhotoImage(file='Left Frame Icons\\environments.png')
environments_dim_img = PhotoImage(file='Left Frame Icons\\environments_dim.png')
servers_img = PhotoImage(file='Left Frame Icons\\server.png')
servers_dim_img = PhotoImage(file='Left Frame Icons\\server_dim.png')
monitors_img = PhotoImage(file='Left Frame Icons\\monitor.png')
monitors_dim_img = PhotoImage(file='Left Frame Icons\\monitor_dim.png')
flows_img = PhotoImage(file='Left Frame Icons\\flows.png')
flow_dim_img = PhotoImage(file='Left Frame Icons\\flows_dim.png')
history_img = PhotoImage(file='Left Frame Icons\\History.png')
history_dim_img = PhotoImage(file='Left Frame Icons\\History_dim.png')
collections_dim_img = PhotoImage(file='Left Frame Icons/collections_dim.png')
collections_img = PhotoImage(file='Left Frame Icons/collections.png')
down_arrow = PhotoImage(file='Left Frame Icons\\down_arrow.png')
up_arrow = PhotoImage(file='Left Frame Icons\\up_arrow.png')
pyramid_img = PhotoImage(file='Left Frame Icons\\pyramid.png')
menu_img = PhotoImage(file='Left Frame Icons\\menu.png')
white_pyramid_image = PhotoImage(file='Left Frame Icons\\pyramid_white.png')

#dictionary for hover effect
button_list = ['Collections', 'APIs', 'Environments', 'Mock Servers', 'Monitors', 'Flows', 'History']
images_list = [collections_dim_img, api_dim_img, environments_dim_img, servers_dim_img, monitors_dim_img, flow_dim_img, history_dim_img]
button_names=[]
for each_name in button_list:
    button_names.append(each_name+'_btn')

#hover functions(with bind)
def chcolor_collections(event):
    button_names[0].config(fg='white', bg='#2c2c2c', image=collections_img)
    button_names[0].fg = 'white'
    button_names[0].image = collections_img
    button_names[0].bg = '#2c2c2c'
def normal_collections(event):
    button_names[0].config(fg='#B8B3B3', bg=left_side_frame_bg, image=collections_dim_img)
    button_names[0].fg = '#B8B3B3'
    button_names[0].image = collections_dim_img
    button_names[0].bg = left_side_frame_bg
def chcolor_APIs(event):
    button_names[1].config(fg='white', bg='#2c2c2c', image=api_img)
    button_names[1].fg = 'white'
    button_names[1].image = api_img
    button_names[1].bg = '#2c2c2c'
def normal_APIs(event):
    button_names[1].config(fg='#B8B3B3', bg=left_side_frame_bg, image=api_dim_img)
    button_names[1].fg = '#B8B3B3'
    button_names[1].image = collections_dim_img
    button_names[1].bg = left_side_frame_bg
def chcolor_environments(event):
    button_names[2].config(fg='white', bg='#2c2c2c', image=environments_img)
    button_names[2].fg = 'white'
    button_names[2].image = environments_img
    button_names[2].bg = '#2c2c2c'
def normal_environments(event):
    button_names[2].config(fg='#B8B3B3', bg=left_side_frame_bg, image=environments_dim_img)
    button_names[2].fg = '#B8B3B3'
    button_names[2].image = environments_dim_img
    button_names[2].bg = left_side_frame_bg
def chcolor_servers(event):
    button_names[3].config(fg='white', bg='#2c2c2c', image=servers_img)
    button_names[3].fg = 'white'
    button_names[3].image = servers_img
    button_names[3].bg = '#2c2c2c'
def normal_servers(event):
    button_names[3].config(fg='#B8B3B3', bg=left_side_frame_bg, image=servers_dim_img)
    button_names[3].fg = '#B8B3B3'
    button_names[3].image = servers_dim_img
    button_names[3].bg = left_side_frame_bg
def chcolor_monitors(event):
    button_names[4].config(fg='white', bg='#2c2c2c', image=monitors_img)
    button_names[4].fg = 'white'
    button_names[4].image = monitors_img
    button_names[4].bg = '#2c2c2c'
def normal_monitors(event):
    button_names[4].config(fg='#B8B3B3',bg=left_side_frame_bg, image=monitors_dim_img)
    button_names[4].fg = '#B8B3B3'
    button_names[4].image = monitors_dim_img
    button_names[4].bg = left_side_frame_bg
def chcolor_flows(event):
    button_names[5].config(fg='white', bg='#2c2c2c', image=flows_img)
    button_names[5].fg = 'white'
    button_names[5].image = flows_img
    button_names[5].bg = '#2c2c2c'
def normal_flows(event):
    button_names[5].config(fg='#B8B3B3', bg=left_side_frame_bg, image=flow_dim_img)
    button_names[5].fg = '#B8B3B3'
    button_names[5].image = flow_dim_img
    button_names[5].bg = left_side_frame_bg
def chcolor_history(event):
    button_names[6].config(fg='white', bg='#2c2c2c', image=history_img)
    button_names[6].fg = 'white'
    button_names[6].image = history_img
    button_names[6].bg = '#2c2c2c'
def normal_history(event):
    button_names[6].config(fg='#B8B3B3', bg=left_side_frame_bg, image=history_dim_img)
    button_names[6].fg = '#B8B3B3'
    button_names[6].image = history_dim_img
    button_names[6].bg = left_side_frame_bg
def chcolor_team(event):
    LFteam_workspace_button.config(fg='#0000fd', image=team_hover_img)
    LFteam_workspace_button.fg = '0000fd'
    LFteam_workspace_button.image = team_hover_img
def normal_team(event):
    LFteam_workspace_button.config(fg='white', image=team_img)
    LFteam_workspace_button.fg = 'white'
    LFteam_workspace_button.image = team_img

def button_click():
    global clicked_button
    clicked_button = customtkinter.CTkButton(master=window,
                            fg_color=main_background_color,
                            text_font=(font_family, 12),
                            text='Workspace',
                            bg_color=main_background_color,
                            width=60,
                            border_width=2,

                            border_color='#9cb8e1',
                            corner_radius=5,
                            text_color='white',
                            hover_color='#2c2c2c',
                            image=up_arrow,
                            command=button_release,
                            compound='right'
                            )
    clicked_button.place(x=78, y=6)
    global in_frame
    in_frame = customtkinter.CTkFrame(master=window,
                                      width=380,
                                      height=560,
                                      fg_color=main_background_color,
                                      corner_radius=5,
                                      border_color='#2b2b2f',
                                      border_width=1
                                      )
    in_frame.place(x=78, y=40)
    global search_box
    search_box = customtkinter.CTkEntry(master=in_frame,
                                        border_width=3,
                                        border_color='blue',
                                        width=190,
                                        height=40,
                                        text_color='white',
                                        text_font=(font_family, 9, 'bold'),
                                        placeholder_text='Search workspaces',
                                        placeholder_text_color='#5b544c',
                                        fg_color=main_background_color
                                        )
    search_box.place(x=15, y=15)
    global button_in_frame
    button_in_frame = customtkinter.CTkButton(master=in_frame,
                                              fg_color='#3b3b3b',
                                              text='Create Workspace',
                                              text_font=(font_family, 10, 'bold'),
                                              hover_color='#6b6b6b',
                                              height=33,
                                              border_width=0,
                                              text_color='white'
                                              )
    button_in_frame.place(x=220, y=20)
def button_release():
    clicked_button.destroy()
    in_frame.destroy()
    # search_box.destroy()


def change_to_entry():
    customtkinter.CTkButton(master=window,
                            image=white_pyramid_image,
                            fg_color=main_background_color,
                            bg_color=left_side_frame_bg
                            )
    entry = customtkinter.CTkEntry(master=window,
                                   bg_color=main_background_color,


                                   )
#Menubar
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0) #Creates file menu
menubar.add_cascade(label='File', font=(font_family, 8))

editMenu = Menu(menubar, tearoff=0)#Creates edit menu
menubar.add_cascade(label='Edit', font=(font_family, 8))

viewMenu = Menu(menubar, tearoff=0)#Creates view menu
menubar.add_cascade(label='View', font=(font_family, 8))

helpMenu = Menu(menubar, tearoff=0)#Creates help menu
menubar.add_cascade(label='Help', font=(font_family, 8))


#Left Side Frame(LF)
LF = Frame(window,                                       #Frame body
                  bg=left_side_frame_bg,
                  width=500,
                  height=900
                  )
LF.place(x=0, y=50)

LFinside_frame = customtkinter.CTkFrame(master=window,                   #Frame beside buttons
                                   fg_color=left_side_frame_bg,
                                   bg_color='#2b2b2f',
                                   width=315,
                                   height=850,
                                   borderwidth=2,
                                   corner_radius=0
                                )
LFinside_frame.place(x=85, y=42)

#Home,workspaces ,API Network, Explore buttons

LFtopHome_btn = customtkinter.CTkButton(master=window,
                                        fg_color=main_background_color,
                                        text_font=(font_family, 12),
                                        text='Home',
                                        bg_color=main_background_color,
                                        width=60,
                                        corner_radius=5,
                                        text_color='white',
                                        hover_color='#2c2c2c'
                                        )
LFtopHome_btn.place(x=12, y=8)

LFtopWorkspaces_button = customtkinter.CTkButton(master=window,
                                                 fg_color=main_background_color,
                                                 text_font=(font_family, 12),
                                                 text='Workspace',
                                                 bg_color=main_background_color,
                                                 width=60,
                                                 border_width=0,

                                                 border_color=main_background_color,
                                                 corner_radius=5,
                                                 text_color='white',
                                                 hover_color='#2c2c2c',
                                                 image=down_arrow,
                                                 command=button_click,
                                                 compound='right'
                                                   )

LFtopWorkspaces_button.place(x=78, y=8)
LFtopWorkspaces_button
#Topbar Frame
LFtop_bar = customtkinter.CTkFrame(master=window,                   #Topbar frame containing, team workspace,
                                   fg_color=left_side_frame_bg,     #new and import buttons
                                   bg_color='#2b2b2f',
                                   width=400,
                                   height=40,
                                   borderwidth=2,
                                   corner_radius=0
                                )
LFtop_bar.place(x=0, y=40)
LFteam_workspace_button = Button(master=window,                         #Team Workspace button
                                 font=(font_family, 9, 'bold'),
                                 fg='white',
                                 bg=left_side_frame_bg,
                                 text='Team Workspace',
                                 image=team_img,
                                 compound='left',
                                 borderwidth=0,
                                 padx=5,
                                 activebackground=left_side_frame_bg,
                                 activeforeground='#0000fd',
                                 takefocus=0
                                )
LFteam_workspace_button.place(x=0, y=60)

LFnew_button = customtkinter.CTkButton(master=window,            #'New' button
                                       text='New',
                                       text_color='white',
                                       text_font=(font_family, 9, 'bold'),
                                       hover_color=None,
                                       bg_color=left_side_frame_bg,
                                       fg_color='#2c2c2c',
                                       width=50
                                       )
LFnew_button.place(x=270, y=45)

LFimport_button = customtkinter.CTkButton(master=window,                 #Import button
                                       text='Import',
                                       text_color='white',
                                       text_font=(font_family, 9, 'bold'),
                                       hover_color=None,
                                       bg_color=left_side_frame_bg,
                                       fg_color='#2c2c2c',
                                       width=70
                                       )
LFimport_button.place(x=325, y=45)

#Widgets in Inside Frame

LFframe_widget_btn = customtkinter.CTkButton(master=window,
                                             image=pyramid_img,
                                             bg_color=left_side_frame_bg,
                                             text='wdiakl,djlkjfakttrrjrgrgfhhkjgkhg',
                                             border_width=1,
                                             border_color='#2b2b2f',
                                             fg_color=left_side_frame_bg,
                                             text_color=left_side_frame_bg,
                                             width=250,
                                             hover_color='#2c2c2c',
                                             command=change_to_entry
                                             )
LFframe_widget_btn.place(x=125, y=83)

LFframe_widget_plus_btn = customtkinter.CTkButton(master=window,
                                                  bg_color=left_side_frame_bg,
                                                  text='+',
                                                  text_font=('Helvetica', 15),
                                                  border_width=0,
                                                  width=20,
                                                  fg_color=left_side_frame_bg,
                                                  text_color=inactive_button_color,
                                                  hover_color='#2c2c2c'
                                                  )
LFframe_widget_plus_btn.place(x=103, y=83)

LFframe_widget_menu_btn = customtkinter.CTkButton(master=window,
                                                  bg_color=left_side_frame_bg,
                                                  image=menu_img,
                                                  text_font=('Helvetica', 15),
                                                  border_width=0,
                                                  width=20,
                                                  fg_color=left_side_frame_bg,
                                                  text_color=inactive_button_color,
                                                  text=None,
                                                  hover_color='#2c2c2c'
                                                  )
LFframe_widget_menu_btn.place(x=363, y=83)
#Navigation buttons
LFbuttons_container = customtkinter.CTkFrame(master=window)
LFbuttons_container.place(x=0, y=80)
for index in range(len(button_list)):
    button_names[index] = Button(LFbuttons_container, activeforeground='white', activebackground=left_side_frame_bg, text=button_list[index], font=(font_family, 8), width=100, bg=left_side_frame_bg, fg='#B8B3B3', pady=10, image=images_list[index], compound='top', borderwidth=0)
    button_names[index].pack(side='top')

#Instances of buttons hover effect
button_names[0].bind('<Enter>', chcolor_collections)
button_names[0].bind('<Leave>', normal_collections)
button_names[1].bind('<Enter>', chcolor_APIs)
button_names[1].bind('<Leave>', normal_APIs)
button_names[2].bind('<Enter>', chcolor_environments)
button_names[2].bind('<Leave>', normal_environments)
button_names[3].bind('<Enter>', chcolor_servers)
button_names[3].bind('<Leave>', normal_servers)
button_names[4].bind('<Enter>', chcolor_monitors)
button_names[4].bind('<Leave>', normal_monitors)
button_names[5].bind('<Enter>', chcolor_flows)
button_names[5].bind('<Leave>', normal_flows)
button_names[6].bind('<Enter>', chcolor_history)
button_names[6].bind('<Leave>', normal_history)
LFteam_workspace_button.bind('<Enter>', chcolor_team)
LFteam_workspace_button.bind('<Leave>', normal_team)

window.mainloop()