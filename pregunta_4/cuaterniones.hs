--Definimos el cuaternion y los elementos a exportar del mismo
--exportaremos el tipo de datos junto con los operadores
module Cuaterniones (Cuaternion(..), (+), (~), (*), (&)) where

-- Ocultamos los operadores conflictivos del Prelude
import Prelude hiding ((+), (*), (&))

--el tipo de datos consiste en 4 Floats, que representan los elementos del cuaternion (a, bi, cj, dk)
--y pueden ser mostrados por pantalla (Show) y comparados por igualdad (Eq)
data Cuaternion = Cuaternion Float Float Float Float deriving (Eq, Show)

--definimos los operadores

--suma
infixl 6 +
(+) :: Cuaternion -> Cuaternion -> Cuaternion
(Cuaternion a1 b1 c1 d1) + (Cuaternion a2 b2 c2 d2) = Cuaternion (a1 + a2) (b1 + b2) (c1 + c2) (d1 + d2)

--conjugada
(~) :: Cuaternion -> Cuaternion 
(~) (Cuaternion a b c d) = Cuaternion a (-b) (-c) (-d)

--producto
infixl 7 *
(*) :: Cuaternion -> Cuaternion -> Cuaternion
(Cuaternion a1 b1 c1 d1) * (Cuaternion a2 b2 c2 d2) = Cuaternion (a1*a2 - b1*b2 - c1*c2 - d1*d2) (a1*b2 + b1*a2 + c1*d2 - d1*c2) (a1*c2 - b1*d2 + c1*a2 + d1*b2) (a1*d2 + b1*c2 - c1*b2 + d1*a2)

-- norma (este operador councide con el que se una para and bit a bit)
(&) :: Cuaternion -> Float
(&) (Cuaternion a b c d) = sqrt (a^2 + b^2 + c^2 + d^2)

--definicion de las operaciones con numeros enteros o flotantes
    -- No alcance a esto :,)


