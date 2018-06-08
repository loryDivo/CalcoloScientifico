from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter import ttk
from Second_Part import DCT2Core
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plot
import cv2

class DCTFrame(Frame):
		inputFile = ""
		part = ""
		#init chiamato per inizializzazione oggetto
		#self è l'oggetto stesso		
		def __init__(self):
			#Inizializza il frame
			Frame.__init__(self, borderwidth=5)
			self.master.title("DCT2App")
			self.master.rowconfigure(5, weight=1)
			self.master.columnconfigure(5, weight=1)
			self.grid(sticky=W+E+N+S)
			#inserimento immagine
			self.inputTitle = Label(self, text= "Carica un immagine")
			self.inputTitle.grid(row=4, column=0, sticky=W)
			self.inputfile = StringVar()
			self.labelImage = Entry(self, textvariable=self.inputfile, width=70, bd=5)
			self.inputfile.set("")
			self.labelImage.grid(row=5, column=1, sticky=W)
			#bottone ricerca immagine directory
			self.buttonLoad = Button(self, text="Carica", command=self.load_file, width=10)
			self.buttonLoad.grid(row=5, column=6, sticky=W)
			#Sezione scelta parametri
			self.labelParamd = Label(self, text="Inserisci valore di d compreso tra 0 e N + M - 2")
			self.labelParamd.grid(row=9, column=0, sticky=W)
			#parametro d
			self.d_param= IntVar()
			self.dParam=Entry(self, textvariable=self.d_param, width=7, bd=5)
			self.dParam.grid(row=11, column=0, sticky=W)
			#parametro beta
			self.labelParambeta=Label(self, text="Inserisci valore di beta")
			self.labelParambeta.grid(row=12, column=0, sticky=W)
			self.b_param=IntVar()
			self.b_param=Entry(self, textvariable=self.b_param, width=7, bd=5)
			self.b_param.grid(row=13, column=0, sticky=W)
			#avvio algoritmo desiderato
			self.run_button = Button(self, text="Avvio", command=self.run_dct, width=10)
			self.run_button.grid(row=15, column=0, sticky=W)

		def load_file(self):
			filename = askopenfilename(filetypes=(("Bmp image", "*.bmp"),
													("JPEG image", "*.jpg"),
													("PNG image", "*.png"),
                                           ("All files", "*.*")))
			if filename:
				try:
					self.inputfile.set(filename)
					self.loaded_img = DCT2Core.get_img(filename)
					self.row_matrix,  self.column_matrix = self.loaded_img.shape
					self.maxd = self.row_matrix + self.column_matrix
					self.labelParamd.config(text=f"Inserisci valore di d compreso tra 0 e {self.maxd}")
				except:
					showerror("Apertura File", "Impossibile aprire il file\n'%s'" % filename)
				return

		def run_dct(self):
			if(self.inputfile.get()!= ""):
				self.outputfile= self.inputfile.get().split(".")[0] + "transformed" + ".bmp"
				self.correct_result = DCT2Core.compute_app(self.loaded_img, self.outputfile, self.row_matrix, self.column_matrix, self.b_param, self.d_param)
				if(self.correct_result):
					self.input_img = self.load_image(self.inputfile.get())
					self.output_img = self.load_image(self.outputfile)
					plot.figure(1)
					#grafico composto da 1 riga e due colonne -> prima colonna immagine input
					plot.subplot(121)
					plot.imshow(self.input_img, cmap='gray')
					#seconda colonna immagine output
					plot.subplot(122)
					plot.imshow(self.output_img, cmap='gray')
					fig = plot.gcf()
					fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))
					manager = plot.get_current_fig_manager()
					manager.resize(*manager.window.maxsize())
					#differenza img
					self.output_img = DCT2Core.get_img(self.outputfile)
					self.image_difference = DCT2Core.get_image_difference(self.input_img, self.output_img)
					#grafico differenza immagini
					plot.figure(2)
					plot.subplot(111)
					plot.imshow(self.image_difference, cmap='gray')
					fig = plot.gcf()
					fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))
					manager = plot.get_current_fig_manager()
					manager.resize(*manager.window.maxsize())
					plot.show()
				else:
					showerror("Input errato", "Impossibile usare il parametro ")
			else:
				showerror("Apertura File", "Impossibile aprire il file")

		def load_image(self, path):
			image_load = cv2.imread(path, 0)
			return image_load


#Lanciato come programma e non come modulo per utilizzare parte delle funzioni
if __name__ == "__main__":
	DCTFrame().mainloop()