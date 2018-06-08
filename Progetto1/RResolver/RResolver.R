library("Matrix")
library(binhf)
solve_LU <- function(filea) {
  A <- readMM(filea)
  print(dim(A))
  print("loaded matrix")
  #matrix positive -> dsCMatrix
  #matrix not positive -> dgCMatrix
  A <- as(A, "dgCMatrix")
  #create xe
  xe <- rep(1, ncol(A))
  xo <- rep(0, ncol(A))
  b <- A %*% xe #prodotto vettoriale
  print("start LU decomposition")
  print(gc())
  # Start the clock!
  ptm <- proc.time()
  x <- solve(A, b, sparse = TRUE)
  # Stop the clock
  time <- proc.time() - ptm
  print(gc())
  norm_vec <- function(x) sqrt(sum(x ^ 2)) 
  error <- norm_vec(x - xe) / norm_vec(xe)
  return(list(error = error, A = A, b = b, x = x, time = time))
}

r <- solve_LU(filea = "/Users/lorenzodivito/Desktop/Universita/MetodiCalcoloScientifico/FirstProject/MatrixNotPositive/mtx/ex19.mtx")
r$time
r$error