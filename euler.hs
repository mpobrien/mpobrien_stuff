euler_one = sum ( filter ( isMultiple ) [1..999] ) where isMultiple x = mod x 5 == 0 || mod x 3 == 0


fibList xs n n1 = if ( n + n1 ) > 4000000 then xs else fibList (xs ++ [n+n1]) (n1) (n+n1)
euler_two = sum ( filter ( even ) ( fibList [] 0 1 ) )
