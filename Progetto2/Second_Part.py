import numpy as np
from scipy.misc import imsave
import scipy.fftpack as sp
import cv2
class DCT2Core():
	def read_image(filename):
		return cv2.imread(filename, 0)

	def dct_image(f):
		f = np.array(f)
		c = sp.dct(sp.dct(f.T, norm="ortho").T, norm = "ortho")
		return c

	def inverse_dct_image(c):
		ff = sp.idct(sp.idct(c.T, norm="ortho").T, norm="ortho")
		ff.round()
		functOverUnderFix = np.vectorize(DCT2Core.over_under_fix)
		return functOverUnderFix(ff)

	def save_output_img(img, outputfile):
		img = cv2.imwrite(outputfile, img)

	#Caso in cui valori eccedono scala RGB
	def over_under_fix(x):
		if x<0: return 0
		elif x > 255: return 255
		else: return x

	def multiply(c, beta, d):
		row_matrix,  column_matrix = c.shape
		for i in range(0, row_matrix):
			for j in range(0, column_matrix):
				if (i + j) >= d.get():
					c[i, j] = c[i, j] * np.float64(beta.get())
		return c

	def compute_app(loaded_img, outputfile, row_matrix, column_matrix, beta, d):
		if(DCT2Core.correct_input_validation(d, row_matrix, column_matrix)):
			c = DCT2Core.dct_image(loaded_img)
			c = DCT2Core.multiply(c, beta, d)
			imgBmpOut = DCT2Core.inverse_dct_image(c)
			DCT2Core.save_output_img(imgBmpOut, outputfile)
			return True
		return False
	def correct_input_validation(d, nrow, ncol):
		if(d.get() <= nrow + ncol and d.get()>=0):
			return True
		else:
			return False
	def get_img(inputfile):
		imgBmp = DCT2Core.read_image(inputfile)
		return imgBmp
	def get_image_difference(input_img, output_img):
		return cv2.absdiff(input_img, output_img)
