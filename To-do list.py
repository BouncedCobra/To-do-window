from tkinter import *
import tkinter.messagebox

def entertask():
    #Nueva ventana para escribir una tarea
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Ingresa algun texto")
        else:
            listbox_task.insert(END,input_text)
            #Cerramos la ventana nueva
            root1.destroy()
    root1=Tk()
    root1.title("Agregar tarea")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Agregar tarea",command=add)
    button_temp.pack()
    root1.mainloop()
    
#Funcion para eliminar tareas
def deletetask():
    #Obtenemos el elemento seleccionado y lo eliminamos
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])
    
#Funcion para marcar como completada la tarea
def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #Convierte el texto seleccionado en un String
    temp_marked=listbox_task.get(marked)
    #Se agrega un ✔ 
    temp_marked=temp_marked+" ✔"
    #Elimina el anterior y se agrega el nuevo
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)
    
    #design
window = Tk() #widget para crear una aplicacion window

#window title
window.title("Lista to-do")

frame_task=Frame(window)
frame_task.pack()

listbox_task=Listbox(frame_task, bg="black",fg="white",height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#Button widget
entry_button=Button(window, text="Agregar tarea", width=50,command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="Eliminar tarea seleccionada",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Marcar como completada",width=50,command=markcompleted)
mark_button.pack(pady=3)


window.mainloop() #final de la ventana
