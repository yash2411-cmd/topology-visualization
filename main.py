# from calendar import leapdays
from cProfile import label
from tkinter import *
import tkinter as tk

from lib2to3.pytree import NodePattern
import tkinter
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import ring
# from turtle import color
# from unittest import TextTestResult


def ringtop():
    G = nx.DiGraph()
    G.add_node("PC_1",pos=(20,20))
    G.add_node("PC_2",pos=(30,10))
    G.add_node("PC_3",pos=(25,0))
    G.add_node("PC_4",pos=(15,0))
    G.add_node("PC_5",pos=(10,10))
    pos=nx.get_node_attributes(G,'pos')

    G.add_edge("PC_1", "PC_2")
    G.add_edge("PC_2", "PC_3")
    G.add_edge("PC_3", "PC_4")
    G.add_edge("PC_4", "PC_5")
    G.add_edge("PC_5", "PC_1")


    nx.draw(G,pos=pos, with_labels = True,edge_color="red",font_weight='bold',node_shape="p", node_size=2000, node_color = 'orange',font_color = 'black')
    plt.show()

def meshtop():
    G = nx.DiGraph()
    G.add_node("PC_1",pos=(20,20))
    G.add_node("PC_2",pos=(30,10))
    G.add_node("PC_3",pos=(25,0))
    G.add_node("PC_4",pos=(15,0))
    G.add_node("PC_5",pos=(10,10))
    pos=nx.get_node_attributes(G,'pos')

    G.add_edge("PC_1", "PC_2")
    G.add_edge("PC_1", "PC_3")
    G.add_edge("PC_1", "PC_4")
    G.add_edge("PC_1", "PC_5")

    G.add_edge("PC_2", "PC_1")
    G.add_edge("PC_2", "PC_3")
    G.add_edge("PC_2", "PC_4")
    G.add_edge("PC_2", "PC_5")

    G.add_edge("PC_3", "PC_1")
    G.add_edge("PC_3", "PC_2")
    G.add_edge("PC_3", "PC_4")
    G.add_edge("PC_3", "PC_5")

    G.add_edge("PC_4", "PC_1")
    G.add_edge("PC_4", "PC_2")
    G.add_edge("PC_4", "PC_3")
    G.add_edge("PC_4", "PC_5")

    G.add_edge("PC_5", "PC_1")
    G.add_edge("PC_5", "PC_2")
    G.add_edge("PC_5", "PC_3")
    G.add_edge("PC_5", "PC_4")


    nx.draw(G,pos=pos, with_labels = True,edge_color="red", font_weight='bold',node_shape="p", node_size=2000, node_color = 'orange',font_color = 'black')
    plt.show()

def startop():
    G = nx.DiGraph()

    G.add_node("Hub",pos=(20,10))
    G.add_node("PC_1",pos=(20,20))
    G.add_node("PC_2",pos=(30,10))
    G.add_node("PC_3",pos=(25,0))
    G.add_node("PC_4",pos=(15,0))
    G.add_node("PC_5",pos=(10,10))
    pos=nx.get_node_attributes(G,'pos')

    G.add_edge("Hub", "PC_1")
    G.add_edge("Hub", "PC_2")
    G.add_edge("Hub", "PC_3")
    G.add_edge("Hub", "PC_4")
    G.add_edge("Hub", "PC_5")
    # G.add_edge("PC_0", "PC_1")


    nx.draw(G,pos=pos, with_labels = True ,edge_color="red", font_weight='bold',node_shape="p", node_size=2000, node_color = 'orange',font_color = 'black')
    plt.show()

def bustop():
    G = nx.DiGraph()

    G.add_node("1",pos=(20,15))
    G.add_node("2",pos=(68,15))
    G.add_node("PC_1",pos=(28,15.003))
    G.add_node("PC_2",pos=(36,14.996))
    G.add_node("PC_3",pos=(44,15.003))
    G.add_node("PC_4",pos=(52,14.996))
    G.add_node("PC_5",pos=(60,15.003))
    G.add_node("-",pos=(28,15))
    G.add_node("--",pos=(36,15))
    G.add_node(".",pos=(44,15))
    G.add_node("..",pos=(52,15))
    G.add_node("-.",pos=(60,15))

    pos=nx.get_node_attributes(G,'pos')

    G.add_edge("1", "2")
    G.add_edge("2", "1")
    G.add_edge("-","PC_1")
    G.add_edge("--","PC_2")
    G.add_edge(".","PC_3")
    G.add_edge("..","PC_4")
    G.add_edge("-.","PC_5")

    nx.draw(G,pos=pos, with_labels = True,edge_color="red",font_weight='bold',node_shape="p", node_size=100, node_color = 'white',font_color = 'black')
    plt.show()




root= Tk()
root.geometry("620x520")
root.title("topology visualizer")
# root.configure(bg="lightgreen")
bg= PhotoImage(file="bg.png")
label1= Label(root,image=bg)
label1.place(x=0,y=0)

t= Label(root,text="Network Topology Visualization",font=("times new roman",25,"bold"))
t.pack()


but1= tk.Button(root,text="Ring",font=("times new roman",15,"bold"),width=15,height=2,command=ringtop,bg="lightgreen")
but1.place(x=30,y=100)
# but1.pack()
but2= tk.Button(root,text="Bus",font=("times new roman",15,"bold"),width=15,height=2,command=bustop,bg="lightgreen")
but2.place(x=400,y=100)
# but2.pack()
but3= tk.Button(root,text="Star",font=("times new roman",15,"bold"),width=15,height=2,command=startop,bg="lightgreen")
but3.place(x=30,y=300)
# but3.pack()
but4= tk.Button(root,text="Mesh",font=("times new roman",15,"bold"),width=15,height=2,command=meshtop,bg="lightgreen")
but4.place(x=400,y=300)
# but4.pack()

root.mainloop()