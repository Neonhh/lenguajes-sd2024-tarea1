--Definimos el cuaternion y los elementos a exportar del mismo
newtype Cuaternion = Cuaternion (Float, Float, Float, Float) deriving Eq

instance Show Cuaternion where
    show :: Cuaternion -> String
    show (Cuaternion (a, b, c, d)) = show a ++ " + " ++ show b ++ "i + " ++ show c ++ "j + " ++ show d ++ "k"

instance Num Cuaternion where
    --suma
    (+) :: Cuaternion -> Cuaternion -> Cuaternion
    (Cuaternion (a1, b1, c1, d1)) + (Cuaternion (a2, b2, c2, d2)) = Cuaternion (a1 + a2, b1 + b2, c1 + c2, d1 + d2)

    --negado
    negate :: Cuaternion -> Cuaternion
    negate (Cuaternion (a, b, c, d)) = Cuaternion (-a, -b, -c, -d)

    --producto
    (*) :: Cuaternion -> Cuaternion -> Cuaternion
    (Cuaternion (a1, b1, c1, d1)) * (Cuaternion (a2, b2, c2, d2)) = Cuaternion (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2, a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)

    --norma o valor absoluto
    abs :: Cuaternion -> Cuaternion
    abs (Cuaternion (a, b, c, d)) = Cuaternion (sqrt (a^2 + b^2 + c^2 + d^2), 0, 0, 0)

    -- resto de definiciones  - signum y fromInteger
    signum :: Cuaternion -> Cuaternion
    signum (Cuaternion (a, b, c, d)) = Cuaternion (a / norm, b / norm, c / norm, d / norm)
        where 
            norm :: Float
            norm = Main.and (Cuaternion (a, b, c, d))^2
    
    fromInteger :: Integer -> Cuaternion
    fromInteger a = Cuaternion (fromInteger a, 0, 0, 0)

-- valor absoluto como flotante
and :: Cuaternion -> Float
and (Cuaternion (a, b, c, d)) = sqrt (a^2 + b^2 + c^2 + d^2)

-- conjugada
con :: Cuaternion -> Cuaternion
con (Cuaternion (a, b, c, d)) = Cuaternion (a, -b, -c, -d)