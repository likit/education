Basic R function
========================================================
## Why function?


```r
temp <- 45  # Fahrenheit
kelvin <- ((temp - 32) * (5/9)) + 273.15
cat("Temperature in Kelvin is", kelvin)
```

```
## Temperature in Kelvin is 280.4
```

```r
temp <- 54  # Fahrenheit
kelvin <- ((temp - 32) * (5/9)) + 273.15
cat("Temperature in Kelvin is", kelvin)
```

```
## Temperature in Kelvin is 285.4
```

```r
temp <- 44  # Fahrenheit
kelvin <- ((temp - 32) * (5/9)) + 273.15
cat("Temperature in Kelvin is", kelvin)
```

```
## Temperature in Kelvin is 279.8
```

```r
temp <- 35  # Fahrenheit
kelvin <- ((temp - 32) * (5/9)) + 273.15
cat("Temperature in Kelvin is", kelvin)
```

```
## Temperature in Kelvin is 274.8
```

....

Basic syntax

function(argument,...) {
  # function body
}


Examples

A very simple function

```r
say.hi <- function() {
    cat("Hi!")
}

say.hi()
```

```
## Hi!
```


A function can take aguments


```r
double.num <- function(num) {
    cat("Argument is", num, "\n")
    result <- num * 2
    return(result)
}
```



```r
double.num(30)
```

```
## Argument is 30
```

```
## [1] 60
```

```r
double.num(35)
```

```
## Argument is 35
```

```
## [1] 70
```

```r
double.num(45)
```

```
## Argument is 45
```

```
## [1] 90
```

```r

output <- double.num(30)  # assign the return value to a variable
```

```
## Argument is 30
```

```r
output
```

```
## [1] 60
```



```r
fahr_to_kelvin <- function(temp) {
    kelvin <- ((temp - 32) * (5/9)) + 273.15
    return(kelvin)
}
```



```r
fahr_to_kelvin(45)
```

```
## [1] 280.4
```

```r
fahr_to_kelvin(56)
```

```
## [1] 286.5
```

```r
fahr_to_kelvin(24)
```

```
## [1] 268.7
```

```r
fahr_to_kelvin(44)
```

```
## [1] 279.8
```


It even works with a vector!

```r
fahr_to_kelvin(c(45, 56, 24, 44))
```

```
## [1] 280.4 286.5 268.7 279.8
```

