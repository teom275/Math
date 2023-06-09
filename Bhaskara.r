# Ingresar los coeficientes A, B y C de la ecuación cuadrática
A <- as.numeric(readline("Ingrese el valor de A: "))
B <- as.numeric(readline("Ingrese el valor de B: "))
C <- as.numeric(readline("Ingrese el valor de C: "))

# Calcular el discriminante
discriminante <- B^2 - 4*A*C

# Calcular las raíces de la ecuación cuadrática usando el método de Bhaskara
if (discriminante > 0) {
  x1 <- (-B + sqrt(discriminante))/(2*A)
  x2 <- (-B - sqrt(discriminante))/(2*A)
  cat("Las raíces de la ecuación cuadrática son:", x1, "y", x2)
} else if (discriminante <- 0) {
  x1 <- (-B)/(2*A)
  cat("La única raíz de la ecuación cuadrática es:", x1)
} else {
  cat("Raíces complejas.")
}
