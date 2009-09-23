import Data.Maybe
-- ONE
euler_one = sum ( filter ( isMultiple ) [1..999] ) where isMultiple x = mod x 5 == 0 || mod x 3 == 0

-- TWO

fibList xs n n1 = if ( n + n1 ) > 4000000 then xs else fibList (xs ++ [n+n1]) (n1) (n+n1)
euler_two = sum ( filter ( even ) ( fibList [] 0 1 ) )

----- THREE
isDivisibleBy :: Integer -> Integer -> Bool
isDivisibleBy x n = x `mod` n == 0 -- return True if x is divisible by n

isComposite x = any ( isDivisibleBy x ) [2..floor (sqrt ( fromIntegral x ) )]
isPrime x = not ( isComposite x )

factorList x = concat ( catMaybes (map ( checkFactors x ) possibles ) )
                where checkFactors x1 n1 | isDivisibleBy x1 n1 == False = Nothing
                      checkFactors x1 n1 = Just [n1, x1 `div` n1]
                      possibles = [2..floor (sqrt ( fromIntegral x ) )]
euler_three = maximum ( filter isPrime ( factorList 600851475143 ) )

----- FOUR
